#program to count words
f=open("c:/pythoncode/myfiles/fruits.txt","r")
text=f.read()
words=text.split()
print("total words=",len(words))
f.close()
