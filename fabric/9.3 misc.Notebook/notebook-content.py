# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {}
# META }

# CELL ********************

# Welcome to your new notebook
# Type here in the cell editor to add code!

%%tsql
-- Query that fails if any table is missing records in the last hour
DECLARE @ErrorMessage NVARCHAR(500);

WITH TableChecks AS (
    SELECT '[lh_edp_prod].[stream].[orderupdated_paymentstream]' AS TableName, COUNT(*) AS RecordCount
    FROM [lh_edp_prod].[stream].[orderupdated_paymentstream]
    WHERE updated_datetime >= DATEADD(HOUR, -1, GETUTCDATE())
    
    UNION ALL
    
    SELECT '[lh_edp_prod].[stream].[orderupdated_rowstream]', COUNT(*)
    FROM [lh_edp_prod].[stream].[orderupdated_rowstream]
    WHERE updated_datetime >= DATEADD(HOUR, -1, GETUTCDATE())
    
    UNION ALL
    
    SELECT '[lh_edp_prod].[stream].[orderupdated_orderstream]', COUNT(*)
    FROM [lh_edp_prod].[stream].[orderupdated_orderstream]
    WHERE updated_datetime >= DATEADD(HOUR, -1, GETUTCDATE())
)
SELECT 
    @ErrorMessage = 'VALIDATION FAILED: No records in last hour for tables: ' + 
                    STRING_AGG(TableName, ', ')
FROM TableChecks
WHERE RecordCount = 0;

-- Throw error if any tables failed
IF @ErrorMessage IS NOT NULL
BEGIN
    THROW 50001, @ErrorMessage, 1;
END
ELSE
BEGIN
    PRINT 'All validations passed successfully';
END

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# import duckdb
# from datetime import datetime, timedelta

# def alert_new_rows(tables):
#     one_hour_ago = datetime.now() - timedelta(hours=1)
#     failed_tables = []
    
#     for table_path in tables:
#         df = duckdb.sql(f"""
#             SELECT * FROM delta_scan('{table_path}')
#             WHERE updated_datetime >= TIMESTAMP '{one_hour_ago.strftime('%Y-%m-%d %H:%M:%S')}'
#         """).df()
        
#         if len(df) == 0:
#             failed_tables.append(table_path)
#             print(f"No new rows in {table_path}")
#         else:
#             print(f"{len(df)} new rows in {table_path}")
    
#     if failed_tables:
#         raise Exception(f"Failed tables: {', '.join(failed_tables)}")

# # Usage
# tables = [
#     '/lakehouse/default/Tables/stream/orderupdated_rowstream',
#     '/lakehouse/default/Tables/stream/orderupdated_paymentstream',
#     '/lakehouse/default/Tables/stream/orderupdated_orderstream',
# ]

# alert_new_rows(tables)


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
