# *Args 
#args: Abitary number of arguments
import os
import subprocess
subprocess.run("cls",shell=True)
def mysum(*x):
    print("sum=",sum(x))
mysum(1,2) 
mysum(10,20,30)
mysum(15,20,25,11,30)
