from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("RetailSalesETL").getOrCreate()

# Load CSV from local or ADLS path
raw_df = spark.read.option("header", "true").csv("/mnt/data/mock_retail_sales.csv")

raw_df.show()