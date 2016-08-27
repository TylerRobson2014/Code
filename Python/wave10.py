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
        self.y = 0
        self.phase = 0
        self.colour = (255, 255, 255)
        self.angularSpeed = omega
        self.waveF = [0 for i in xrange(0,500)]
# display the particle
    def display(self):
        gfxdraw.pixel(screen, int(self.x), int(self.y), self.colour)

# create an array to hold the particles
fieldParticles = []
# set the step size
stepsize = 2
# now create the collection
for i in xrange(0,numberY,stepsize):
	for j in xrange(0,numberX,stepsize):
		phase = 0
		particle = Particle()
		particle.x = j
		particle.y = i
		fieldParticles.append(particle)
		particle.display()

sourcex = [0 for x in xrange(0,numberX)]
sourcey = [0 for x in xrange(0,numberY)]

sourcex[0] = int(220)
sourcey[0] = int(0)
sourcex[1] = int(270)
sourcey[1] = int(0)

blue = (0,0,255)

# define global time

clockTick = 0

# define speed of the wave
speed = 2

# define x and y of the barrier

rect_x = 220
rect_y = 100
rect_w = 50
rect_h = 5

maxr = 2
n = 2

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
	screen.fill(background_colour)
	pygame.draw.rect(screen, blue,(rect_x,rect_y,rect_w,rect_h),2)

	recty = xrange(rect_y,rect_y+rect_h)
	rectx = xrange(rect_x,rect_x+rect_w)

	for m in range(0,maxr):
		for i in range(0,int(numberX*numberY/(stepsize*stepsize))):
			radiusseparation = math.sqrt((fieldParticles[i].x - sourcex[m])**2 + (fieldParticles[i].y - sourcey[m])**2)

			if radiusseparation <= speed * clockTick:	 
				fieldParticles[i].phase = (radiusseparation/speed)*omega
				fieldParticles[i].waveF[m] = int(10*math.sin(fieldParticles[i].angularSpeed * clockTick + fieldParticles[i].phase))
				if m == maxr - 1:
					fieldParticles[i].waveF[m] = fieldParticles[i].waveF[0] + fieldParticles[i].waveF[1]
				if fieldParticles[i].waveF[m] >= 0:
					fieldParticles[i].colour = (255,0,0)
				if fieldParticles[i].waveF[m] < 0:
					 fieldParticles[i].colour = (255,250,250)
				fieldParticles[i].display()
				
				if fieldParticles[i].y in recty and fieldParticles[i].x in rectx:
					
					sourcex[n] = fieldParticles[i].x
					sourcey[n] = fieldParticles[i].y
					maxr = maxr + 1
					n = n + 1
					print n,maxr,m

# advance the clock
	clockTick += 1
	pygame.display.flip()
