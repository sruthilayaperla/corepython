#overriding
import os
import subprocess
subprocess.run("cls",shell=True)
class RBI:
    def irate(self):
        print("RBI decides the base interest rate")
class HDFC(RBI):
    def irate(self):
        print("HDFC provides 7% interest rate")
H=HDFC()
H.irate()
