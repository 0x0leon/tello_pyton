import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

import time

mpl.rcParams['legend.fontsize'] = 10

fig = plt.figure()
ax = fig.add_subplot(projection='3d')




xList = [1,2,3,3,5]
yList = [1,1,1,4,7]
zList = [1,1,1,4,10]

def addPoint(x,y,z):
    xList.append(x)
    yList.append(y)
    zList.append(z)

for i in range(0, 100, 1):
    addPoint(i, i, i)
    time.sleep(0.001)

    
    ax.clear()
    ax.plot(xList, yList, zList, label='flight path')
    
    ax.set_xlabel('X cm')
    ax.set_ylabel('Y cm')
    ax.set_zlabel('Z cm')

    ax.legend()
    ax.grid(True)
    plt.draw()
    plt.pause(0.001)
    



plt.show()