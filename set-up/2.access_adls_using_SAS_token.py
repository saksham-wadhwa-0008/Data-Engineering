# Databricks notebook source
# MAGIC %md
# MAGIC #### Access Azure Data Lake using SAS Tokens
# MAGIC 1. Set the spark config SAS Token
# MAGIC 2. List files from demo container
# MAGIC 3. Read data from circuits.csv file

# COMMAND ----------

spark.conf.set("fs.azure.account.auth.type.formula1dl069.dfs.core.windows.net", "SAS")
spark.conf.set("fs.azure.sas.token.provider.type.formula1dl069.dfs.core.windows.net", "org.apache.hadoop.fs.azurebfs.sas.FixedSASTokenProvider")
spark.conf.set("fs.azure.sas.fixed.token.formula1dl069.dfs.core.windows.net","sp=rl&st=2024-10-19T13:10:23Z&se=2024-10-19T14:10:23Z&spr=https&sv=2022-11-02&sr=c&sig=bjDhDhQnc%2BdAlH5gCsBmrZWRaX3gTg3%2B1%2B2lYbPrDtQ%3D")

# COMMAND ----------

display(dbutils.fs.ls("abfss://demo@formula1dl069.dfs.core.windows.net"))

# COMMAND ----------

display(spark.read.csv("abfss://demo@formula1dl069.dfs.core.windows.net/circuits.csv"))

# COMMAND ----------


