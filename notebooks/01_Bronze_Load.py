customers_df = spark.read.csv(
"file:/Workspace/Users/geethuashok7@gmail.com/customers.csv",
header=True,
inferSchema=True
)

display(customers_df)


accounts_df = spark.read.csv(
"file:/Workspace/Users/geethuashok7@gmail.com/accounts.csv",
header=True,
inferSchema=True
)

display(accounts_df)


transactions_df = spark.read.csv(
"file:/Workspace/Users/geethuashok7@gmail.com/transactions.csv",
header=True,
inferSchema=True
)

display(transactions_df)


customers_df.write.format("delta").mode("overwrite").saveAsTable("bronze_customers")

accounts_df.write.format("delta").mode("overwrite").saveAsTable("bronze_accounts")

transactions_df.write.format("delta").mode("overwrite").saveAsTable("bronze_transactions")
