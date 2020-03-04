'''
Bron 1: https://pynative.com/python-postgresql-insert-update-delete-table-data-to-perform-crud-operations/#Python_PostgreSQL_INSERT_into_database_Table

LET OP
Het wachtwoord van je PostgreSQL moet je zelf invullen, anders werkt het niet
Zoek naar de plekken waar je een wachtwoord in moet vullen met ctrl+f password
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
        connection = psycopg2.connect("dbname=voordeelshop user=postgres password=")
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


#get_products_mongo()


def opdracht_2():
    try:
        connection = psycopg2.connect("dbname=voordeelshop user=postgres password=")
        cursor = connection.cursor()

        cursor = connection.cursor()
        postgreSQL_select_Query = "select Price from Product"

        cursor.execute(postgreSQL_select_Query)
        price_records = cursor.fetchall()

        total = 0
        b = 0
        for row in price_records:
            total += row[0]
            b += 1
        print(total/b)


    except (Exception, psycopg2.Error) as error:
        if (connection):
            print("Failed to insert record into mobile table", error)


opdracht_2()