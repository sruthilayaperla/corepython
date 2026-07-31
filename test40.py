#*args model -2:
import os
import subprocess
subprocess.run("cls",shell=True)
def mysum(*x):
    return sum(x)
print("sum=",mysum(1,2),sep="")
print("sum=",mysum(10,20),sep="")
print("sum=",mysum(10,20,25,30,11),sep="")

