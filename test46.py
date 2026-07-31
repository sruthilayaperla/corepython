#heirarchial inheritance
import os
import subprocess
subprocess.run("cls",shell=True)
class parent:
    def payfees(self):
        print("parent pays the schools fees")

class teacher:
    def teach(self):
        print("Teacher teaches the student")
class student(parent,teacher):
    def response(self):
        print("student is responsible to parent and also teacher")
S=student()
S.payfees()
S.response()
S.teach()