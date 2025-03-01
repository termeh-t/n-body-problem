import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

import tkinter as tk
from tkinter import simpledialog

G = 6.6743e-11

time_step = 1


class Mass():
    def __init__(self, position, mass, initial_velocity):
        self.position = np.array(position, dtype=float)
        self.mass = mass
        self.velocity = np.array(initial_velocity, dtype=float)

    def calculate_magnitude_vector(self):
        return np.linalg.norm(self.position)
    
    def calculate_magnitude_acceleration(self, other_mass):
        radius_vector = other_mass.position - self.position
        radius = np.linalg.norm(radius_vector)
        return G * other_mass.mass / (radius ** 3) * radius_vector
    
    def calculate_position(self, acceleration, time_step):

        followingvelocity = acceleration * time_step + self.velocity

        following_position = followingvelocity * time_step + self.position

        self.velocity = followingvelocity
        self.position = following_position

    def size(self):

        return np.log10(self.mass)

def get_input():
    root = tk.Tk()
    root.withdraw() 

    mass1 = simpledialog.askfloat("Input", "Enter the mass for object 1:")
    mass2 = simpledialog.askfloat("Input", "Enter the mass for object 2:")
    velocity1_x = simpledialog.askfloat("Input", "Enter the initial velocity (x) for object 1:")
    velocity1_y = simpledialog.askfloat("Input", "Enter the initial velocity (y) for object 1:")
    velocity1_z = simpledialog.askfloat("Input", "Enter the initial velocity (z) for object 1:")
    velocity2_x = simpledialog.askfloat("Input", "Enter the initial velocity (x) for object 2:")
    velocity2_y = simpledialog.askfloat("Input", "Enter the initial velocity (y) for object 2:")
    velocity2_z = simpledialog.askfloat("Input", "Enter the initial velocity (z) for object 2:")

    return (mass1, mass2, [velocity1_x, velocity1_y, velocity1_z], [velocity2_x, velocity2_y, velocity2_z])

mass1, mass2, initial_velocity1, initial_velocity2 = get_input()

m1 = Mass([0.0, 0.0, 0.0], mass1, initial_velocity1)
m2 = Mass([10.0, 10.0, 10.0], mass2, initial_velocity2)

# m1 = Mass([-10.0, -10.0, 0.0], 5e10, [0.0, 0.0, 0.0])
# m2 = Mass([-30.0, -30.0, -10.0], 15e10, [0.5, 0.0, 0.0])

list_position_m1 = []
list_position_m2 = []

def calculate_coordinates(m1, m2):
    for _ in range(2000):
        acceleration_m1 = m1.calculate_magnitude_acceleration(m2)
        acceleration_m2 = m2.calculate_magnitude_acceleration(m1)

        m1.calculate_position(acceleration_m1, time_step)
        m2.calculate_position(acceleration_m2, time_step)

        list_position_m1.append(m1.position.copy())
        list_position_m2.append(m2.position.copy())

calculate_coordinates(m1, m2)

list_position_m1 = np.array(list_position_m1)
list_position_m2 = np.array(list_position_m2)

fig = plt.figure(figsize=(12,8))
ax = fig.add_subplot(111, projection='3d')

ax.set_xlim3d([-30.0, 30.0])
ax.set_ylim3d([-30.0, 30.0])
ax.set_zlim3d([-30.0, 30.0])

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

point_m1, = ax.plot([], [], [], 'bo', markersize=m1.size())
point_m2, = ax.plot([], [], [], 'ro', markersize=m2.size())

trace_m1, = ax.plot([], [], [], 'b-', linewidth=1)
trace_m2, = ax.plot([], [], [], 'r-', linewidth=1)

def update(frame):
    
    x1, y1, z1 = list_position_m1[frame]
    x2, y2, z2 = list_position_m2[frame]

    point_m1.set_data([x1], [y1])
    point_m1.set_3d_properties([z1])

    point_m2.set_data([x2], [y2])
    point_m2.set_3d_properties([z2])

    trace_m1.set_data(list_position_m1[:frame+1, 0], list_position_m1[:frame+1, 1])
    trace_m1.set_3d_properties(list_position_m1[:frame+1, 2])

    trace_m2.set_data(list_position_m2[:frame+1, 0], list_position_m2[:frame+1, 1])
    trace_m2.set_3d_properties(list_position_m2[:frame+1, 2])

    return point_m1, point_m2, trace_m1, trace_m2

ani = FuncAnimation(fig, update, frames=len(list_position_m1), interval=50, blit=False)

plt.show()
