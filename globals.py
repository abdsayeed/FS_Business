from pymongo import MongoClient

SECRET_KEY = "mysecret"

Client = MongoClient("mongodb://localhost:27017/")
db = Client.Business