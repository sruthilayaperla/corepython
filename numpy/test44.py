#joining array
import numpy as np
a=np.array([1,2,3])
b=np.array([4,5,6])
print("concatenate:")
print(np.concatenate((a,b)))
print("stack:")
print(np.stack((a,b)))
print("vstack:")
print(np.vstack((a,b)))
print("hstack:")
print(np.hstack((a,b)))