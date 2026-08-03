# program without exception handling
import os
import subprocess
subprocess.run("cls",shell=True)
a=100;b=0
print("Begin")
print("Ready to do division")
c=a/b                     # exception will raise here
print("result=",c)
print("division completed")
print("end")
