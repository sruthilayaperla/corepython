#incorrect probability distribution
import numpy as np
num_list=[10,20,30,40,50]
numbers_list=np.array(np.random.choice(num_list,3,p=[0,0,0,1,0]))
print(numbers_list)

