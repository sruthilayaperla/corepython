# program to insert records
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
    q = "INSERT INTO myemp (eno, ename, esal, egrade) VALUES (%s, %s, %s, %s)"
    records = [
        (101, "Balu", 4000, "A"),
        (102, "Sarath", 5000, "B"),
    ]
    y.executemany(q, records)
    x.commit()
    print("Records inserted")
except mysql.connector.Error as error:
    print(f"Insert failed: {error}")
