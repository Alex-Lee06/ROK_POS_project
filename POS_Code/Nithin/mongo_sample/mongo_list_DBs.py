import certifi
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# Modify username and password before executing the script
uri = "mongodb+srv://nithinvasireddy:<DB_password>@cluster0.iqkc1.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, tlsCAFile=certifi.where())

for db_name in client.list_database_names():
        print(db_name)
