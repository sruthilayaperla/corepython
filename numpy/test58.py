#Bargraph:A graph that represents values using rectangular bars
import numpy as np
import matplotlib.pyplot as plt
x=[5,8,10]
y=[12,16,6]
plt.bar(x,y,align='center',color="green")
plt.title('Bar graph')
plt.ylabel('Y-axis')
plt.xlabel('X-axis')
plt.show()