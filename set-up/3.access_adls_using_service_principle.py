# Databricks notebook source
# MAGIC %md
# MAGIC #### Access Azure Data Lake using Service Principle
# MAGIC 1. Register Azure AD Applicationn/Service Principal
# MAGIC 2. Generate a secret/password for the Application
# MAGIC 3. Set Spark Config with App/Client Id, Directry/Tenat Id & Secret
# MAGIC 4. Assign Role 'Storage Blob Data Contributor' to the Data Lake.

# COMMAND ----------

client_id = ""
tenant_id = ""
client_seceret = ""

# COMMAND ----------

spark.conf.set(
    "fs.azure.account.auth.type.formula1dl069.dfs.core.windows.net", 
    "OAuth"
)
spark.conf.set(
    "fs.azure.account.oauth.provider.type.formula1dl069.dfs.core.windows.net", 
    "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider"
)
spark.conf.set(
    "fs.azure.account.oauth2.client.id.formula1dl069.dfs.core.windows.net", 
    client_id
)
spark.conf.set(
    "fs.azure.account.oauth2.client.secret.formula1dl069.dfs.core.windows.net", 
     client_seceret
)
spark.conf.set(
    "fs.azure.account.oauth2.client.endpoint.formula1dl069.dfs.core.windows.net", 
    f"https://login.microsoftonline.com/{tenant_id}/oauth2/token"
)

# COMMAND ----------

display(dbutils.fs.ls("abfss://demo@formula1dl069.dfs.core.windows.net"))

# COMMAND ----------

display(spark.read.csv("abfss://demo@formula1dl069.dfs.core.windows.net/circuits.csv"))

# COMMAND ----------


