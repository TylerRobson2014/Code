from __future__ import division
import pygame
import math
from decimal import Decimal
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
        self.density = 1
# display the particle
    def display(self):
#        gfxdraw.pixel(screen, int(self.x), int(self.z), self.colour)
		if self.density > 1:
			drawden = 3
		else:
			drawden = 1
		pygame.draw.circle(screen, self.colour, (int(self.x), int(self.z)), drawden)

# create an array to hold the particles
fieldParticles = []
old = []

# set the step size
stepsize = 1
# now create the collection
for i in xrange(0,numberX,stepsize):
	particle = Particle()
	particle.x = i
	particle.z = 200
	if i > 200:
		particle.density = 4
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
density = 1


fieldParticles[0].z = start

running = True
timer_event = pygame.USEREVENT + 1
pygame.time.set_timer(timer_event, 100)
screen.fill(background_colour)
while running:
	event = pygame.event.wait()
	screen.fill(background_colour)
# ********************	
	if clockTick < 5000:
		new = 100*math.sin(clockTick*0.1) + 200
	else :
		new = 200
		
	old[0] = fieldParticles[0].z
	fieldParticles[0].z = new
# ********************

	for i in xrange(1,int(numberX/stepsize)):
		
		if i > int(numberX/(stepsize*2)):
			fieldParticles[i].density = 5
		else:
			fieldParticles[i].density = 1
			
		density = fieldParticles[i].density

		if i < int(numberX/stepsize) - 1:
			T1 = old[i-1] - fieldParticles[i].z
			T2 = fieldParticles[i+1].z - fieldParticles[i].z

			T = T1 + T2
			new = 2*fieldParticles[i].z - old[i] + T * (dt*dt)/(factor3*density)
			
		else:
			T1 = old[i-1] - fieldParticles[i].z
			T2 = 200. - fieldParticles[i].z

			T = T1 + T2
			new = 2 * fieldParticles[i].z - old[i] + T * (dt*dt)/(factor3*density)		
			
	
			
		old[i] = fieldParticles[i].z
		fieldParticles[i].z = new
		#print fieldParticles[i].z
		fieldParticles[int(numberX/stepsize)-1].z = 200.
		
# ********************
#		if fieldParticles[0].z < 200.:
#			old[0] = fieldParticles[0].z
#			fieldParticles[0].z = fieldParticles[0].z + returnstep
# ********************

		fieldParticles[i].display()
		fieldParticles[0].display()
		
		
# advance the clock
	clockTick += dt
	pygame.display.flip()
