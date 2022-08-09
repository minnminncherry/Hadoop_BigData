from attr import field
from pyspark.sql import SparkSession
from pyspark.sql import Row
from pyspark.ml.recommendation import ALS
from pyspark.sql.functions import lit

def loadMovieNames():
   movieNames = {}
   with open("../u.item",encoding = "ISO-8859-1") as f:
      for line in f:
         fields = line.split('|')
         movieNames[int(fields[0])] = fields[1]
   return movieNames

def parseInput(line):
   fields = line.value.split()
   return Row(userID = int(fields[0]), movieID = int(fields[1]), rating = float(fields[2]))

if __name__ == "__main__":
   spark = SparkSession.builder.appName("movieRecs").getOrCreate()

   movieNames = loadMovieNames()

   lines = spark.read.text("../u.data").rdd

   ratingsRDD = lines.map(parseInput)

   ratings = spark.createDataFrame(ratingsRDD).cache()

   als = ALS(maxIter = 5, regParam = 0.01, userCol = "userID", itemCol = "movieID", ratingCol = "rating")

   model = als.fit(ratings)

   print ("\n Rating for user ID 0:")
   userRating = ratings.filter("userID = 0")
   for rating in userRating.collect():
      print (movieNames[rating['movieID']], rating['rating'])
   
   print ("\n top 20 movie recommendations : ")
   ratingCounts = ratings.groupBy("movieID").count().filter("count > 100")
   popularMovies = ratingCounts.select("movieID").withColumn('userID',lit(0))

   recommendations = model.transform(popularMovies)
   topRecommendation = recommendations.sort(recommendations.prediction.desc()).take(20)

   for recommendation in topRecommendation:
      print (movieNames[recommendation['movieID']], recommendation['prediction'])

   spark.stop()