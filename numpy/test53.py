#random Generator API & reproducibility:NumPy provides a modern Random Generator API through np.random.default_rng(). It is the recommended way to generate random numbers in Python.
import numpy as np
rng=np.random.default_rng(42)
print(rng.integers(1,10,size=5))
#random normal values
rng=np.random.default_rng()
print(rng.normal(loc=0,scale=1,size=5))
#same seed produces reproducible results
rng1=np.random.default_rng(100)
print(rng1.normal(0,1,10).astype(int))
print(rng1.normal(0,1,10))
