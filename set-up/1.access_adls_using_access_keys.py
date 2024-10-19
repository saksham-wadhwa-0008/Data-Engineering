# Databricks notebook source
# MAGIC %md
# MAGIC #### Access Azure Data Lake using Keys
# MAGIC 1. Set the spark config fs.azure.account.key
# MAGIC 2. List files from demo container
# MAGIC 3. Read data from circuits.csv file

# COMMAND ----------

spark.conf.set(
    "fs.azure.account.key.formula1dl069.dfs.core.windows.net",
    "your storage access key will go here"
)

# COMMAND ----------

display(dbutils.fs.ls("abfss://demo@formula1dl069.dfs.core.windows.net"))

# COMMAND ----------

display(spark.read.csv("abfss://demo@formula1dl069.dfs.core.windows.net/circuits.csv"))

# COMMAND ----------


