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
	def __init__(self,(x,y),(vx,vy),fuse,color):
		self.x = x
		self.y = y
		self.vx = vx
		self.vy = vy
		self.fuse = fuse
		self.color = color
		self.radius = 10
		self.sphere = [[0 for i in xrange(3)] for j in xrange(900)]

	def populate_sphere(self):
		radius = 2
		dev = 30
		phi = 0
		count = 0
		for phi in xrange(0,dev):
			theta = 0
			for theta in xrange(0,dev):
				self.sphere[count][0] = radius * math.sin(phi * 2 * math.pi/dev) * math.cos(theta * 2 * math.pi/dev) 
				self.sphere[count][1] = radius * math.sin(theta * 2 * math.pi/dev)
				self.sphere[count][2] = radius * math.cos(theta * 2 * math.pi/dev) * math.cos(phi * 2 * math.pi/dev)
				count += 1
				theta += 1
			phi += 1

	def display_fw(self,count):
		newsphere = [[0 for i in xrange(3)] for j in xrange(900)]
		dev = 30	
		phi = 0
		cc = 0
		if count >= self.fuse:
			self.radius = self.radius + 1
			for phi in xrange(0,dev):
				theta = 0
				for theta in xrange(0,dev):
					cx = (self.sphere[cc][0] * abs(self.sphere[cc][2]*0.0015+1))
					cy = (self.sphere[cc][1] * abs(self.sphere[cc][2]*0.0015+1))
					
					cx *= self.radius
					cy *= self.radius
					
					cx += self.x
					cy += self.y
					
					pygame.draw.circle(screen, self.color, (int(cx),int(cy)), 2, 2)
					
					theta += 1
					cc += 1
				phi += 1
		else:
			pygame.draw.circle(screen, (255,255,255), (int(self.x),int(self.y)), 2, 2)
	
	def launch(self):
		self.x = random.randint(100,400)
		self.y = 400
		self.vy = random.randint(20,25)
		self.vx = 0
		self.fuse = random.randint(8,12)
		self.radius = 2
		c = random.randint(1,6)
		if c == 1: self.color = (255,0,0)
		if c == 2: self.color = (0,255,0)
		if c == 3: self.color = (0,0,255)
		if c == 4: self.color = (255,255,224)
		if c == 5: self.color = (178,34,34)
		
	def move(self,count):
		if count <= self.fuse:
			self.vy -= 1
		else:
			if self.vy > 0: self.vy -= 1.5
			if self.vy <=0: self.vy = 0
		self.x += self.vx
		self.y -= self.vy

color0 = (0,0,0)
color4 = (255,255,255)

number_of_FWs = random.randint(1,10)
FireWorks = []
for i in xrange(number_of_FWs):
	FireWorks.append(firework((200,400),(0,0),0,(255,0,0)))

for fw in FireWorks:
	fw.populate_sphere()
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
		fw.move(count)
	
	count += 1

	pygame.display.flip()

