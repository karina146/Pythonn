import matplotlib.pyplot as plt
import numpy as np
from scipy.special import legendre

x = np.arange(-1,1,0.005)

for n in range(1,8):
    Pn = legendre(n)
    y = Pn(x)
    plt.plot(x,y)


plt.title('Legendre polynomial')
plt.legend(range(1,8),bbox_to_anchor=(1,0.6))

plt.show()