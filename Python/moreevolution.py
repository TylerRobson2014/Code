from __future__ import division
import pygame
from pygame import gfxdraw
import math
import random
import sys
from copy import deepcopy

background_colour = (255,255,255)
height = int(500)
width = int(500)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Lattice Gas')
screen.fill(background_colour)
	
class grazer(object):
	def __init__(self,x,y,direction,color):
		(self.x,self.y) = (x,y)
		self.direction = direction
		self.color = color
		self.size = 20
		self.speed = 5
		self.FoV = math.pi/6
		self.doV = 50
		self.eyes = 5
		self.detect = [False,"Nothing"]

	def display(self):
		self.eye1x = int(self.x+(self.size)*math.cos(self.direction+self.FoV/2))
		self.eye2x = int(self.x+(self.size)*math.cos(self.direction-self.FoV/2))
		self.eye1y = int(self.y+(self.size)*math.sin(self.direction+self.FoV/2))
		self.eye2y = int(self.y+(self.size)*math.sin(self.direction-self.FoV/2))
		pygame.draw.circle(screen, self.color, (int(self.x),int(self.y)), int(self.size), int(self.size))
		pygame.draw.line(screen, (0,0,0), (int(self.x),int(self.y)), (int(self.x+(self.doV)*math.cos(self.direction)), int(self.y+(self.doV)*math.sin(self.direction))), 1)
		pygame.draw.line(screen, (0,0,0), (int(self.x),int(self.y)), (int(self.x+(self.doV)*math.cos(self.direction+self.FoV/2)), int(self.y+(self.doV)*math.sin(self.direction+self.FoV/2))), 1)
		pygame.draw.line(screen, (0,0,0), (int(self.x),int(self.y)), (int(self.x+(self.doV)*math.cos(self.direction-self.FoV/2)), int(self.y+(self.doV)*math.sin(self.direction-self.FoV/2))), 1)
		pygame.draw.circle(screen, (0,0,0), (int(self.eye1x),int(self.eye1y)), int(self.eyes), int(self.eyes))
		pygame.draw.circle(screen, (0,0,0), (int(self.eye2x),int(self.eye2y)), int(self.eyes), int(self.eyes))

	def move(self):
		if not self.detect[0]:
			self.x += self.speed*math.cos(self.direction)
			self.y += self.speed*math.sin(self.direction)
			if self.x > width: self.x = 0
			if self.y > height: self.y = 0
			if self.x < 0: self.x = width
			if self.y < 0: self.y = height
		
	def turn(self):
		fact = 20
		self.direction += random.uniform(-math.pi/fact, math.pi/fact)
		if self.direction > math.pi: self.direction = -(2 * math.pi - self.direction)
		if self.direction < -math.pi: self.direction = (2 * math.pi - abs(self.direction))
		
	def look(self):
		a = {(x,y) for x in xrange(int(self.x-self.doV),int(self.x+self.doV)) for y in xrange(int(self.y-self.doV),int(self.y+self.doV)) if math.atan2(-self.y+y,-self.x+x) < self.direction + self.FoV and math.atan2(-self.y+y,-self.x+x) > self.direction - self.FoV and abs(self.x-x) > self.size and abs(self.y-y) > self.size}
		self.detect = [False,"Nothing"]
		for b in a:
			try:
				s = screen.get_at((b[0], b[1]))
				if (s[0],s[1],s[2]) == (255,0,0):
					self.detect = [True,"Barrier"]
				if (s[0],s[1],s[2]) == (0,255,255):
					self.detect = [True,"Food"]
			except:
				pass
	def shout(self):
		if self.detect[1] == "Food":
			print "Food"
		if self.detect[1] == "Barrier":
			print "Barrier"

			
class food(object):
	def __init__(x,y,size):
		(self.x,self.y) = (x,y)
		self.size = size
		
class carnivor(object):
	def __init__(x,y,direction,color):
		(self.x,self.y) = (x,y)
		self.direction = direction
		self.color = color

color1 = (255,0,0)
color2 = (0,255,0)
color3 = (0,255,255)

test = grazer(100,100,math.pi/4,color1)

points = []

running = True

timer_event = pygame.USEREVENT + 1
pygame.time.set_timer(timer_event, 50)
screen.fill(background_colour)
while running:
	event = pygame.event.wait()
	if event.type == pygame.QUIT:
		raise StopIteration
	screen.fill(background_colour)

	test.display()
	test.move()
	test.turn()
	mouseB = pygame.mouse.get_pressed()
	mxy = pygame.mouse.get_pos()
	if mouseB[0]:
		points.append(mxy)
	for p in points:
		pygame.draw.circle(screen, color3, p, 5, 5)
	test.look()
	test.shout()
#	test.avoid()
	pygame.display.flip()
