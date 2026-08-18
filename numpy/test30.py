#argmin(),argmax(),nonzeros()
import numpy as np
a=np.array([45,12,78,239,56])
print("Index of minimum value:",np.argmin(a))
print("Index of maximum value:",np.argmax(a))
print("Maximum value:",a[np.argmax(a)])
print("Minimum value:",a[np.argmin(a)])
print("nonzero indexes:")
print(np.nonzero(a))
