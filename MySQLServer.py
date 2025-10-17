#!/usr/bin/python3

import mysql.connector


mydb = None
try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="toorroot",
        database="alx_book_store"
    )
except Exception as e:
    print(f"Failed to Connect to DB: {e}")

if mydb:
    cursor = mydb.cursor()

    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

    print("Database 'alx_book_store' created successfully!")

    mydb.close()
