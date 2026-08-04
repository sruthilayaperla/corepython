#program to count characters
f=open("c:/pythoncode/myfiles/fruits.txt","r")
text=f.read()
print("characters=",len(text))
f.close()