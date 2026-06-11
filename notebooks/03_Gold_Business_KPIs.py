silver_df = spark.table("silver_transactions")

#display(silver_df)

from pyspark.sql.functions import *

gold_deposits = silver_df.filter(
    col("Transaction_Type") == "Deposit"
).groupBy(
    "Customer_Name"
).agg(
    sum("Amount").alias("Total_Deposits")
)

#display(gold_deposits)

#Save table
gold_deposits.write \
.format("delta") \
.mode("overwrite") \
.saveAsTable("gold_total_deposits")

#totla withdrawles by customer
gold_withdrawals = silver_df.filter(
    col("Transaction_Type") == "Withdrawal"
).groupBy(
    "Customer_Name"
).agg(
    sum("Amount").alias("Total_Withdrawals")
)

#display(gold_withdrawals)

#save
gold_withdrawals.write \
.format("delta") \
.mode("overwrite") \
.saveAsTable("gold_total_withdrawals")


#transaction summwer by account type
gold_account_type = silver_df.groupBy(
    "Account_Type"
).agg(
    sum("Amount").alias("Total_Amount"),
    count("Transaction_ID").alias("Transaction_Count")
)

display(gold_account_type)

#save
gold_account_type.write \
.format("delta") \
.mode("overwrite") \
.saveAsTable("gold_account_summary")

#Gold Table 4: Monthly Transaction Summary
from pyspark.sql.functions import month
gold_monthly = silver_df.groupBy(
    month("Transaction_Date").alias("Month")
).agg(
    sum("Amount").alias("Total_Amount")
)

#display(gold_monthly)
#save
gold_monthly.write \
.format("delta") \
.mode("overwrite") \
.saveAsTable("gold_monthly_summary")
