#unique() with counts & inverse indexes
import numpy as np
a=np.array([10,20,10,30,20,20,40])
unique,counts=np.unique(a,return_counts=True)
print("Unique values:",unique)
print("Counts:",counts)
unique,inverse=np.unique(a,return_inverse=True)
print("Inverse indexes:",inverse)