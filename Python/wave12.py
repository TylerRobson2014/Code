from __future__ import division
import pygame
import math
from pygame import gfxdraw


background_colour = (255,255,255)
(width, height) = (500, 500)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Wave')
screen.fill(background_colour)

# now define field as collection of particles
# first define number of particles
numberX = 400
numberY = 50

# omega of wave
omega = 2*math.pi/5

# define class for particle
class Particle():
    def __init__(self):
        self.x = 0
        self.z = 0
        self.colour = (0,0,255)
# display the particle
    def display(self):
        gfxdraw.pixel(screen, int(self.x), int(self.z), self.colour)
#		pygame.draw.circle(screen, self.colour, (int(self.x), int(self.z)), 2)

# create an array to hold the particles
fieldParticles = []
# set the step size
stepsize = 1
# now create the collection
for i in xrange(0,numberX):
	particle = Particle()
	particle.x = i
	particle.z = 200
	fieldParticles.append(particle)
	particle.display()

sourcex = int(0)
#sourcey[0] = int(0)

blue = (0,0,255)

# define global time
clockTick = 0
i = 1

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
	screen.fill(background_colour)

	fieldParticles[0].z = 100*math.sin(clockTick*0.05) + 200

	for i in xrange(1,numberX):
		
		if i < numberX - 1:
			deltaZ = fieldParticles[i + 1].z + fieldParticles[i - 1].z - 2 * fieldParticles[i].z
		else:
			deltaZ = 200 + fieldParticles[i - 1].z - 2 * fieldParticles[i].z

		fieldParticles[i].z = fieldParticles[i].z + deltaZ
			
		fieldParticles[i].display()

# advance the clock
	clockTick += 1
	pygame.display.flip()
