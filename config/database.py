from pymongo import MongoClient
from os import environ, path

# Determine the environment (GitHub Actions or Render.com)
is_github_actions = "GITHUB_ACTIONS" in environ
dotenv_path = "/etc/secrets/.env" if is_github_actions else ".env"

# Load environment variables from the appropriate .env file
if path.exists(dotenv_path):
    from dotenv import load_dotenv
    load_dotenv(dotenv_path=dotenv_path)

# Get the MongoDB connection details from environment variables
username = environ.get("DBUSER")
password = environ.get("DBPASS")
dbname = environ.get("DBNAME")
col_name = environ.get("COLNAME")

# Connect to MongoDB using the retrieved connection details
if username and password and dbname and col_name:
    client = MongoClient(f"mongodb+srv://{username}:{password}@cluster0.taxfc6l.mongodb.net/?retryWrites=true&w=majority")
    db = client[dbname]
    collection_name = db[col_name]
else:
    raise ValueError("MongoDB connection details not provided in environment variables.")
