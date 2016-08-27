from __future__ import division
import pygame
from pygame import gfxdraw
import math


background_colour = (255,255,255)
(width, height) = (500, 500)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Wave')
screen.fill(background_colour)

# define global time

clockTick = 0

# omega of wave
omega = 2*math.pi/5

# define class for particle
class Particle():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.phase = 0
        self.size = 2
        self.scale = 10
        self.colour = (255, 255, 255)
        self.angularSpeed = omega
# display the particle
    def display(self):
        #pygame.draw.circle(screen, self.colour, (int(self.x), int(self.y)), self.size)
        gfxdraw.pixel(screen, int(self.x), int(self.y), self.colour)
# move the particle
    def move(self):
		waveF = int(10*math.sin(self.angularSpeed * clockTick + self.phase))
		if waveF >= 0:
			self.colour = (255,0,0)
		if waveF < 0:
			 self.colour = (255,250,250)


# now define field as collection of particles
# first define number of particles
numberX = 500
numberY = 500
# create an array to hold the particles
fieldParticles = []
# set the step size
stepsize = 2
# now create the collection
for i in xrange(0,numberX,stepsize):
	for j in xrange(0,numberY,stepsize):
		phase = 0
		x = i
		y = j
		particle = Particle()
		particle.x = x
		particle.y = y
		fieldParticles.append(particle)
		particle.display()

sourcex = [240,260]
sourcey = [0,0]
# define speed of the wave
speed = 5

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
	screen.fill(background_colour)
# advance the clock
	clockTick += 1
	m = 0
	for i in range(0,int(math.trunc(numberX*numberY/(stepsize*stepsize)))):
		radiusseparation = math.sqrt((fieldParticles[i].x - fieldParticles[sourcex[m]].x)**2 + (fieldParticles[i].y - fieldParticles[sourcey[m]].y)**2)
		fieldParticles[i].phase = (radiusseparation/speed)*omega
		if radiusseparation <= speed * clockTick:
			fieldParticles[i].move()
		fieldParticles[i].display()

	pygame.display.flip()
