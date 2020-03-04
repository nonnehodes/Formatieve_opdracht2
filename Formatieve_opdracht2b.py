'''
Bron 1: https://pynative.com/python-postgresql-insert-update-delete-table-data-to-perform-crud-operations/#Python_PostgreSQL_INSERT_into_database_Table

'''

import pymongo
import psycopg2  # Module om met PostgreSQL te communiceren

client = pymongo.MongoClient("mongodb://localhost:27017/")
database = client["huwebshop"]


try:
    connection = psycopg2.connect("dbname=voordeelshop user=postgres password=ZET HIER JE WW NEER")   # Verbind met Postgres database
    cursor = connection.cursor()

    postgres_insert_query = """ INSERT INTO product VALUES(%s,%s,%s,%s)"""
    record_to_insert = ('123', 'Man', 'Shirt', '1')
    cursor.execute(postgres_insert_query, record_to_insert)

    connection.commit()
    count = cursor.rowcount
    print(count, "Record inserted successfully into mobile table")

except (Exception, psycopg2.Error) as error:
    if(connection):
        print("Failed to insert record into mobile table", error)

finally:
    #   closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")

