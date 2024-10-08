from pymongo import MongoClient
from app.core.config import settings

# Conexión a MongoDB Atlas
client = MongoClient(settings.MONGODB_ATLAS_CLUSTER_URI)
MONGODB_COLLECTION = client[settings.DB_NAME][settings.COLLECTION_NAME]

try:
    print("Trying to ping your deployment...")
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
