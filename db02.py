#program to create a database
import mysql.connector
try:
    x=mysql.connector.connect(host="localhost",user="root",passwd="brilliant")
    y=x.cursor()
    q="create database demobase"
    y.execute(q)
    x.commit()
    print("databse created")
except:
    print("error")
