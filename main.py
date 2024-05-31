import numpy as np

G = 6.6743e-11

class Mass():
    
    def __init__ (self, position, mass, initialVelocity):
        self.position = np.array(position, dtype=float)
        self.mass = mass
        self.velocity = np.array(initialVelocity, dtype=float)

    def calculate_magnitude_vector(self):
        return np.linalg.norm(self.position)
    
    def calculate_magnitude_acceleration(self, other_mass):
        radius_vector = other_mass.position - self.position
        radius = np.linalg.norm(radius_vector)
        return G * other_mass.mass / (radius ** 3) * radius_vector
    
    def calculate_position(self, acceleration, time_step):
        self.position += self.velocity * time_step + 0.5 * acceleration * (time_step ** 2)
        self.velocity += acceleration * time_step


m1 = Mass([0.0, 0.0, 0.0], 10e10, [0.0, 0.0, 0.0])
m2 = Mass([10.0, 10.0, 10.0], 20e10, [0.0, 0.0, 0.0])

def calculate_coordinates(m1, m2):
    time_step = 0.1
    for _ in range(2000):
        
        acceleration_m1 = m1.calculate_magnitude_acceleration(m2)
        acceleration_m2 = m2.calculate_magnitude_acceleration(m1)

        m1.calculate_position(acceleration_m1, time_step)
        m2.calculate_position(acceleration_m2, time_step)

        print(f"At time {_ * time_step}:")
        print("m1 position:", m1.position)
        print("m2 position:", m2.position)


calculate_coordinates(m1, m2)
