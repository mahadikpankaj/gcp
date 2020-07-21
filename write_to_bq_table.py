from pyspark.sql.types import StructField, StructType, IntegerType
from pyspark.sql import SparkSession
from py4j.protocol import Py4JJavaError
spark = SparkSession.builder.appName("Pankaj").getOrCreate()

fields = [StructField("report_month", IntegerType(), True),
          StructField("rec_count", IntegerType(), True)]
schema = StructType(fields)

results_count = spark.createDataFrame([], schema)

months = ['202008', '202009', '202010']
table = 'report_analysis.projected_results'
for month in months:
    new_record = spark.createDataFrame([month, 100], schema)
    results_count.union(new_record)

spark.write.format('bigquery').option('table', table).save())

df = spark.read.format('bigquery').option('table', table).load()

print("Results: " )
df.show()

