from __future__ import division
import pygame
import math
from decimal import Decimal
from pygame import gfxdraw
from bigfloat import *

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
#        gfxdraw.pixel(screen, int(self.x), int(self.z), self.colour)
		pygame.draw.circle(screen, self.colour, (int(self.x), int(self.z)), 2)

# create an array to hold the particles
fieldParticles = []
old = []

# set the step size
stepsize = 2
# now create the collection
for i in xrange(0,numberX,stepsize):
	particle = Particle()
	particle.x = i
	particle.z = 200
	fieldParticles.append(particle)
	particle.display()
	old.append(200)

blue = (0,0,255)

# define global time
clockTick = 0
dt = 1
index = 0
factor1 = 1.999
factor2 = 0.999
factor3 = 5
start = 0.
returnstep = 0.05

fieldParticles[0].z = start

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
	screen.fill(background_colour)
# ********************	
#	if clockTick < 500:
#		new = 50*math.sin(clockTick*0.05) + 200
#	else :
#		new = 200
#		
#	old[0] = fieldParticles[0].z
#	fieldParticles[0].z = new
# ********************

	for i in xrange(1,int(numberX/stepsize)):

		if i < int(numberX/stepsize) - 1:
			T1 = old[i-1] - fieldParticles[i].z
			T2 = fieldParticles[i+1].z - fieldParticles[i].z
			T = T1 + T2
			new = factor1 * fieldParticles[i].z - factor2*old[i] + T * (dt**2)/factor3
			
		else:
			T1 = old[i-1] - fieldParticles[i].z
			T2 = 200. - fieldParticles[i].z
			T = T1 + T2
			new = factor1 * fieldParticles[i].z - factor2*old[i] + T * (dt**2)/factor3		
			
			
		old[i] = fieldParticles[i].z
		fieldParticles[i].z = new
		#print fieldParticles[i].z
		fieldParticles[int(numberX/stepsize)-1].z = 200.
		
# ********************
		if fieldParticles[0].z < 200.:
			old[0] = fieldParticles[0].z
			fieldParticles[0].z = fieldParticles[0].z + returnstep
# ********************

		fieldParticles[i].display()
		fieldParticles[0].display()
		
		
# advance the clock
	clockTick += dt
	pygame.display.flip()
