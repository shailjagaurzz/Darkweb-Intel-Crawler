from db import collection

# Insert a test document
collection.insert_one({"test": "connection_successful"})

# Print all documents
for doc in collection.find():
    print(doc)
