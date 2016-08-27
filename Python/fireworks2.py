from __future__ import division
import pygame
from pygame import gfxdraw
import math
import random
from random import shuffle

background_colour = (0,0,0)
height = int(500)
width = int(500)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Lattice Gas')
screen.fill(background_colour)


class firework():
	def __init__(self,(startx,starty),(vx,vy),fuse,color):
		self.startx = startx
		self.starty = starty
		self.vx = vx
		self.vy = vy
		self.fuse = fuse
		self.color = color

	def populate():
		pass



	def display_fw(count):
		global xpos,ypos,zpos
		global sphere,dev
		newsphere = [[0 for x in xrange(3)] for y in xrange(dev*dev)]	
		phi = 0
		count = 0
		if count - self.fuse <= 0:
			for phi in xrange(0,dev):
				theta = 0
				for theta in xrange(0,dev):
					x = (self.sphere[count][0] * abs(self.sphere[count][2]*0.0015+1) * abs(zpos*0.0015+1))
					y = (self.sphere[count][1] * abs(self.sphere[count][2]*0.0015+1) * abs(zpos*0.0015+1))
					
					x *= radius
					y *= radius
					
					x += xpos
					y += ypos
					
					pygame.draw.circle(screen, self.color, (int(x),int(y)), 2, 2)
					
					theta += 1
					count += 1
				phi += 1
		else:
			pygame.draw.circle(screen, (255,255,255), (xpos,ypos), 2, 2)
	
	def launch():
		self.startx = random.randint(100,400)
		self.starty = 400
		self.vy = random.randint(20,25)
		self.vx = random.randint(0,5)
		self.fuse = random.randint(8,12)
		c = random.randint(1,6)
		if c == 1: self.color = (255,0,0)
		if c == 2: self.color = (0,255,0)
		if c == 3: self.color = (0,0,255)
		if c == 4: self.color = (255,255,224)
		if c == 5: self.color = (178,34,34)

color0 = (0,0,0)
color4 = (255,255,255)

number_of_FWs = 5
FireWorks = []
for i in xrange(number_of_FWs):
	FireWorks.append(firework((200,400),(0,0),0,(255,0,0)))

for fw in FireWorks:
	fw.populate()
	fw.launch()

running = True

count = 0

timer_event = pygame.USEREVENT + 1
pygame.time.set_timer(timer_event, 100)
screen.fill(background_colour)
while running:
	event = pygame.event.wait()
	if event.type == pygame.QUIT:
		raise StopIteration
	screen.fill(background_colour)

	for fw in FireWorks:
		fw.display_fw(count)
	
	count += 1

	pygame.display.flip()

