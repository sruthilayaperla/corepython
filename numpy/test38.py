#bincount() for frequency counting
import numpy as np
a=np.array([1,2,2,3,3,4,4])
print("frequency of each integer:")
print(np.bincount(a))