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
numberX = 500
numberY = 500

# omega of wave
omega = 2*math.pi/5

# define class for particle
class Particle():
    def __init__(self):
        self.x = 0
        self.z = 0
        self.speed = 0
        self.colour = (0,0,255)
# display the particle
    def display(self):
        gfxdraw.pixel(screen, int(self.x), int(self.z), self.colour)

# create an array to hold the particles
fieldParticles = []
# set the step size
stepsize = 1
# now create the collection
for i in xrange(0,numberX,stepsize):
	particle = Particle()
	particle.x = i
	particle.z = 200
	particle.speed = 0
	fieldParticles.append(particle)
	particle.display()

z = []
for i in xrange(0,numberX,stepsize):
	z.append(200)

#sourcex = [0 for x in xrange(0,numberX)]
#sourcey = [0 for x in xrange(0,numberY)]

sourcex = int(0)
#sourcey[0] = int(0)

blue = (0,0,255)

# define global time
clockTick = 0
index = 1

# define x and y of the barrier
rect_x = 220

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
#	screen.fill(background_colour)
	z[0]= fieldParticles[0].z
	fieldParticles[0].z = 100*math.sin(clockTick*0.1) + 200
#	fieldParticles[0].x = clockTick
	if index > int(numberX/stepsize):
		index = 1

	for i in xrange(0,index+1):
		if i > 0:
			z[i] = fieldParticles[i].z
			restoreForceab = abs(z[i - 1] - z[i])
			restoreForcebc = abs(z[i + 1] - z[i])
			restoreForce = round(restoreForceab + restoreForcebc,2)
#			angle = math.atan2()
			if restoreForce > 200:
				restoreForce = 200
			if restoreForce < -200:
				restoreForce = -200			
			#print clockTick,i,fieldParticles[i-1].z,fieldParticles[i].z,fieldParticles[i+1].z,restoreForce
			
			fieldParticles[i].speed = fieldParticles[i].speed + restoreForce
			
			fieldParticles[i].z = z[i] + fieldParticles[i].speed
			fieldParticles[i].display()
			
			print clockTick,i,restoreForce

	fieldParticles[0].display()

# advance the clock
	clockTick += 1
	index += 1
	pygame.display.flip()
