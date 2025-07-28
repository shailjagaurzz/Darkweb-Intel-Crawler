import json
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["leak_detection"]
collection = db["leaks"]

# Load fake leaks from JSON
with open("fake_leaks.json") as f:
    data = json.load(f)

# Insert into MongoDB
collection.delete_many({})  # Clear previous data
collection.insert_many(data)

print("✅ Fake leaks inserted into MongoDB!")
