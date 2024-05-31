import numpy as np

import matplotlib

G = 6.6743e-11

class Mass():
    
    def __init__ (self, x, y, z, mass, intialVelocityX, intialVelocityY, initialVelocityZ):
            
        self.x = x
        self.y = y
        self.z = z
        self.mass = mass
        self.velocityX = intialVelocityX
        self.velocityY = intialVelocityY
        self.velocityZ = initialVelocityZ

    def calculate_Magnitute_Vector(self):
        
        a = (self.x**2 + self.y**2 + self.z**2)**(1/2)

        return (self.x**2 + self.y**2 + self.z**2)**(1/2)
    
    def calculate_Magnitute_Acceleration(self):

        a = calculate_Gravitaional_Law()/self.mass 

        return calculate_Gravitaional_Law()/self.mass 
    
    def calculate_position(self):

        print(self.x, self.y, self.z)


m1 = Mass(0.0, 0.0, 0.0, 10e10, 0.0, 0.0, 0.0)
m2 = Mass(10.0, 10.0, 10.0, 20e10, 0.0, 0.0, 0.0)

def calculate_Magnitute_radius():

    return Mass.calculate_Magnitute_Vector(m1) - Mass.calculate_Magnitute_Vector(m2) 


def calculate_Gravitaional_Law():

    a = G*m1.mass*m2.mass/calculate_Magnitute_radius()

    return G*m1.mass*m2.mass/calculate_Magnitute_radius()



def calculate_coordinate(m : Mass):    
        
    timediff = 0.1

    for i in np.arange(0, 1000, 0.1):

        accleration = float(Mass.calculate_Magnitute_Acceleration(m))

        followingVelocityX = accleration * timediff + m.velocityX 
        followingVelocityY = (accleration * timediff) + (m.velocityY)
        followingVelocityZ = (accleration * timediff) + (m.velocityZ) 

        diffposX = (followingVelocityX**2 - float(m.velocityX**2))/(2*accleration)
        diffposY = (followingVelocityY**2 - float(m.velocityY**2))/(2*accleration)
        diffposZ = (followingVelocityZ**2 - float(m.velocityZ**2))/(2*accleration)

        m.x = m.x + diffposX
        m.y = m.y + diffposY
        m.z = m.z + diffposZ

        m.velocityX = followingVelocityX
        m.velocityY = followingVelocityY
        m.velocityZ = followingVelocityZ

        print(f" at time {i} {Mass.calculate_position(m)} ")




calculate_coordinate(m1)
calculate_coordinate(m2)