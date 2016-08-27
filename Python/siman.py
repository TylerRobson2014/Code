from __future__ import division
import pygame
from pygame import gfxdraw
import math
import random
import sys
from copy import deepcopy
#import numpy as np



background_colour = (255,255,255)
height = int(500)
width = int(500)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Lattice Gas')
screen.fill(background_colour)

def circles(n,x,y,w):
	global positions,size
	limit = 1000
	side = w
	
	for i in xrange(n):
		test1 = False
		test2 = False
		count = 0
		while not(test1 and test2) and count < limit:
			count += 1
			c = False
			overlap = False
			radius = random.randint(5,int(side/5))
			posx = random.randint(x+radius,x+w-radius)
			posy = random.randint(y+radius,y+w-radius)
			test1 = posx + radius <= w+x and posx - radius >= x and posy + radius <= w + y and posy - radius >=y
			if len(positions) > 0:
				for j in xrange(len(positions)):
					c = math.sqrt((posx - positions[j][0])**2 + (posy - positions[j][1])**2) < (radius + positions[j][2])
					if c:
						overlap = True
				test2 = not(overlap)		
			else:
				test2 = True		
		if count < limit:
			positions.append([posx,posy,radius])

def get_area(positions):
	global area,w
	area = 0
	for i in xrange(len(positions)):
		area += math.pi * positions[i][2]**2
	area = w**2 - area
	

def test_circles(n,x,y,w):
	global positions,size
	limit = 1000
	side = w
	radius = 1
	posx = x+radius
	posy = y+radius
	positions.append([posx,posy,radius])
	radius = 1
	posx = x+w-radius
	posy = y+w-radius
	positions.append([posx,posy,radius])

def test(sol):
	global positions,x,y,w,area,max_pc_area
	global fitness_record
	posx = sol[0]
	posy = sol[1]
	radius = sol[2]
	test2 = False
	overlap = False
	test1 = posx + radius <= w+x and posx - radius >= x and posy + radius <= w+y and posy - radius >=y
	if len(positions) > 0:
		for j in xrange(len(positions)):
			c = math.sqrt((posx - positions[j][0])**2 + (posy - positions[j][1])**2) < (radius + positions[j][2])
			if c:
				overlap = True
		test2 = not(overlap)		
	else:
		test2 = True
	
	if test1 and test2:
		return True
	else:
		return False
	

def cost(sol):
	global positions,x,y,w,area,max_pc_area
	global fitness_record
	posx = sol[0]
	posy = sol[1]
	radius = sol[2]
	if test(sol):
		try:
			fitness_value = (area/(math.pi*radius))
		except:
			fitness_value = 0.000000000001
	else:
		fitness_value = 10
	return fitness_value

def gensol(x,y,w):
	global positions
	#w-x,w-y
	solution = [0,0,0]
	while not(test(solution)):
		posx = random.randint(x,w+x)
		posy = random.randint(y,w+y)
		radius = random.uniform(1,w/2)
		solution[0] = posx
		solution[1] = posy
		solution[2] = radius
	return solution
	
def neighbor(sol):
	global x,y,w

	toss = random.randint(1,3)
	dum = deepcopy(sol)
	fact = 1
	dum[0] = int(random.gauss(sol[0],w))
	dum[1] = int(random.gauss(sol[1],w))
	dum[2] = random.gauss(sol[2],w)
	if dum[2] < 1: dum[2] = 1
	print "re-check"
	print dum

	while not(test(dum)):
		
		
		
		#raw_input()

		dum[0] = int(random.gauss(sol[0],w))
		dum[1] = int(random.gauss(sol[1],w))
		dum[2] = random.gauss(sol[2],w)
		if dum[2] < 1: dum[2] = 1
	
	sol = deepcopy(dum)
	print "exit"
	print dum
#	raw_input()

	return sol
	
def acceptance_probability(ocost,ncost,temp):
	ap = math.exp(-(ncost - ocost)/(temp))
	return ap
	

color1 = (255,0,0)
color2 = (0,255,0)

n = 20

w = 200
(x,y) = (10,10)	

population_size = 50
area = 0
size = 0
positions = []

circles(n,x,y,w)
get_area(positions)

solution = gensol(x,y,w)

old_cost = cost(solution)
T = 1.0
T = 0.1
T_min = 0.00000001
alpha = 0.999

first = True
running = True
Done = False
timer_event = pygame.USEREVENT + 1
pygame.time.set_timer(timer_event, 50)
screen.fill(background_colour)
while running:
	event = pygame.event.wait()
	if event.type == pygame.QUIT:
		raise StopIteration
	screen.fill(background_colour)
	
	pygame.draw.rect(screen, color1, (x,y,w+x,w+y), 1)
	for i in xrange(len(positions)):
		pygame.draw.circle(screen, color1, (positions[i][0],positions[i][1]), positions[i][2], 1)
	pygame.draw.circle(screen, color2, (solution[0],solution[1]), int(solution[2]), 1)

	if T > T_min:
		
		i = 1
		while i < 200:

#			
			print "T = ",T

			a = x
			b = y
			c = w

			#new_solution = neighbor(solution)

			new_solution = gensol(a,b,c)
				
			new_cost = cost(new_solution)
			if new_cost <= old_cost:
				old_cost = new_cost
				solution = new_solution
			else:
				ap = acceptance_probability(old_cost, new_cost, T)
				print "ap = ",ap
				r = random.uniform(0,1)
				print "r = ",r
				if ap > r:
					solution = new_solution
					old_cost = new_cost
			i += 1
		T = T * alpha
	else:
		running = False
		print "End"
		
	pygame.display.flip()
while True:
	pass
	

