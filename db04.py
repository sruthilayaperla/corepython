#program to insert records
import mysql.connector
try:
 x=mysql.connector.connect(host="localhost",user="root",passwd="brilliant",db="demobase")
 y=x.cursor()
 q="insert into myemp(eno, ename, esal, egrade) values(101,'Balu',4000,'a),(102,'Sarath',5000,'b)"
 y.execute(q)
 x.commit()
 print("Inserted record")
except:
    print("not inserted")