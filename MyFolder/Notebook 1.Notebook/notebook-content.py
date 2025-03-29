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

# PARAMETERS CELL ********************

param1 = "default value for param1"
param2 = 1
param3 = True

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df = spark.read.format("csv").option("header","true").load("Files/movies.csv")
# df now is a Spark DataFrame containing CSV data from "Files/movies.csv".
df.createOrReplaceTempView("df_view")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC SELECT * FROM df_view LIMIT 10

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************


# Get information about a Lakehouse in the current workspace, maximum number of Notebooks to return default is 1000
notebookutils.fs.mkdirs("Files/new-folder")



# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

#list all contents of a folder
notebookutils.fs.ls("Files/new-folder")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

#remove contents of a folder
notebookutils.fs.rm("Files/new-folder",True)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Note: NotebookUtils is only supported on runtime v1.2 and above. If you are using runtime v1.1, please use mssparkutils instead.
# Mount a lakehouse/gen2/blob/fileshare storage with AAD token credential
storage_url = 'abfss://mycontainer@<accountname>.dfs.core.windows.net' # replace with your storage url
mount_point = '/your/mnt' # replace with your mount point name, it should start with /
# If you already have the access to the storage account, then just use:
notebookutils.fs.mount(storage_url, mount_point)
# Use account key as credential to access the storage follow below method
# Ussparkutils.fs.mount(storage_url, mount_point, {"accountKey": "<your account key>"})
# Use sas token as credential  to access the storage follow below method
# notebookutils.fs.mount(storage_url, mount_point, {"sasToken": "<your sas token>"})

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
