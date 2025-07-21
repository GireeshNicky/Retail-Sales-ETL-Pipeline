# Daily Sales KPI
daily_sales = df.groupBy("InvoiceDate").agg({"TotalPrice": "sum"}).withColumnRenamed("sum(TotalPrice)", "DailyRevenue")

# Top 5 Products
top_products = df.groupBy("ProductName").agg({"TotalPrice": "sum"}) \
                 .orderBy(col("sum(TotalPrice)").desc()).limit(5)

# Store Performance
store_perf = df.groupBy("StoreLocation").agg({"TotalPrice": "sum"}).orderBy("sum(TotalPrice)", ascending=False)

daily_sales.show()
top_products.show()
store_perf.show()