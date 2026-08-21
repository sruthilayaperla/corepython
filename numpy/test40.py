#covarinace and correlation
import numpy as np
x=np.array([1,2,3,4,5])
y=np.array([2,4,5,8,10])
print("covariance matrix:")
print(np.cov(x,y))
print("correlation matrix:")
print(np.corrcoef(x,y))