#program to convert file content to uppercase
f=open("c:/pythoncode/myfiles/fruits.txt","r")
text=f.read()
print(text.upper())
f.close()