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
	def __init__(self,(x,y),speed,orient,bid,color):
		self.x = x
		self.y = y
		self.speed = speed
		self.bearing = orient
		self.vx = self.speed*math.cos(self.bearing)
		self.vy = self.speed*math.sin(self.bearing)
		self.size = 2
		self.bid = bid
		self.horizon = 50
		self.colour = color
		self.home = [width/2 , height/2]

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
					sumVX += bird.speed*math.cos(bird.bearing)
					sumVY += bird.speed*math.sin(bird.bearing)
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
		
	def bounce_opt2(self):
		if self.x > width:
			self.x = 0
		if self.x < 0:
			self.x = width
		if self.y > height:
			self.y = 0
		if self.y < 0:
			self.y = height
	def adjust_speed(self,flock_birds):
		sumSPEED = 0
		count = 0
		for bird in flock_birds:
			if bird.bid != self.bid:
				distance = (bird.x-self.x)**2 + (bird.y-self.y)**2
				distance = math.sqrt(distance)
				if distance < self.horizon:
					sumSPEED += bird.speed
					count += 1
		if count > 0:
			sumSPEED = sumSPEED/count
			self.speed = sumSPEED
					
	def random_move(self):
		coin_toss = random.randint(1 , 10)
		if coin_toss < 6:
			factor = random.gauss(1.0,2.5)
			self.bearing *= factor
			self.vx = self.speed * math.cos(self.bearing)
			self.vy = self.speed * math.sin(self.bearing)

	def gohome(self, flock_birds):
		count = 0
		for bird in flock_birds:
			distance_from_home2 = (bird.x - bird.home[0])**2 + (bird.y - bird.home[1])**2 
			if math.sqrt(distance_from_home2) > 50:
				toss = random.gauss(5 , 2)
				if toss > 6 or toss < 4:
					self.bearing = math.atan2(self.y - self.home[1],self.x - self.home[0])
					self.vx = -self.speed*math.cos(self.bearing)
					self.vy = -self.speed*math.sin(self.bearing) 	

	def avoidob(self):
		radius = 20
		zone = 5 * radius
		centx = 200
		centy = 200
		pygame.draw.circle(screen, (0,0,0), (centx, centy), zone, 1)
		pygame.draw.circle(screen, (0,0,0), (centx, centy), radius, 2)
		d = (self.x-centx)**2 + (self.y-centy)**2
		d = math.sqrt(d)
		if d >= radius:
			angle = math.atan2(centy - self.y , centx - self.x)
			if angle < 0: angle += 2 * math.pi
			delta = math.atan2(radius,math.sqrt((d**2 - radius**2)))
			#print d
			f = 180/math.pi
			#self.bearing = abs(self.bearing) % (2 * math.pi)
			if d < zone:
				if angle < 0:
					testAngleL = (angle + delta)
					testAngleU = angle - delta
				if angle > 0:
					testAngleL = angle - delta
					testAngleU = (angle + delta) 
				testp = self.bearing
				if testp < 0: testp += 2 * math.pi
				#print "avoid",testp*f,delta*f,angle,testAngleL*f,testAngleU*f
				if testp < testAngleU and self.bearing >= angle:
					#print "add"
					#raw_input()
					self.bearing += (((radius/d)*180)/180)*math.pi
				elif testp > testAngleL and self.bearing < angle:
					self.bearing -= (((radius/d)*180)/180)*math.pi
					#print "sub"
					#raw_input()
		else: 
			self.bearing += math.pi
			

	def move(self):
		self.x = self.x + self.speed*math.cos(self.bearing)
		self.y = self.y + self.speed*math.sin(self.bearing)
	def display(self):
		pygame.draw.circle(screen, self.colour, (int(self.x), int(self.y)), self.size, self.size)
		pygame.draw.line(screen, self.colour, (self.x, self.y), (int(self.x+(self.size*5)*math.cos(self.bearing)), int(self.y+(self.size*5)*math.sin(self.bearing))), 1)	

def set_speed():
	return random.gauss(15 , 0.2)

def set_orientation():
	#return random.uniform(0 , 2*math.pi)
	return random.gauss(math.pi/2 , math.pi)
	
number_of_birds = 100

flock_birds = []

for n in range(number_of_birds):
	x = random.gauss(width/2, 50)
	y = random.gauss(height/2, 50)
	speed = set_speed()
	orient = set_orientation()
	bid = n
	if n == 0:
		color = (255,0,0)
	else:
		color = (0,0,0)
	flock_birds.append(Bird((x, y),speed,orient,bid,color))
	

running = True
timer_event = pygame.USEREVENT + 1
pygame.time.set_timer(timer_event, 1)
screen.fill(background_colour)
while running:
	event = pygame.event.wait()

	screen.fill(background_colour)

	for bird in flock_birds:
		bird.random_move()
#		bird.gohome()
		bird.findSpace(flock_birds)
		bird.moveToCoG9self(flock_birds)
		#bird.findSpace(flock_birds)
		bird.setdirection(flock_birds)
		#bird.findSpace(flock_birds)
		bird.bounce_opt2()
		bird.avoidob()
		bird.move()
		bird.display()

	pygame.display.flip()

