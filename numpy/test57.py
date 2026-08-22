#program to produce a sine wave
import numpy as np
import matplotlib.pyplot as plt
x=np.arange(1,3*np.pi,0.1)
print(x)
y=np.sin(x)
plt.title("Sine wave")
plt.plot(x,y)
plt.show()