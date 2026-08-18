#program to find the dimension
import numpy as np
a=np.array([1,2,3,4,5,6])
b=np.array([[1,2,3],[4,5,6]])
c=np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
print(a.ndim)
print(b.ndim)
print(c.ndim)