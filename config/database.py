from pymongo import MongoClient
from os import environ
from dotenv import load_dotenv

load_dotenv('/etc/secrets/.env')

# Get the MongoDB connection details from environment variables
username = environ.get("DBUSER")
password = environ.get("DBPASS")
dbname = environ.get("DBNAME")
col_name = environ.get("COLNAME")

# Connect to MongoDB using the retrieved connection details
client = MongoClient(f"mongodb+srv://{username}:{password}@cluster0.taxfc6l.mongodb.net/?retryWrites=true&w=majority")
db = client[dbname]
collection_name = db[col_name]
