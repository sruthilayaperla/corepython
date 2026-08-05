#program to replace a word
f=open("c:/pythoncode/myfiles/fruits.txt","r")
text=f.read()
text=text.replace("Apple","Orange")
f.close()
f=open("c:/pythoncode/myfiles/fruits.txt","w")
f.write(text)
f.close()
