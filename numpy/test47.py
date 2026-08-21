#solve
import numpy as np
a=np.array([[4,7],[2,6]],dtype=float)
b=np.array([10,8],dtype=float)
print("Solutionof AX=b:")
print(np.linalg.solve(a,b))
