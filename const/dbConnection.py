import os
from pymongo import MongoClient

class DbConnection:
    client = MongoClient(os.environ.get('MONGODB-CONNECTION-STRING'))
    db = client.PostPostmanDB
