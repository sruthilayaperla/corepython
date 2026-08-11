#percentile
import numpy as np
data=np.array([1,2,3,4,5,6])
percentiles=np.percentiles(data,[25])
print(percentiles)