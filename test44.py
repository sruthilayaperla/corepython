#single inheritance
import os
import subprocess
subprocess.run("cls",shell=True)
class parent:
    def feeamt(self,months,fee_per_month):
        return months*fee_per_month
    def payfees(self):
        print("payment will be given by parent")
class student(parent):
    def attendschool(self):
        print("student attends class")
S=student()
S.payfees()
S.attendschool()
print(f"Total amoount={S.feeamt(5,5000)}")
