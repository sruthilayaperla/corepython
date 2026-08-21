#eigen values: An eigen values is a scalar tell us how much a particular vector is stretched, compressed or reversed when a matrix transformation is applied.
import numpy as np
A=np.array([[2,1],[1,2]])
eigenvalues,eigenvectors=np.linalg.eig(A)
print("Eigen values:")
print(eigenvalues)
print("Eigen vectors:")
print(eigenvectors)