#program to read csv file
import csv
f=open("students.csv","r")
reader=csv.reader(f)
for row in reader:
    print(row)
f.close()