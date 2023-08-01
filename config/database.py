from os import environ
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient

load_dotenv()

# Get the MongoDB connection details from environment variables
username = environ.get("USER")
password = environ.get("PASS")
database = environ.get("BASE")
collection = environ.get("COLLECTION")
host = environ.get("HOST")

# Connect to MongoDB using the retrieved connection details
client = AsyncIOMotorClient(f"mongodb+srv://{username}:{password}@{host}")
db = client[database]
bcards_collection = db[collection]
