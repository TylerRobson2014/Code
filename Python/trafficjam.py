from __future__ import division
import random
import numpy as np
import math
import pygame
from copy import deepcopy


background_colour = (255,255,255)
(width, height) = (800, 500)

screen = pygame.display.set_mode((width, height))
screen.fill(background_colour)

class car():
	def __init__(self,id,position,speed,reaction_time,color,radius):
		self.speed = speed
		self.position = position
		self.reaction_time = reaction_time
		self.radius = radius
		self.color = color
		self.id = id
		self.maxspeed = 5

	
	def drive(self,clock_tick):
		global number_blobs,blobs,BREAK
		if not clock_tick%51:
			start = (self.position)
			end = (self.position+self.speed+1)
			dummy=self.mysum(start,end)-1
			if dummy == 0 and not (blobs[(self.position+1)%number_blobs])>0:
				if self.speed == 0: self.speed += 1
				self.setcol()
				blobs[self.position] = 0
				self.position = (self.position+self.speed)%number_blobs
				blobs[self.position] = 1
			else:
				self.press_break()
			if self.mysum(start,end+5)-1 == 0:
				if self.speed < self.maxspeed: self.speed += 1
				

	def press_break(self):
		global number_blobs,blobs
		self.color = (255,0,0)
		start = (self.position)
		end = (self.position+self.speed+1)
		dummy=self.mysum(start,end)-1
		#print dummy
		while dummy > 0 and self.speed > 0:
			#print self.speed, dummy
			self.speed -= 1
			start = (self.position)
			end = (self.position+self.speed+1)
			dummy=self.mysum(start,end) -1

	def setcol(self):
		if self.speed < 2:
			self.color = (0,204,0)
		elif self.speed < 3:
			self.color = (0,0,255)
		elif self.speed < 4:
			self.color = (255,255,0)
		elif self.speed < 5:
			self.color = (255,0,127)
		elif self.speed == 5:
			self.color = (255,128,0)	

	def mysum(self,start,end):
		global blobs,number_blobs
		if start < number_blobs and end < number_blobs:
			return sum(blobs[start:end])
		elif start < number_blobs and end == number_blobs:
			return sum(blobs[start:number_blobs]) + blobs[0]
		elif start < number_blobs and end > number_blobs:
			return sum(blobs[start:number_blobs]) + sum(blobs[0:end-number_blobs])
		elif start >= number_blobs:
			return sum(blobs[start-number_blobs:end-number_blobs])

 
running = True
timer_event = pygame.USEREVENT + 1
pygame.time.set_timer(timer_event, 1)
screen.fill(background_colour)

track_radius = 210
number_cars = 150
number_blobs = 200
radius = 5
blobs = [0 for x in xrange(number_blobs)]
reaction_time = 0.5
color = (0,0,0)
cars = []
for i in xrange(number_cars):
	position = i*int(number_blobs/number_cars)
	blobs[position] = 1
	start_speed = random.randint(1,5)
	if start_speed < 2:
		color = (0,204,0)
	elif start_speed < 3:
		color = (0,0,255)
	elif start_speed < 4:
		color = (255,255,0)
	elif start_speed < 5:
		color = (255,0,127)
	elif start_speed == 5:
		color = (255,128,0)	
	c = car(i,position,start_speed,reaction_time,color,radius)
	cars.append(c)

clock_tick = 0
time_check = 0

while running:
	clock_tick += 1
	event = pygame.event.wait()

	screen.fill(background_colour)
	BREAK = False
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			# User pressed down on a key
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				if cars[0].speed > 0:
					cars[0].speed += -1
					cars[0].color = (255,0,0)
					BREAK = True
					time_check = clock_tick
				
					#print "Hi"	
		
	for i in xrange(0,number_blobs):
		theta = i*2*math.pi/number_blobs
		x = track_radius*math.cos(theta)+width/2
		y = track_radius*math.sin(theta)+height/2
		if blobs[i] == 0:
			color = (106,106,106)
		else:
			for c in cars:
				if c.position == i:
					color = c.color
		pygame.draw.circle(screen, color, (int(x),int(y)), radius, radius)
		if BREAK or clock_tick < time_check + 100:
			if i == cars[0].position:
				print cars[0].speed
				pygame.draw.circle(screen, (255,0,0), (int(x),int(y)), 2*radius, 2*radius)
				#print "break"
		
	for c in cars:
		c.drive(clock_tick)

	#pygame.display.flip()
	pygame.display.update()
