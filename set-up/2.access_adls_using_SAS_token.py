# Databricks notebook source
# MAGIC %md
# MAGIC #### Access Azure Data Lake using SAS Tokens
# MAGIC 1. Set the spark config SAS Token
# MAGIC 2. List files from demo container
# MAGIC 3. Read data from circuits.csv file

# COMMAND ----------

SAS_token = dbutils.secrets.get("formula1-sc", key='formula1dl-sas-demo')

# COMMAND ----------

spark.conf.set("fs.azure.account.auth.type.formula1dl069.dfs.core.windows.net", "SAS")
spark.conf.set("fs.azure.sas.token.provider.type.formula1dl069.dfs.core.windows.net", "org.apache.hadoop.fs.azurebfs.sas.FixedSASTokenProvider")
spark.conf.set("fs.azure.sas.fixed.token.formula1dl069.dfs.core.windows.net",
dbutils.secrets.get("formula1-sc", key='formula1dl-sas-demo'))

# COMMAND ----------

display(dbutils.fs.ls("abfss://demo@formula1dl069.dfs.core.windows.net"))

# COMMAND ----------

display(spark.read.csv("abfss://demo@formula1dl069.dfs.core.windows.net/circuits.csv"))

# COMMAND ----------


