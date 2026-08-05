#program to check file exists
import os
path="c:/pythoncode/myfiles/fruits.txt"
if os.path.exists(path):
    print("File exists")
else:
    print("File not found")
