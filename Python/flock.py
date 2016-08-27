from __future__ import division
import pygame
from pygame import gfxdraw
import math
import random


background_colour = (255,255,255)
(width, height) = (800, 500)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Flock')
screen.fill(background_colour)

class Bird():
	def __init__(self,(x,y),(vx,vy),bid,color):
		self.x = x
		self.y = y
		self.vx = vx
		self.vy = vy
		self.speed = math.sqrt(vx**2+vy**2)
		self.bearing = math.atan2(vy,vx)
		self.size = 1
		self.bid = bid
		self.horizon = 50
		self.colour = color

	def findSpace(self,flock_birds):
		(sumX, sumY) = (0, 0)
		found = False
		for bird in flock_birds:
			if bird.bid != self.bid:
				distance = (bird.x-self.x)**2 + (bird.y-self.y)**2
				distance = math.sqrt(distance)
				if distance < self.horizon:
					sumX += (self.x - bird.x)
					sumY += (self.y - bird.y)
					found = True
		if found:
			#sumX = math.copysign(sumX,-0.0)
			#sumY = math.copysign(sumY,-0.0)
			
			self.bearing = math.atan2(sumY,sumX)
			self.vx = self.speed*math.cos(self.bearing)
			self.vy = self.speed*math.sin(self.bearing) 
						
	def setdirection(self,flock_birds):
		(sumVX, sumVY) = (0, 0)
		count = 0
		for bird in flock_birds:
			if bird.bid != self.bid:
				distance = (bird.x-self.x)**2 + (bird.y-self.y)**2
				distance = math.sqrt(distance)
				if distance < self.horizon:
					sumVX += bird.vx
					sumVY += bird.vy
					count += 1
		if count > 0:
			sumVX = sumVX/count
			sumVY = sumVY/count
			self.bearing = math.atan2(sumVY,sumVX)
			self.vx = self.speed*math.cos(self.bearing)
			self.vy = self.speed*math.sin(self.bearing) 
		
	def moveToCoG9self(self,flock_birds):
		(sumX, sumY) = (0, 0)
		(CoMx, CoMy) = (0, 0)
		count = 0
		for bird in flock_birds:
			if bird.bid != self.bid:
				distance = (bird.x-self.x)**2 + (bird.y-self.y)**2
				distance = math.sqrt(distance)
				if distance < self.horizon:
					sumX += bird.x
					sumY += bird.y
					count += 1
		if count > 0:
			CoMx = sumX/count
			CoMy = sumY/count
			self.bearing = math.atan2(self.y - CoMy,self.x - CoMx)
			self.vx = -self.speed*math.cos(self.bearing)
			self.vy = -self.speed*math.sin(self.bearing) 					
		
	def bounce_opt1(self):
		if self.x > width:
			self.vx = -self.vx
		if self.x < 0:
			self.vx = -self.vx
		if self.y > height:
			self.vy = -self.vy
		if self.y < 0:
			self.vy = -self.vy
	def bounce_opt2(self):
		if self.x > width:
			self.x = 0
		if self.x < 0:
			self.x = width
		if self.y > height:
			self.y = 0
		if self.y < 0:
			self.y = height
	def move(self):
		self.x = self.x + self.vx
		self.y = self.y + self.vy
	def display(self):
		self.bearing = math.atan2(self.vy,self.vx)
		pygame.draw.circle(screen, self.colour, (int(self.x), int(self.y)), self.size, self.size)
		pygame.draw.line(screen, self.colour, (self.x, self.y), (int(self.x+(self.size*5)*math.cos(self.bearing)), int(self.y+(self.size*5)*math.sin(self.bearing))), 1)	

number_of_birds = 20

flock_birds = []

for n in range(number_of_birds):
	x = random.randint(width/2-50, width/2+50)
	y = random.randint(height/2-50, height/2+50)
	vx = random.randint(-2,2)
	vy = random.randint(-2,2)
	if vx == 0:
		vx = 1
	if vy == 0:
		vy = 1
	speed = math.sqrt(vx**2+vy**2)
	bid = n
	if n == 0:
		color = (255,0,0)
	else:
		color = (0,0,0)
	flock_birds.append(Bird((x, y),(vx,vy),bid,color))
	

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

	screen.fill(background_colour)

	for bird in flock_birds:
		bird.findSpace(flock_birds)
		bird.moveToCoG9self(flock_birds)
		bird.setdirection(flock_birds)
		
	for bird in flock_birds:	
		
		bird.move()
		bird.bounce_opt2()
		bird.display()

	pygame.display.flip()

