from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

#Connect to Mongo Atlas Clutter 
mongo_client = MongoClient(os.getenv("MONGO_URI"))

# Access database
event_manager_db = mongo_client["event_manager_db"]

# Pick a collection to operate on
events_collection = event_manager_db["events"]