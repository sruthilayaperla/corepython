# program to create a database
import os
import mysql.connector

try:
    x = mysql.connector.connect(
        host=os.getenv("MYSQL_HOST", "localhost"),
        user=os.getenv("MYSQL_USER", "root"),
        password=os.getenv("MYSQL_PASSWORD"),
    )
    y = x.cursor()
    y.execute("CREATE DATABASE demobase")
    x.commit()
    print("Database created")
except mysql.connector.Error as error:
    print(f"Database creation failed: {error}")
