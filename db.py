# db.py
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Get values from environment
MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB = os.getenv("MONGO_DB", "emailLogsDB")
MONGO_COLLECTION = os.getenv("MONGO_COLLECTION", "logs")

client = MongoClient(MONGO_URI)
db = client[MONGO_DB]
logs_collection = db[MONGO_COLLECTION]
