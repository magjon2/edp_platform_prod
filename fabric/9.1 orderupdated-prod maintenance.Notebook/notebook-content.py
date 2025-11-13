# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "408d8412-c973-46aa-8c0c-52dbe1c38ada",
# META       "default_lakehouse_name": "lh_edp_prod",
# META       "default_lakehouse_workspace_id": "fb736e26-5db5-424b-8125-6f2ab29a83f0",
# META       "known_lakehouses": [
# META         {
# META           "id": "408d8412-c973-46aa-8c0c-52dbe1c38ada"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC 
# MAGIC -- 5x new  columns to orderupdated_row
# MAGIC /*
# MAGIC ALTER TABLE orderupdated_row
# MAGIC ADD COLUMNS (
# MAGIC     orderDate TIMESTAMP,
# MAGIC     salesBrand STRING,
# MAGIC     customerNumber STRING,
# MAGIC     country STRING,
# MAGIC     currency STRING
# MAGIC )
# MAGIC ALTER TABLE orderupdated_row
# MAGIC ADD COLUMNS (
# MAGIC     source_isExternal BOOLEAN,
# MAGIC     deliveryStatus_value STRING,
# MAGIC     fraudStatus_value STRING
# MAGIC )
# MAGIC */
# MAGIC 
# MAGIC ALTER TABLE orderupdated_row
# MAGIC ADD COLUMNS (
# MAGIC     source_name STRING
# MAGIC )
# MAGIC 


# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Validate
df = spark.sql("SELECT * FROM lh_edp_prod.dbo.orderupdated_row order by source_name desc LIMIT 1000")
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************


df = spark.sql("SELECT * FROM lh_edp_prod.stream.orderupdated_raw LIMIT 1000")
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC DESCRIBE DETAIL lh_edp_prod.stream.orderupdated_raw


# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }
