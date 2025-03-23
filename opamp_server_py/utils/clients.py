import os
from pymongo import MongoClient

mongo_client = MongoClient(os.environ.get('MONGO_URI'))
mongo_database = mongo_client[os.environ.get('DB_NAME','opamp')]
mongo_agents_collection = mongo_database['agents']