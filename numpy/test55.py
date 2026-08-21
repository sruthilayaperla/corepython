# data visualizing using numbers:
#line plot: A graph that displays data points connected by lines, commonly used to show trends.
import numpy as np
import matplotlib import pyplot as plt
x=np.arange(1,11)
y=2*x+5
plt.plot(x,y)
plt.title("lineplot")
plt.xlabel("x-axis caption")
plt.ylabel("y-axis caption")
plt.plot(x,y)
plt.show()
