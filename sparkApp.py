from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("MySparkApp").getOrCreate()

data = spark.read.csv("/data.csv", header=True, inferSchema=True)
data.csv

result = data.groupBy("name ").agg({"score": "sum"})

result.show()

spark.stop()