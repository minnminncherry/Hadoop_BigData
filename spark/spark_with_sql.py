from pyspark.sql import SparkSession
from pyspark.sql import Row

def loadMovieNames():
   movieNames = {}
   with open("../u.item",encoding = "ISO-8859-1") as f:
      for line in f:
         fields = line.split('|')
         movieNames[int(fields[0])] = fields[1]
   return movieNames

def parseInput(line):
   fields = line.split()
   return Row(movieID = int(fields[1]), rating = float(fields[2]))

if __name__ == '__main__':
   spark = SparkSession.builder.appName("PopularMovies").getOrCreate()

   movieNames = loadMovieNames()

   lines = spark.sparkContext.textFile("../u.data")
   movieRatings = lines.map(parseInput)

   movieDataSet = spark.createDataFrame(movieRatings)

   averageRatings = movieDataSet.groupBy("movieID").avg("rating")

   countMovie = movieDataSet.groupBy("movieID").count()

   avgAndCount = countMovie.join(averageRatings,"movieID")

   sortedMovies = avgAndCount.orderBy("avg(rating)")

   results = sortedMovies.take(20)

   for result in results:
      print (movieNames[result[0]], result[1], result[2])

   spark.stop()