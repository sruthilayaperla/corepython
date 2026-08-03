#operator overloading
import os
import subprocess
subprocess.run("cls",shell=True)
class point:
    def __init__(self,x):
        self.x=x
    def __add__(self,other):
        return self.x+other.x
p1=point(10+3j)
p2=point(7+3j)
p3=p1+p2
print("sum=",p3)

