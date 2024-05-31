import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

G = 6.6743e-11

time_step = 0.1


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
        # self.position += self.velocity * time_step + 0.5 * acceleration * (time_step ** 2)
        # self.velocity += acceleration * time_step
        followingvelocity = acceleration * time_step + self.velocity

        following_position = followingvelocity * time_step + self.position

        self.velocity = followingvelocity
        self.position = following_position


m1 = Mass([0.0, 0.0, 0.0], 19e10, [0.0, 0.0, 0.0])
m2 = Mass([10.0, 10.0, 10.0], 20e10, [1.0, 0.0, 0.0])

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

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.set_xlim3d([-30.0, 30.0])
ax.set_ylim3d([-30.0, 30.0])
ax.set_zlim3d([-30.0, 30.0])

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

point_m1, = ax.plot([], [], [], 'bo', markersize=2)
point_m2, = ax.plot([], [], [], 'ro', markersize=2)

def update(frame):
    x1, y1, z1 = list_position_m1[frame]
    x2, y2, z2 = list_position_m2[frame]

    point_m1.set_data([x1], [y1])
    point_m1.set_3d_properties([z1])

    point_m2.set_data([x2], [y2])
    point_m2.set_3d_properties([z2])

    return point_m1, point_m2,

ani = FuncAnimation(fig, update, frames=len(list_position_m1), interval=50, blit=False)

plt.show()
