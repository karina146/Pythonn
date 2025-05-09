import matplotlib.pyplot as plt
import numpy as np

k = [[(3,2), (3,4)], [(5,4), (5,6)]]
colors = [['green', 'pink'], ['purple', 'red']]
tt = np.arange(0,2*np.pi,0.005)
fig,ax = plt.subplots(2,2)
plt.subplots_adjust(hspace=0.3)

for i in 0,1:
    for j in 0,1:
        a,b = k[i][j]
        x = [np.sin(a*t + np.pi/2)  for t in tt]
        y = [np.sin(b*t)  for t in tt]
        ax[i,j].plot(x,y,color=colors[i][j])


ax[0,0].set_title('(3,2)')
ax[0,1].set_title('(3,4)')
ax[1,0].set_title('(5,4)')
ax[1,1].set_title('(5,6)')


plt.show()