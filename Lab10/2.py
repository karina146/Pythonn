import matplotlib.pyplot as plt
import numpy as np

k = [[(3,2), (3,4)], [(5,4), (5,6)]]
tt = np.arange(0,2*np.pi,0.005)
fig,ax = plt.subplots(2,2)
for i in k:
    for j in i:
        a,b = j
        x = [np.sin(a*t + np.pi/2)  for t in tt]
        y = [np.sin(b*t)  for t in tt]
        ax[k.index(i),i.index(j)].plot(x,y)

plt.show()
# print(k.index([(3,2), (3,4)]), [(3,2), (3,4)].index((3,2)))