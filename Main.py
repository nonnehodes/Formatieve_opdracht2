import pymongo
client = pymongo.MongoClient("mongodb://localhost:27017/")
webshop_databases = client['huwebshop']
products_database = webshop_databases['products']
sessions_database = webshop_databases['sessions']
profiles_database = webshop_databases['profiles']
#   Opdracht 1
print(' Opdracht 1:')
producten = products_database.find({},{'name':1, 'price':1})
print('Naam v/h eerste product in de DB: {}'.format(producten[0]['name']))
print('Prijs v/h eerste product in de DB: {}'.format(producten[0]['price']['selling_price']))

#   Opdracht 2
print('\n Opdracht 2:')
producten_2 = products_database.find({ "name": { "$gt": "R" } }, {'name':1})
print('Naam v/h eerste product met een r: {}'.format(producten_2[0]['name']))


#   Opdracht 3

'''
Bron 1: https://www.w3schools.com/python/python_mongodb_find.asp

'''