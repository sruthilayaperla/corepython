#Nan-safe statistical functions
import numpy as np
a=np.array([10.0,20.0,np.nan,40.0,np.nan])
print("nanmean:",np.nanmean(a))
print("nanmedian:",np.nanmedian(a))
print("nansum:",np.nansum(a))
print("nanmin:",np.nanmin(a))
print("nanmax:",np.nanmax(a))
print("nanstd:",np.nanstd(a))
