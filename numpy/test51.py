#singular value decompositioon(SVD): When a is a 2-D array and full_matrices= false, then it is factorized as u @np.daig(s) @vh,where u & the hermitian transpose of vh are 2d arrays with orthonoraml columns and s is a 1d array of a singular values
import numpy as np
A=np.array([[1,2],[3,4]])
result=np.linalg.svd(A)
print(result)