from pymongo.mongo_client import MongoClient
import pandas as pd
import json

# uniform resource indentifier
uri = "mongodb+srv://abid55570:test1234@cluster-wafer.qnalkgy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster-wafer"

# Create a new client and connect to the server
client = MongoClient(uri)

# create database name & collection name 
DATABASE_NAME = "abid55570"
COLLECTION_NAME = "wafers_database"

# read the data as a dataframe
df=pd.read_csv(r"C:\Users\abida\OneDrive\Desktop\Sensor Project\notebooks\wafer.csv")
df=df.drop("Unnamed: 0",axis=1)

# Convert the data into json
json_record=list(json.loads(df.T.to_json()).values())

#now dump the data into the database
client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)