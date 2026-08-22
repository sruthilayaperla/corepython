#line graph model 2
import numpy as np
import matplotlib.pyplot as plt
x=np.arange(1,11)
y=2*x+5
plt.title("Line plot")
plt.xlabel("x-axis caption")
plt.ylabel("y-axis caption")
plt.plot(x, y,"g")
plt.show()