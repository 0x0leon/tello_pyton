
# install requirements
# > pip install --upgrade pip
# > pip install -r requirements.txt

from djitellopy import Tello
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

drone = Tello()

xList = []
yList = []
zList = []

'''
    graph operations
'''

def add_point(x, y, z) -> None:
    xList.append(x)
    yList.append(y)
    zList.append(z)

def update_coordinates() -> None:

    # get state with x,y,z
    state = drone.get_current_state()
    
    # get curent coordinates from Drone
    add_point(state['x'],state['y'],state['z'])


def plot_graph() -> None:

    ax.plot(xList, yList, zList, label='flight path')
    
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    ax.legend()
    ax.grid(True)
    plt.draw()
    plt.pause(0.001)

'''
    drone operations
'''

def main():
    print("test")

    running = True    
    
    while running:
        print("running")





    
if __name__ == "__main__":
    main()