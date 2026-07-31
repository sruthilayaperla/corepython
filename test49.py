#multipath inheritance
import os
import subprocess
subprocess.run("cls",shell=True)
class parent:
    def sendtoschool(self):
        print("parent send child to school")
class student(parent):
    def study(self):
        print("the child has to study")
class teacher(parent):
    def teaching(self):
        print("Teacher teaches in the class room")
class principal(student,teacher):
    def maintainschool(self):
        print("principal maintains school")
P=principal()
P.sendtoschool()
P.study()
P.teaching()
P.maintainschool()