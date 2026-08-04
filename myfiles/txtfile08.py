#program to copy one file to another file
source=open("c:/pythoncode/myfiles/fruit.txt","r")
destination=open("c:/pythoncode/myfiles/fruits_copy.txt","w")
source.close()
destination.close()
print("file copied suceessfully")