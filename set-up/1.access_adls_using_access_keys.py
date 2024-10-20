# Databricks notebook source
# MAGIC %md
# MAGIC #### Access Azure Data Lake using Keys
# MAGIC 1. Set the spark config fs.azure.account.key
# MAGIC 2. List files from demo container
# MAGIC 3. Read data from circuits.csv file

# COMMAND ----------

account_key = dbutils.secrets.get("formula1-sc", key='storage-account-access-key')

# COMMAND ----------

spark.conf.set(
    "fs.azure.account.key.formula1dl069.dfs.core.windows.net",
    account_key)

# COMMAND ----------

display(dbutils.fs.ls("abfss://demo@formula1dl069.dfs.core.windows.net"))

# COMMAND ----------

display(spark.read.csv("abfss://demo@formula1dl069.dfs.core.windows.net/circuits.csv"))

# COMMAND ----------


