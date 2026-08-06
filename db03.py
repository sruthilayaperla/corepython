#program to create a table
import mysql.connector
try:
    x=mysql.connector.connect(host="localhost",user="root",passwd="brilliant",database="demobase")
    y=x.cursor()
    q="create table myemp(eno int,ename char(20),esal int,egrade char(3))"
    y.exceute(q)
    x.commit()
    print("Table created")
except:
    print("Table not created")
    