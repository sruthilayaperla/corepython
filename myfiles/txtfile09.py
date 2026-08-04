#program to search a word
f=open("c:/pythoncode/myfiles/fruits.txt","r")
text=f.read()
word=input("enter word to search:")
if word in text:
    print(word,"found")
else:
    print(word,"notfound")
f.close()