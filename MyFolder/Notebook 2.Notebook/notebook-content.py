# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "519d5508-80a3-4316-b6bc-7dc88e7c5b03",
# META       "default_lakehouse_name": "KKTestLaksHouse",
# META       "default_lakehouse_workspace_id": "799d5789-66bd-43b0-bb27-8e80b6c4cef5"
# META     }
# META   }
# META }

# CELL ********************

# Welcome to your new notebook
# Type here in the cell editor to add code!


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df = spark.read.format("csv").option("header","true").load("Files/userdata.csv")
# df now is a Spark DataFrame containing CSV data from "Files/userdata.csv".
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
