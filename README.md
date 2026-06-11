# banking-databricks-project
End-to-end Banking Data Engineering project using Databricks Medallion Architecture
CSV Files (Source Data)
        ↓
🥉 Bronze Layer (Raw Data Ingestion)
        ↓
🥈 Silver Layer (Cleaned + Transformed + Joined Data)
        ↓
🥇 Gold Layer (Business KPIs & Aggregated Tables)
        ↓
Dashboards & Reporting

Technologies Used
Databricks Community Edition
Apache Spark (PySpark)
SQL
Delta Lake
Python
Medallion Architecture
📂 Dataset Description
1. Customers
Customer_ID
Customer_Name
City
State
2. Accounts
Account_ID
Customer_ID
Account_Type
3. Transactions
Transaction_ID
Account_ID
Transaction_Date
Transaction_Type (Deposit / Withdrawal)
Amount
🥉 Bronze Layer (Raw Data Ingestion)
Loaded raw CSV files into Databricks
Stored as Delta Tables without transformations

Tables Created:

bronze_customers
bronze_accounts
bronze_transactions
🥈 Silver Layer (Data Cleaning & Transformation)

Performed data cleaning and transformations:

Transformations:
Removed duplicates
Handled null values
Converted date formats
Joined datasets:
Customers + Accounts
Accounts + Transactions + Customers

Tables Created:

silver_customer_account
silver_transactions
🥇 Gold Layer (Business KPIs)

Created aggregated tables for reporting:

KPI Tables:
Total Deposits by Customer
Total Withdrawals by Customer
Account Type Transaction Summary
Monthly Transaction Summary

Tables Created:

gold_total_deposits
gold_total_withdrawals
gold_account_summary
gold_monthly_summary
📊 Key Business Insights
Identify top customers by deposits
Analyze withdrawal behavior
Understand account type usage
Monthly transaction trends
🚀 How to Run the Project
Create Databricks Community Edition workspace
Upload CSV files to /FileStore/tables/
Run notebooks in sequence:
01_Bronze_Load
02_Silver_Processing
03_Gold_KPIs
Query tables using SQL or Spark
📸 Screenshots (Add Here)
Bronze tables output
Silver joined data
Gold KPI tables
Databricks workflow
📈 Skills Demonstrated
Data ingestion using PySpark
Data transformation & cleaning
SQL-based analytics
Delta Lake usage
Medallion Architecture design
ETL pipeline development
🎯 Future Enhancements
Add data quality checks (null validation, schema enforcement)
Implement incremental loading
Build Databricks dashboard
Add fraud detection rules
Automate pipeline using Databricks Jobs
👩‍💻 Author

Geetha Saminathan
Data Analyst | Aspiring Data Engineer
Located in North Carolina, USA
