import os
import subprocess
subprocess.run("cls",shell=True)
def mysum(*x):
    s=0
    for i in x:
        s=s+i
        print("sum=",s,sep="")
mysum(10,20)
mysum(1,2,3)
