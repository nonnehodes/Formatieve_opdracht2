'''
Bron 1: https://pynative.com/python-postgresql-insert-update-delete-table-data-to-perform-crud-operations/#Python_PostgreSQL_INSERT_into_database_Table

'''

import pymongo
import psycopg2  # Module om met PostgreSQL te communiceren




def get_products_mongo():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    database = client["huwebshop"]

    colom_product = database["products"]

    products = colom_product.find({"gender": "Unisex"}).limit(20)
    for i in products:
        insert_into_postgres((i["_id"], i["gender"], i["name"], i["price"]["selling_price"]))





def insert_into_postgres(values):
    try:
        connection = psycopg2.connect("dbname=voordeelshop user=postgres password=WACHTWOORD")
        cursor = connection.cursor()

        postgres_insert_query = """ INSERT INTO product VALUES(%s,%s,%s,%s)"""
        record_to_insert = values
        cursor.execute(postgres_insert_query, record_to_insert)

        connection.commit()
        count = cursor.rowcount
        print(count, "Record inserted successfully into mobile table")

    except (Exception, psycopg2.Error) as error:
        if(connection):
            print("Failed to insert record into mobile table", error)


get_products_mongo()

