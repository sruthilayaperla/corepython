#program to check the connection
import mysql.connector
x=mysql.connector.connect(host="localhost",user="root",passwd="brilliant")
print(x)