#weights
import numpy as np
a=np.array([5,6,7])
print(a)
print("-------------------")
wt=np.array([8,2,3])
print(np.average(a,weights=wt))
