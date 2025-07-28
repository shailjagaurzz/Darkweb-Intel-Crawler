from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Load env variables
load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")

# Connect to MongoDB
client = MongoClient(MONGO_URI)
db = client["darkweb_leaks"]
collection = db["leaks"]

def check_email_leak(email):
    leak = collection.find_one({"email": email})
    if leak:
        print(f"🚨 Leak Found for: {email}")
        print(f"🔍 Source: {leak['leak_source']}")
        print(f"📄 Details: {leak['details']}")
    else:
        print(f"✅ No leak found for: {email}")

if __name__ == "__main__":
    user_email = input("🔐 Enter your email to check for leaks: ").strip()
    check_email_leak(user_email)
