#advanced array creation
import numpy as np
a=np.fromiter((x*x for x in range (5)),dtype=int)
print("fromiter:",a)
a=np.fromfunction(lambda i,j:i+j,(3,3),dtype=int)
print("fromfunction:",a)
print(a)
x=np.array([1,2,3])
y=np.array([10,20,30])
print("x:")
print(x)
print("y:")
print(y)
