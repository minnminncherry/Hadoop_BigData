from unittest import result
from pyspark import SparkConf, SparkContext

def loadMovieNames():
   movieNames = {}
   with open("../u.item",encoding = "ISO-8859-1") as f:
      for line in f:
         fields = line.split('|')
         movieNames[int(fields[0])] = fields[1]
   return movieNames

def parseInput(line):
   fields = line.split()
   return (int(fields[1]), (float(fields[2]), 1.0))

if __name__ == '__main__':
   conf = SparkConf().setAppName("WorstMovies")
   sc = SparkContext(conf = conf)

   movieNames = loadMovieNames()

   lines = sc.textFile("../u.data")
   movieRatings = lines.map(parseInput)

   ratingTotalsAndCount = movieRatings.reduceByKey(lambda movie1, movie2 : (movie1[0] + movie2[0], movie1[1] + movie2[1]))

   averageRatings = ratingTotalsAndCount.mapValues(lambda totalAndCount : totalAndCount[0] / totalAndCount[1])

   sortedMovies = averageRatings.sortBy(lambda x : x[1])

   results = sortedMovies.take(20)

   for result in results:
      print (movieNames[result[0]], result[1])