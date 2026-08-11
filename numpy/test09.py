#complex
import numpy as np
a=np.array([-5.6j,0.2j,11.5j,1+1j])
print(a)
print(np.real(a))
print(np.imag(a))
print(np.conj(a))
print(np.angle(a))
print(np.angle(a,deg=True))
