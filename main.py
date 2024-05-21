import math
import numpy as np


class Particle:
    def __init__(self, position, velocity, mass):
        self.position = position
        self.velocity = velocity
        self.mass = mass

    def update(self, force, time_interval):
        acceleration = force / self.mass
        self.velocity += acceleration * time_interval
        self.position += self.velocity * time_interval

def simulate(particles, time_interval):
    for particle in particles:
        total_forces = calculate_total_force(particle, particles)
        particle.update(total_forces, time_interval)

def calculate_total_force(particle, particles):
    total_force = np.array([0.0, 0.0])
    for other in particles:
        if other == particle:
            continue
        distance = math.sqrt((particle.position[0] - other.position[0])**2 + (particle.position[1] - other.position[1])**2)
        force = calculate_force(particle, other, distance)
        total_force += force
    return total_force

def calculate_force(particle1, particle2, distance):
    G = 6.674e-11 #gravitational constant
    force = G * particle1.mass * particle2.mass / distance**2
    force_x = force * (particle2.position[0] - particle1.position[0]) / distance
    force_y = force * (particle2.position[1] - particle1.position[1]) / distance
    return np.array([force_x, force_y])

if __name__ == "__main__":
    particles = [Particle((0, 0), (1, 0), 1), Particle((5,0), (-1, 0), 1)]
    for i in range(1000):
        simulate(particles, 0.1)
