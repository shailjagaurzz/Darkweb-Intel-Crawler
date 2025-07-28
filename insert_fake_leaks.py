import json
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["darkweb_leaks"]
collection = db["leaked_emails"]

# Load fake leaks from JSON file
with open("fake_leaks.json", "r") as file:
    leaks = json.load(file)

# Clear previous leaks (optional)
collection.delete_many({})

# Insert leaks into MongoDB
collection.insert_many(leaks)

print("✅ Fake leaks inserted into MongoDB!")
