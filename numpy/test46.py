#determinant & Inverse
import numpy as np
a=np.array([2,3,4,5])
print(a)
print("determinant of the array:",np.linalg.det(a.reshape(2,2)))
print("------------------------------")
print("inverse of the array:",np.linalg.inv(a.reshape(2,2)))