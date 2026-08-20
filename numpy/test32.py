#random distribution
import numpy as np
from numpy import random
x=np.random.choice([3,5,7,9],p=[0.1,0.3,0.6,0.0],size=[100])
print(x)