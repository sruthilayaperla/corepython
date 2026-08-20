#Binomial Distribution
#Given 10 trails for a coin toss generate 10 data points 
import numpy as np
from numpy import random
x=random.binomial(n=10, p=0.5, size=10)
print(x)