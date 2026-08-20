#generate a random normal distribution 2*3 with mean at 1 & standard deviation at 2
import numpy as np
from numpy import random
x=random.normal(loc=1, scale=2, size=(2,3))
print(x)
