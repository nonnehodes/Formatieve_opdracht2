'''
Bron 1: https://www.w3schools.com/python/python_mongodb_find.asp

'''

import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
database = client["huwebshop"]



#   Opdracht 1
def opdracht_1():
    colom_product = database["products"]

    results = colom_product.find()
    for result in results:
        print(result["name"], (result["price"])['selling_price'])
        break



#   Opdracht 2
def opdracht_2():
    colom_product = database["products"]

    myquery = {'name':{"$regex": "^R" }}
    results= colom_product.find(myquery)
    for result in results:
        print(result['name'])
        break

def opdracht_3():#  Deze functie duurt even
    colom_product = database["products"]
    results = colom_product.find()

    total = 0
    loop = 0

    for result in results:
        try:
            total += ((result["price"])["selling_price"])
        except:
            continue
        else:
            loop +=1

    print(total/loop)

opdracht_3()