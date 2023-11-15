
# install requirements
# > pip install --upgrade pip
# > pip install -r requirements.txt

import cv2
import numpy as np
from djitellopy import Tello
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

xList = []
yList = []
zList = []

drone = Tello()
drone.connect()
drone.stream_on()

cv2.namedWindow("Tello Television")

follow_color_lower = np.array([30, 100, 100])
follow_color_upper = np.array([60, 255, 255])

# Set the desired distance for "follow me" (in pixels)
follow_distance = 50

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


    while True:
        
        # get frame from drone camera
        frame = drone.get_frame_read().frame

        # get hsv
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        f_mask = cv2.inRange(hsv, follow_color_lower, follow_color_upper)
        
        cntrs, _ = cv2.findContours(f_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if cntrs:

            largest_contoure = max(cntrs, key=cv2.contourArea)

            Matrix  = cv2.moments(largest_contoure)
            cx = int(Matrix["m10"] / Matrix["m00"])
            cy = int(Matrix["m01"] / Matrix["m00"])

            cv2.circle(frame, (cx, cy), 5, (0, 255, 0), -1)

            drone_to_center = np.sqrt((cx - frame.shape[1] // 2)**2 + (cy - frame.shape[0] // 2)**2)

            if drone_to_center > follow_distance:
                drone.send_rc_control(0, 0, 30, 0)
            else: 
                drone.send_rc_control(0, 0, 0, 0)

        cv2.imshow("Tello Television Stream", frame)

        key = cv2.waitKey(1) & 0xFF
        if key == 27:
            break
    drone.streamoff()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()