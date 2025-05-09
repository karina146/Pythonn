import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

fig = plt.figure()
frames = 100
b = 1
ax = plt.axes(xlim=(-1,1), ylim=(-1,1))
line, = ax.plot([],[], lw=3)
t = np.arange(0,2*np.pi,0.01)
# t = np.linspace(0, 2 * np.pi)

def init():
    line.set_data([],[])
    return line,

def animate(i):
    a = i/frames
    x = np.sin(a*t)
    y = np.sin(b*t)
    line.set_data(x,y)
    return line,

anim = FuncAnimation(fig, animate, init_func=init, frames=200, interval=20, blit=True)

plt.show()