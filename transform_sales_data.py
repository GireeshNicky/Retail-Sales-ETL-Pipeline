from pyspark.sql.functions import col, to_date, expr

df = raw_df.withColumn("Quantity", col("Quantity").cast("int")) \
           .withColumn("UnitPrice", col("UnitPrice").cast("double")) \
           .withColumn("TotalPrice", col("Quantity") * col("UnitPrice")) \
           .withColumn("InvoiceDate", to_date("InvoiceDate", "yyyy-MM-dd")) \
           .dropna()

df.createOrReplaceTempView("sales_transformed")
df.show()