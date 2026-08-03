#program with exception handling
import os
import subprocess
subprocess.run("cls",shell=True)
a=100;b=0
try:
    print("begin")
    print("ready to do to divison")
    c=a/b
    print("result=",c)
    print("division completed")
    print("end")
except:
    print("you cannot divide a number with zero")
    

