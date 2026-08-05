#program to store user input in a file
name=input("Enter your name:")
f = open("c:/pythoncode/myfiles/fruits.txt", "w")
f.write(name)
f.close()
print("Saved successfully")