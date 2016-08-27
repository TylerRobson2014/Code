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
z = []
for i in xrange(numberX):
	z.append([])
	for j in xrange(2):
		z[i].append(200)

# set the step size
stepsize = 1
# now create the collection
for i in xrange(0,numberX):
	particle = Particle()
	particle.x = i
	particle.z = 200
	fieldParticles.append(particle)
	particle.display()

blue = (0,0,255)

# speed
speed = 0.005

# define global time
clockTick = 0
index = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
	screen.fill(background_colour)
	
	if clockTick < 10000000:
		fieldParticles[0].z = round(100*math.sin(clockTick*0.01) + 200,4)
	else :
		fieldParticles[0].z = 200

	z[0].append(fieldParticles[0].z)
	z[0].pop(0)

	for i in xrange(1,numberX):

		oldPos = z[i][0]
		
		if i < numberX - 1:
			fieldParticles[i].z = round(2 * fieldParticles[i].z,4) - round(oldPos,4) + speed * (round(fieldParticles[i + 1].z,4) + round(fieldParticles[i-1].z,4) - 2*round(fieldParticles[i].z,4))
		else:
			fieldParticles[i].z = round(2 * fieldParticles[i].z,4) - round(oldPos,4) + speed * (200                              + round(fieldParticles[i-1].z,4) - 2*round(fieldParticles[i].z,4))

		z[i].append(fieldParticles[i].z)
		z[i].pop(0)
		
	for j in xrange(0,numberX):
		fieldParticles[j].display()
		
# advance the clock
	clockTick += 1
	pygame.display.flip()
