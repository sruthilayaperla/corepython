#Norm: The forbenius norm is a way of measuring the size or magnitude of a matrix. It is similar to the funclidean norm for vectors
import numpy as np
A=np.array([[1,2],[3,4]])
result=np.linalg.norm(A,'fro')
print(result)