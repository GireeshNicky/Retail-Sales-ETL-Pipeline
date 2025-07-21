# Save as Delta table (overwrite for testing)
df.write.format("delta").mode("overwrite").save("/mnt/datalake/retail_sales_delta/")