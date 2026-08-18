#expand dims
import numpy as np
x=np.array([1,2,3])
print(x)
print("expand_dims:")
print(np.expand_dims(x,axis=0))
print(np.expand_dims(x,axis=1))