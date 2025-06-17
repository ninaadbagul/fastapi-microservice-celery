from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["fastapi_db"]  # This is the database
users_collection = db["users"]  # This is the collection (like a table)

# Insert a test document
result = users_collection.insert_one({
    "name": "John",
    "email": "john@example.com"
})

print("Inserted ID:", result.inserted_id)
