#program to create a json file
import json
empdet=open("students.json","w")
x={'sno':101,'sname':"Anil",'scourse':"pdgca"}
json.dump(x,empdet)
empdet.close()