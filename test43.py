#**kwargs
import os
import subprocess
subprocess.run("cls",shell=True)
def empdet(**x):
    for key,value in x.items():
        print(f'{key}:{value}',end="")
    print()
empdet(eno=101,ename="Anil")
empdet(eno=102,ename="Madhu",esal=4500)
