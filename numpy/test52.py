#Comparison:comparisons are element-wise. The result is usually a Boolean array
import numpy as np
a=np.array([1.0,2.0,3.0])
b=np.array([1.0,2.000001,3.0])
print("Equal:")
print(np.equal(a,b))
print("Approximately equal:")
print(np.isclose(a,b))
print("All approximately equal:")
print(np.allclose(a,b))