#lexsort()
import numpy as np
first_names=np.array(["Bob","Alice","Cathy"])
last_names=np.array(["Marley","Daves","Watson"])
sorted_indices=np.lexsort([first_names])
sorted_indices
print("----------------------------------------")
sorted_indices=np.lexsort([first_names,last_names])
for i in sorted_indices:
    print(first_names[i]+" "+last_names[i])
    


                      