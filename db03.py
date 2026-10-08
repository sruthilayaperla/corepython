# program to create a table
import os
import mysql.connector

try:
    x = mysql.connector.connect(
        host=os.getenv("MYSQL_HOST", "localhost"),
        user=os.getenv("MYSQL_USER", "root"),
        password=os.getenv("MYSQL_PASSWORD"),
        database="demobase",
    )
    y = x.cursor()
    y.execute("CREATE TABLE myemp (eno INT, ename CHAR(20), esal INT, egrade CHAR(3))")
    x.commit()
    print("Table created")
except mysql.connector.Error as error:
    print(f"Table creation failed: {error}")
