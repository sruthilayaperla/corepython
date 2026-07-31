#multilevel inheritance
import os
import subprocess
subprocess.run("cls",shell=True)
class parent:
    def feeamt(self,i,p):
        return i*p
    def payfees(self):
        print("payment will be given by parent")
class student(parent):
    def attendschool(self):
        print("student can use quipment to play")
class play(student):
    def psports(student):
        print("student plays sports")
S=student()
S.payfees()
S.attendschool()
print(f"Total amoount={S.feeamt(5,5000)}")
print("---------------------------------------------")
P=play()
P.payfees()
P.attendschool()
print(f"Total amoount={S.feeamt(5,5000)}")
P.psports
