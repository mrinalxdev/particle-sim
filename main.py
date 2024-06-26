import math
import random
import numpy as np
import pygame


class Particle:
    def __init__(self, position, velocity, mass):
        self.position = position
        self.velocity = velocity
        self.mass = mass

    def update(self, force, time_interval):
        acceleration = force / self.mass
        self.velocity += acceleration * time_interval
        self.position += self.velocity * time_interval

        # Checking if the particle has crossed the boundary

        if self.position[0] < 0 or self.position[0] > window_size[0]:
            self.velocity = (-self.velocity[0], self.velocity[0])
        

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

def draw_particles(particles, surface):
    for particle in particles:
        x, y = particle.position
        pygame.draw.circle(surface, (255, 255, 255), (int(x), int(y)), 5)


if __name__ == "__main__":

    pygame.init()
    window_size = (800, 600)
    window = pygame.display.set_mode(window_size)
    window_center = (window_size[0] // 2, window_size[1] // 2)
   
    max_velocity = 25
    offset = 50
    particles = []

    for i in range(100):
        velocity = (random.uniform(-max_velocity, max_velocity), random.uniform(-max_velocity, max_velocity))
        position = (window_center[0] + random.uniform(-offset, offset), window_center[1] + random.uniform(-offset, offset))
        particles.append(Particle(position, velocity, 1))

    frame_rate = 60
    frame_time = 1.0/frame_rate

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    simulate(particles, frame_time)
    window.fill((0, 0, 0))
    draw_particles(particles, window)
    pygame.display.flip()
    pygame.time.delay(int(frame_rate * 1000))

    pygame.quit()

