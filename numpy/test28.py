#Conditional selection:(Where,Select,Clip)
import numpy as np
a=np.array([10,25,40,55,70])
print("where:")
print(np.where(a>=40,"pass","fail"))
conditions=[a,30,a>=30]
choices=["Low","High"]
print("select:")
print(np.select(conditions,choices,default="unknown"))
print("clip:")
print(np.clip(a,20,50))
