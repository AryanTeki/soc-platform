from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['your_database_name']

# Ensure the users collection exists
if 'users' not in db.list_collection_names():
    db.create_collection('users')

# Add any additional database initialization logic here

def insert_user(username, hashed_password):
    db.users.insert_one({'username': username, 'password': hashed_password})


def find_user(username):
    return db.users.find_one({'username': username}) 