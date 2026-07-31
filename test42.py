import os
import subprocess
subprocess.run("cls",shell=True)
def mysum(*x):
    s=0
    for i in x:
        s=s+i
        return s
print("sum=",mysum(10,20),sep="")
print("sum=",mysum(1,2,3),sep="")
