#abstraction
from abc import ABC
class Bank(ABC):
    def irate(self):
        pass
class HDFC(Bank):
    def irate(self):
        print("interest rate is 7%")
class ICICI(Bank):
    def irate(self):
        print("Interest rate is 6.5")
H=HDFC()
I=ICICI()
H.irate()
I.irate()

