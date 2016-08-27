from __future__ import division
import pygame
from pygame import gfxdraw
import math
import random
import sys
import numpy as np
import matplotlib.pyplot as plt


background_colour = (255,255,255)
height = int(500)
width = int(500)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Lattice Gas')
screen.fill(background_colour)

def circles(n,x,y,w):
	global positions,size
	limit = 1000
	side = w - x
	
	for i in xrange(n):
		test1 = False
		test2 = False
		count = 0
		while not(test1 and test2) and count < limit:
			count += 1
			c = False
			overlap = False
			radius = random.randint(5,int(side/5))
			posx = random.randint(x+radius,w-radius)
			posy = random.randint(y+radius,w-radius)
			test1 = posx + radius <= w and posx - radius >= x and posy + radius <= w and posy - radius >=y
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
	side = w - x
	radius = 10
	posx = x+radius
	posy = y+radius
	positions.append([posx,posy,radius])
	radius = 10
	posx = w-radius
	posy = w-radius
	positions.append([posx,posy,radius])

def initial_pop(solutions):
	
	global population_size
	global w,x,y
	
	for j in xrange(population_size):
		xposition = (bin(random.randint(x,w))[2:])
		while len(xposition) < 10:
			xposition = "0" + xposition
		yposition = (bin(random.randint(y,w))[2:])
		while len(yposition) < 10:
			yposition = "0" + yposition
		radius = (bin(random.randint(1,int((w-x)/2)))[2:])
		while len(radius) < 10:
			radius = "0" + radius
		
		gene_string = xposition + yposition + radius
		solutions.append(gene_string)
			
def decode(gene_string):
	result = []
	i = 0
	while i < len(gene_string):
		string = gene_string[i:i+10]
		conversion = int(string,2)
		result.append(conversion)
		i = i + 10
	return result
	
def fitness(solutions):
	fitness_function = []
	converted = []
	global positions,x,w,area
	global fitness_record
	for i in xrange(len(solutions)):
		fitness_function.append(0)
		converted = decode(solutions[i])
		posx = converted[0]
		posy = converted[1]
		radius = converted[2]
		test2 = False
		overlap = False
		test1 = posx + radius <= w and posx - radius >= x and posy + radius <= w and posy - radius >=y
		if len(positions) > 0:
			for j in xrange(len(positions)):
				c = math.sqrt((posx - positions[j][0])**2 + (posy - positions[j][1])**2) < (radius + positions[j][2])
				if c:
					overlap = True
			test2 = not(overlap)		
		else:
			test2 = True
		if test1 and test2:
			fitness_value = (math.pi*radius**2)/area
			#print "*******************",posx,posy,radius,(math.pi*radius**2)/area
			if fitness_value > 0.46:
				print "Done????????????????",fitness_value
				fitness_value = -1
		else:
			fitness_value = 0.000000000001	
		fitness_function[i] = fitness_value
	fitness_record.append(max(fitness_function))
	return fitness_function

def select_genese_old(fitness_f,solutions):
	res = []
	pie = []
	selections = ["",""]
	min_fit = min(fitness_f)
	for i in xrange(len(fitness_f)):
		ss = fitness_f[i]/min_fit
		for j in xrange(int(ss)):
			pie.append(i)
	selections[0] = solutions[random.choice(pie)]
	selections[1] = solutions[random.choice(pie)]
	return selections
	
def select_genes2(fitness_f,solutions):
	dummy = [[[0] for x in xrange(2)] for m in xrange(len(fitness_f))]
	for i in xrange(len(fitness_f)):
		dummy[i][0] = fitness_f[i]
		dummy[i][1] = solutions[i]
	dummy.sort()
	for j in xrange(2):
		sum_fit = 0
		for i in xrange(len(fitness_f)):
			sum_fit += dummy[i][0]
		rand_num = random.uniform(0,sum_fit)
		sum_fit = 0
		flag = 0
		for i in xrange(len(fitness_f)):
			sum_fit += dummy[i][0]
			if sum_fit > rand_num and flag == 0:
				selections[j] = dummy[i][1]
				flag = 1
	return selections	
	
def crossover(solutions,j):
	swap_point = random.randint(1,2)*10
	partial_1 = ""
	partial_2 = ""

	if swap_point > 0 and swap_point < 30:
		partial_1 = solutions[j][:swap_point]
		partial_2 = solutions[j+1][:swap_point]
		h = list(solutions[j+1])
		for i in xrange(swap_point):
			h[i] = partial_1[i]
		try:
			solutions[j+1] = ''.join(h)
		except: 
			e = sys.exc_info()[0]
		k = list(solutions[j])
		for i in xrange(swap_point):
			k[i] = partial_2[i]
		try:
			solutions[j] = ''.join(k)
		except: 
			e = sys.exc_info()[0]
	return solutions
	
def mutation(solutions,j):
	global mut_rate
	k = list(solutions[j])
	l = list(solutions[j+1])
	for i in xrange(len(k)):
		toss = random.randint(0,1000)
		if toss < mut_rate:
			if k[i] == "1":
				k[i] = "0"
			else:
				k[i] = "1"
		toss = random.randint(0,1000)
		if toss < mut_rate:
			if l[i] == "1":
				l[i] = "0"
			else:
				l[i] = "1"
	solutions[j] = ''.join(k)
	solutions[j+1] = ''.join(l)
	return solutions
		
color1 = (255,0,0)
color2 = (0,255,0)

population_size = 50
area = 0
size = 0
positions = []
n = 10
w = 210
(x,y) = (10,10)	
solutions = []
newsolutions = []
fitness_record = []
selections = ["",""]
Done = False
generation = 1
mut_rate = 10

test_circles(n,x,y,w)
initial_pop(solutions)
get_area(positions)
newsolutions = []

while not(Done):
	generation += 1
	fitness_f = fitness(solutions)

	for i in xrange(len(fitness_f)):
		if fitness_f[i] == -1:
			winner = min(fitness_f)
			print "Done"
			print solutions[i]
			Done = True
	if not(Done):
		i = 0
		winner = max(fitness_f)
		print "*******************",winner
		while i < (population_size):
			selections = select_genes2(fitness_f,solutions)
			newsolutions.append(selections[0])
			newsolutions.append(selections[1])
			newsolutions = crossover(newsolutions,i)
			newsolutions = mutation(newsolutions,i)
			i = i + 2
		solutions = newsolutions

	fitness_record.append(winner)

plt.plot(fitness_record)
plt.show()
print fitness_record
first = True
running = True
timer_event = pygame.USEREVENT + 1
pygame.time.set_timer(timer_event, 100)
screen.fill(background_colour)
while running:
	event = pygame.event.wait()
	if event.type == pygame.QUIT:
		raise StopIteration
	screen.fill(background_colour)
	
	pygame.draw.rect(screen, color1, (x,y,w-x,w-y), 1)

	for i in xrange(len(positions)):
		pygame.draw.circle(screen, color1, (positions[i][0],positions[i][1]), positions[i][2], 1)
	
	win = decode(solutions[fitness_f.index(winner)])
	pygame.draw.circle(screen, color2, (win[0],win[1]), win[2], 1)

	pygame.display.flip()
	


