from __future__ import division
import random as r
import numpy as np


class car():
	global distance
	def __init__(self):
		self.direction = r.randint(0,1)
		self.x = self.direction * distance
		self.y = self.direction
		self.start_time = clock_time 
		if self.direction == 0:
			self.direction = 1
		else:
			self.direction = -1
		self.speed = r.gauss(30,5)

	
	def drive(self,clock_time):
		self.x = self.x + self.direction * self.speed * (clock_time-self.start_time)


class predestrian():
	def __init__(self):
		self.speed = 2
		self.y = 0
		self.x = 50
		
	def cross(self,array_of_cars):
		global road
		if len(array_of_cars) == 0: return True
		for car in array_of_cars:
			estimate_speed = r.gauss(car.speed,10)
			sd = car.x*0.2
			estimate_distance = r.gauss(car.x,sd)
			
			cross = False
			
			if car.direction > 0 and (self.x - estimate_distance) > 0:
				if (self.x - estimate_distance)/estimate_speed > (road/self.speed) :cross = True
				if (self.x - estimate_distance)/estimate_speed < (road/self.speed) :cross = False
			if car.direction > 0 and (self.x - estimate_distance) < 0:	
				cross = True
			if car.direction < 0 and (self.x - estimate_distance) > 0:
				cross = True
			if car.direction < 0 and (self.x - estimate_distance) < 0:
				if abs(self.x - estimate_distance)/estimate_speed > (road/self.speed) :cross = True
				if abs(self.x - estimate_distance)/estimate_speed < (road/self.speed) :cross = False				

			return cross	
	
	def walk(self,time):
		self.y = self.y + self.speed * time
		
def carHitsBob(pedX,carX,carDir,killzone):

	HIT = False
	
	if carDir > 0 and (pedX - carX) > 0:
		if (pedX - carX) < killzone :HIT = True
		if (pedX - carX) > killzone :HIT = False

	if carDir < 0 and (pedX - carX) < 0:
		if abs(pedX - carX) > killzone :HIT = False
		if abs(pedX - carX) < killzone :HIT = True				

	return HIT
	
	
road = 10
distance = 20
killzone = 0.1
collision = 0
safe = 0
iteration = 0
total =10000
array_cars = []
for count in xrange(total):
	iteration += 1
	clock_time = 0
	bob = predestrian()
	cars = []
	running = True
	crossing = False
	first = True
	start_walking = 0
	while running:
		number_cars = np.random.poisson(1, 1)
		number_cars = number_cars[0]
		print number_cars
		array_cars.append(number_cars)
		for c in xrange(number_cars):
			newcar = car()
			cars.append(newcar)

		if bob.cross(cars) or crossing:
			crossing = True
			if first: start_walking = clock_time
			first = False
			bob.walk((clock_time-start_walking))
		if bob.y >= road:
			safe += 1
			running = False

		for c in xrange(len(cars)):
			cars[c].drive(clock_time)
			if cars[c].x > distance+5 or cars[c].x < -5: cars[c].speed = 0
			if bob.y <= road/2 : bob_y = 0
			if bob.y >  road/2 : bob_y = 1
			if running:
				if (bob_y == cars[c].y) and carHitsBob(bob.x,cars[c].x,cars[c].direction,killzone):
					collision += 1
					running = False
		clock_time += 1
		#print "run",iteration,"time",clock_time,"Bob at ",bob.y
		#for c in xrange(len(cars)):
			#print "car ",c,cars[c].x,cars[c].y,cars[c].speed

print "Total: ",total
print "safe : ",safe
print "Dead : ",collision
print "Prob die = ",(collision/total)*100,"%"
print sum(array_cars)/total
