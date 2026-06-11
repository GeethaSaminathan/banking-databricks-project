customers_df = spark.table("bronze_customers")

accounts_df = spark.table("bronze_accounts")

transactions_df = spark.table("bronze_transactions")

#print("Customers:", customers_df.count())
#print("Accounts:", accounts_df.count())
#print("Transactions:", transactions_df.count())


customers_clean = customers_df.dropDuplicates()

accounts_clean = accounts_df.dropDuplicates()

transactions_clean = transactions_df.dropDuplicates()


from pyspark.sql.functions import *

transactions_clean = transactions_clean.withColumn(
    "Transaction_Date",
    to_date(col("Transaction_Date"), "yyyy-MM-dd")
)

#Join Customers and Accounts:
customer_account = customers_clean.join(
    accounts_clean,
    "Customer_ID",
    "inner"
)

display(customer_account)

#Join transaction and Customers and Accounts:
silver_transactions = transactions_clean \
    .join(accounts_clean, "Account_ID") \
    .join(customers_clean, "Customer_ID")


#display(silver_transactions)

customer_account.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("silver_customer_account")

silver_transactions.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("silver_transactions")
