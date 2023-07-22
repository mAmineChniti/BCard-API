from pymongo import MongoClient
import os
from dotenv import load_dotenv
from pathlib import Path

# Check if environment variables are present (for GitHub Actions)
username = os.environ.get("DBUSER")
password = os.environ.get("DBPASS")
dbname = os.environ.get("DBNAME")
col_name = os.environ.get("COLNAME")

# If environment variables are not present, load them from .env file (for Render)
if not (username and password and dbname and col_name):
    dotenv_path = Path('.env')
    load_dotenv(dotenv_path=dotenv_path)

    username = os.environ.get("DBUSER")
    password = os.environ.get("DBPASS")
    dbname = os.environ.get("DBNAME")
    col_name = os.environ.get("COLNAME")

# Check if all required variables are set
if not (username and password and dbname and col_name):
    raise ValueError("Missing required environment variables or .env file.")

# Now, proceed with the rest of your code as before
client = MongoClient(f"mongodb+srv://{username}:{password}@cluster0.taxfc6l.mongodb.net/?retryWrites=true&w=majority")
db = client[dbname]
collection_name = db[col_name]
