#Multiple inheritance
import os
import subprocess
subprocess.run("cls",shell=True)
class parent:
    def sendtoschool(self):
        print("parent send child to school")
class teacher:
    def teaching(self):
        print("Teacher teaches in the class room")
class student(parent,teacher):
    def study(self):
        print("the child has to study")
S=student()
S.sendtoschool()
S.study()
S.teaching()