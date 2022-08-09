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

   ratingCount = ratings.groupBy("movieID").avg("rating")

   counts = ratings.groupBy("movieID").count()

   avgAndCount = counts.join(ratingCount,"movieID")

   popularAvgAndCount = avgAndCount.filter("count > 10")

   topTen = popularAvgAndCount.orderBy("avg(rating)").take(10)

   for movie in topTen:
        print (movieNames[movie[0]], movie[1], movie[2])

   spark.stop()