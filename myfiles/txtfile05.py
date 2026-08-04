#program to count lines
f=open("c:/pythoncode/myfiles/fruits.txt","r")
count=0
for line in f:
    count+=1
    print("Total lines=",count)
f.close()