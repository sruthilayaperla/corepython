#super in python
#calling a parent constructor
import os
import subprocess
subprocess.run("cls",shell=True)
class parent:
    def __init__(self, name):
        self.name = name
        print("Parent constructor")
class child(parent):
    def __init__(self, name, age):
        super().__init__(name)   # Calls parent class constructor
        self.age = age
        print("Child constructor")
c = child("John", 20)
print("Name:", c.name)
print("Age:", c.age)
