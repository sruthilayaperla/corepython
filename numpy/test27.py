#Adding & removing Dimensions
import numpy as np
a=np.array([10,20,30])
b=a[np.newaxis,:]
c=a[:,np.newaxis]
print(a)
print("Row vector:")
print(b)
print("column vector")
print(c)