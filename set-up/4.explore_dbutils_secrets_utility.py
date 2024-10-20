# Databricks notebook source
# MAGIC %md
# MAGIC ## Explore the capabilities of the dbutils.secerets utility

# COMMAND ----------

dbutils.secrets.help()

# COMMAND ----------

dbutils.secrets.listScopes()

# COMMAND ----------

dbutils.secrets.list("formula1-sc")

# COMMAND ----------

dbutils.secrets.get("formula1-sc", key='storage-account-access-key')

# COMMAND ----------

dbutils.secrets.get("formula1-sc", key='formula1dl-demo-sas')

# COMMAND ----------


