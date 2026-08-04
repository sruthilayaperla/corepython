#program to convert file content to lowercase
f=open("c:/pythoncode/myfiles/fruits.txt","r")
text=f.read()
print(text.lower())
f.close()