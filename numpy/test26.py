#dimensions manipulations(swapaxes and moveaxes)
import numpy as np
a = np.arange(24).reshape(2, 3, 4)
print("Original shape:", a.shape)
print("swapaxes shape:", np.swapaxes(a, 0, 2).shape)
print("moveaxis shape:", np.moveaxis(a, 0, -1).shape)