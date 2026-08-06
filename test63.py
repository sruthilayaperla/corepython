#program to read json file
import json
x=open("students.json","r")
y=json.load(x)
print(y)