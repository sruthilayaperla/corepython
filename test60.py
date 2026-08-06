#program to create a csv file
import csv
f=open("students.csv","w",newline="")
f.write("Name,Age,Grade\n")
f.write("John,20,A\n")
f.write("Madhu,21,B\n")
w=csv.writer(f)
f.close()