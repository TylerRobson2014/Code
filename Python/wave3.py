from __future__ import division
import pygame
import math


background_colour = (255,255,255)
(width, height) = (500, 500)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Wave')
screen.fill(background_colour)

# omega of wave
period = 200
omega = 2*math.pi/period

# define class for particle
class Particle():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.oppy = 0
        self.phase = 0
        self.size = 2
        self.scale = 10
        self.colour = (0, 0, 255)
        self.angularSpeed = omega
        self.amp = 50
        self.force = 0
# display the particle
    def display(self):
        pygame.draw.circle(screen, self.colour, (int(self.x), int(self.y)), self.size)
# move the particle
    def move(self):
		self.y = int(self.amp*math.sin(self.angularSpeed * time))
		self.oppy = int(self.amp*math.sin(self.angularSpeed * anticlock + math.pi))
		self.y = self.y + self.oppy + 100

# now define field as collection of particles
# first define number of particles
numberX = 5

# create an array to hold the particles
fieldParticles = []
# set the step size
stepsize = 1
# now create the collection
for i in xrange(0,numberX,stepsize):
	phase = 0
	x = i
	y = 100
	particle = Particle()
	particle.x = x
	particle.y = y
	if i == 0 or i == int(numberX/stepsize):
		particle.amp = 0
	fieldParticles.append(particle)

sourcex = 0

# define speed of the wave
speed = 10
flag = 0
# define global time
clockTick = 0
anticlock = int(numberX/stepsize)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
	screen.fill(background_colour)
	for i in range(0 , int(numberX/stepsize)):
		fieldParticles[i].display()

#	for i in range(0,int(numberX/stepsize)):
	time = clockTick
	fieldParticles[clockTick].move()
	fieldParticles[clockTick].display()
	clockTick += 1
	anticlock -= 1
	if clockTick == int(numberX/stepsize):
		clockTick = 0
		anticlock = int(numberX/stepsize)
		

	pygame.display.flip()
