'''
Bron 1: https://www.w3schools.com/python/python_mongodb_find.asp

'''

import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
database = client["huwebshop"]
colom = database["products"]


#   Opdracht 2
myquery = { "name": { "$gt": "R" } }
mydoc = colom.find(myquery)

