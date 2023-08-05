from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os
from dotenv import load_dotenv

load_dotenv()
uri = os.getenv("MONGO_URI")
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client['rose']
users=db.get_collection('users')

def ins(id):
    r=users.find_one({"user_id":int(id)},max_time_ms=500)
    if not r:
        users.insert_one({"user_id":int(id)})

def get_count():
    return users.count_documents(filter={})
