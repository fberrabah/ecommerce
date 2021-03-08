import os
import sqlite3
import csv





class Database:
    def __init__(self):
        self._conn = sqlite3.connect("shop.db")  #CONNECTION à la base de donnée
        self._cursor = self._conn.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    @property
    def connection(self):
        return self._conn

    @property
    def cursor(self):
        return self._cursor

    def commit(self):
        self.connection.commit()

    def close(self, commit=True):
        if commit:
            self.commit()
        self.connection.close()

    def execute(self, sql, params=None):
        self.cursor.execute(sql, params or ())

    def last_id(self):
        return self.cursor.lastrowid()

    def fetchall(self):
        return self.cursor.fetchall()

    def fetchone(self):
        return self.cursor.fetchone()

    def query(self, sql, params=None):
        self.cursor.execute(sql, params or ())
        return self.fetchall()

    def queryOne(self, sql, params=None):
        self.cursor.execute(sql, params or ())
        return self.fetchone()



files = {
    "olist_geolocation_dataset.csv": "geolocation",
    "olist_customers_dataset.csv": "customers",
    "olist_products_dataset.csv" : "products",
    "olist_orders_dataset.csv" : "orders",
    "olist_order_payments_dataset.csv" : "order_payments",
    "olist_order_items_dataset.csv" : "order_items",
    "olist_order_reviews_dataset.csv" : "order_reviews",
    "olist_sellers_dataset.csv" : "sellers",
    "product_category_name_translation.csv" : "category_name_translation",
}



with Database() as db:
    for file, table_name in files.items():
        with open(f'data/{file}', 'r') as data_file:
            reader = csv.reader(data_file)
            for i, row in enumerate(reader):
                if i == 0:
                    fields = row
                else:
                    if table_name == "category_name_translation":
                        fields = ["product_category_name", "product_category_name_english"] #incorrect sur la db
                    query = f"INSERT INTO {table_name} ({','.join(fields)}) VALUES ({','.join(['?']*len(row))})"
                    db.execute(query, row)

                    #CREATTION DE LA BASE DE DONNÉE 
