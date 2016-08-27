from __future__ import division
import pygame
from pygame import gfxdraw
import math
import random
import sys
#import numpy as np
#import matplotlib.pyplot as plt


background_colour = (255,255,255)
height = int(500)
width = int(500)


screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Lattice Gas')
screen.fill(background_colour)

def initial_pop(solutions):
	global population_size,size
	maxsize = size*size
	for j in xrange(population_size):
		gene = ""
		for k in xrange(maxsize):
			gene += str(random.randint(0,1))
		solutions.append(gene)
			
def decode(gene_string):
	global size
	grid = [[["."] for i in xrange(size)] for j in xrange(size)]
	count = 0
	for j in xrange(size):
		for i in xrange(size):
			grid[i][j][0] = gene_string[count]
			count += 1
	return grid

def check(d):
	count = 0
	record = []
	for i in xrange(len(d)):
		if d[i][0] == "1":
			count += 1
		if d[i][0] == "0" or d[i][0] == ".":
			if count == 0:
				pass
			else:
				record.append(count)
				count = 0
	if count > 0:
		record.append(count)
		count = 0
		
	return record
	
def fitness(solutions):
	fitness_function = []

	global constraints,size
	global fitness_record
	for i in xrange(len(solutions)):
		
		grid = []
		d1 = []
		r1 = []
	
		fitness_function.append(0)
		grid = decode(solutions[i])

		diff01 = 0
		diff02 = 0
		diff11 = 0
		diff12 = 0
		fit = 0
		found0 = 0
		found1 = 0

		for m in xrange(size):
			d1 = [grid[m][k] for k in xrange(size)]
			r1 = check(d1)
			diff01 += abs(len(r1) - len(constraints[0][m]))
			if len(r1) - len(constraints[0][m]) == 0:
				for nn in xrange(len(r1)):
					diff02 += abs(r1[nn] - constraints[0][m][nn])
					found0 = 1
					#print "diff01 diff02",diff01,diff02
					#print "found0",found0

		for m in xrange(size):
			d1 = [grid[k][m] for k in xrange(size)]
			r1 = check(d1)
			diff11 += abs(len(r1) - len(constraints[1][m]))
			if len(r1) - len(constraints[1][m]) == 0:
				for nn in xrange(len(r1)):
					diff12 += abs(r1[nn] - constraints[1][m][nn])
					found1 = 1
					#print "diff11 diff12",diff11,diff12
					#print "found1",found1		
		w = 0
		mass = 10000
		if not(found0): diff02 = mass
		if not(found1): diff12 = mass
		if True:
			if not (grid[3][3][0] == "1"): w = mass
			if not (grid[4][3][0] == "1"): w = mass
			if not (grid[12][3][0] == "1"): w = mass
			if not (grid[13][3][0] == "1"): w = mass
			if not (grid[21][3][0] == "1"): w = mass
			if not (grid[6][8][0] == "1"): w = mass
			if not (grid[7][8][0] == "1"): w = mass
			if not (grid[10][8][0] == "1"): w = mass
			if not (grid[14][8][0] == "1"): w = mass
			if not (grid[15][8][0] == "1"): w = mass
			if not (grid[18][8][0] == "1"): w = mass
			if not (grid[6][16][0] == "1"): w = mass
			if not (grid[11][16][0] == "1"): w = mass
			if not (grid[16][16][0] == "1"): w = mass
			if not (grid[20][16][0] == "1"): w = mass
			if not (grid[3][21][0] == "1"): w = mass
			if not (grid[4][21][0] == "1"): w = mass
			if not (grid[9][21][0] == "1"): w = mass
			if not (grid[10][21][0] == "1"): w = mass
			if not (grid[15][21][0] == "1"): w = mass
			if not (grid[20][21][0] == "1"): w = mass
			if not (grid[21][21][0] == "1"): w = mass

		try:
			fit = 1/(diff01 + diff11 + diff12 + diff02 + w)
			#fit = 1/(diff12 + diff02) 
		except:
			fit = -1
		fitness_function[i] = fit
	fitness_record.append(max(fitness_function))
	#print "max",max(fitness_function)
	return fitness_function

def marks():
	
	global size
	
	mark = [[[0 for i in xrange(9)] for j in xrange(size)] for k in xrange(size)]

	mark[0][0] = [7,2,1,1,7]
	mark[0][1] = [1,1,2,2,1,1]
	mark[0][2] = [1,3,1,3,1,3,1,3,1]
	mark[0][3] = [1,3,1,1,5,1,3,1]
	mark[0][4] = [1,3,1,1,4,1,3,1]
	mark[0][5] = [1,1,1,2,1,1]
	mark[0][6] = [7,1,1,1,1,1,7]
	mark[0][7] = [1,1,3]
	mark[0][8] = [2,1,2,1,8,2,1]
	mark[0][9] = [2,2,1,2,1,1,1,2]
	mark[0][10] = [1,7,3,2,1]
	mark[0][11] = [1,2,3,1,1,1,1,1]
	mark[0][12] = [4,1,1,2,6]
	mark[0][13] = [3,3,1,1,1,3,1]
	mark[0][14] = [1,2,5,2,2]
	mark[0][15] = [2,2,1,1,1,1,1,2,1]
	mark[0][16] = [1,3,3,2,1,8,1]
	mark[0][17] = [6,2,1]
	mark[0][18] = [7,1,4,1,1,3]
	mark[0][19] = [1,1,1,1,4]
	mark[0][20] = [1,3,1,3,7,1]
	mark[0][21] = [1,3,1,1,1,2,1,1,4]
	mark[0][22] = [1,3,1,4,3,3]
	mark[0][23] = [1,1,2,2,2,6,1]
	mark[0][24] = [7,1,3,2,1,1]
	
	mark[1][0] = [7,3,1,1,7]
	mark[1][1] = [1,1,2,2,1,1]
	mark[1][2] = [1,3,1,3,1,1,3,1]
	mark[1][3] = [1,3,1,1,6,1,3,1]
	mark[1][4] = [1,3,1,5,2,1,3,1]
	mark[1][5] = [1,1,2,1,1]
	mark[1][6] = [7,1,1,1,1,1,7]
	mark[1][7] = [3,3]
	mark[1][8] = [1,2,3,1,1,3,1,1,2]
	mark[1][9] = [1,1,3,2,1,1]
	mark[1][10] = [4,1,4,2,1,2]
	mark[1][11] = [1,1,1,1,1,4,1,3]
	mark[1][12] = [2,1,1,1,2,5]
	mark[1][13] = [3,2,2,6,3,1]
	mark[1][14] = [1,9,1,1,2,1]
	mark[1][15] = [2,1,2,2,3,1]
	mark[1][16] = [3,1,1,1,1,5,1]
	mark[1][17] = [1,2,2,5]
	mark[1][18] = [7,1,2,1,1,1,3]
	mark[1][19] = [1,1,2,1,2,2,1]
	mark[1][20] = [1,3,1,4,5,1]
	mark[1][21] = [1,3,1,3,10,2]
	mark[1][22] = [1,3,1,1,6,6]
	mark[1][23] = [1,1,2,1,1,2]
	mark[1][24] = [7,2,1,2,5]
	
	return mark

def marks_rr():
	
	mark = [[[0 for i in xrange(9)] for j in xrange(size)] for k in xrange(size)]

	mark[1][0] = []
	mark[1][1] = []
	mark[1][2] = []
	mark[1][3] = [1,1]
	mark[1][4] = [1,1]
	mark[1][5] = [1,1]
	mark[1][6] = [1,1]
	mark[1][7] = [1,1]
	mark[1][8] = [1,1]
	mark[1][9] = [1,1]
#	mark[1][10] = []
#	mark[1][11] = []
#	mark[1][12] = []
#	mark[1][13] = []
#	mark[1][14] = []



	mark[0][0] = []
	mark[0][1] = [7]
	mark[0][2] = []
	mark[0][3] = []
	mark[0][4] = []
	mark[0][5] = [7]
	mark[0][6] = []
	mark[0][7] = []
	mark[0][8] = []
	mark[0][9] = []
#	mark[1][10] = []
#	mark[1][11] = []
#	mark[1][12] = []	
#	mark[1][13] = []		
#	mark[1][14] = []
		
	return mark

def marks_ttt():
	
	global size
	
	mark = [[[0 for i in xrange(9)] for j in xrange(size)] for k in xrange(size)]

	mark[1][0] = []
	mark[1][1] = []
	mark[1][2] = [5]
	mark[1][3] = [1,1]
	mark[1][4] = [5]
	mark[1][5] = []
	mark[1][6] = []
	mark[1][7] = []
	mark[1][8] = []
	mark[1][9] = []
	
	mark[0][0] = []
	mark[0][1] = []
	mark[0][2] = [3]
	mark[0][3] = [1,1]
	mark[0][4] = [1,1]
	mark[0][5] = [1,1]
	mark[0][6] = [3]
	mark[0][7] = []
	mark[0][8] = []
	mark[0][9] = []
		
	return mark

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
	
	global size
	
	#print "Before cross", len(solutions[j]),len(solutions[j+1])

	swap_point1 = random.randint(1,5)
	swap_point2 = random.randint(1,5)

	div = int(size*size/5)
	
	partial_1 = ""
	partial_2 = ""
	partial_3 = ""
	partial_4 = ""
	
	partial_11 = solutions[j][:div]
	partial_12 = solutions[j][div:2*div]
	partial_13 = solutions[j][2*div:3*div]
	partial_14 = solutions[j][3*div:4*div]
	partial_15 = solutions[j][4*div:5*div]
	partial_21 = solutions[j][:div]
	partial_22 = solutions[j][div:2*div]
	partial_23 = solutions[j][2*div:3*div]
	partial_24 = solutions[j][3*div:4*div]
	partial_25 = solutions[j][4*div:5*div]		

	if swap_point1 == 5:
		
		partial_1 = partial_11 + partial_12 + partial_13 + partial_14
		
		if swap_point2 == 5: partial_1 = partial_1 + partial_25
		if swap_point2 == 4: partial_1 = partial_1 + partial_24		
		if swap_point2 == 3: partial_1 = partial_1 + partial_23
		if swap_point2 == 2: partial_1 = partial_1 + partial_22
		if swap_point2 == 1: partial_1 = partial_1 + partial_21

	if swap_point1 == 4:
		
		partial_1 = partial_11 + partial_12 + partial_13
		
		if swap_point2 == 5: partial_1 = partial_1 + partial_25
		if swap_point2 == 4: partial_1 = partial_1 + partial_24		
		if swap_point2 == 3: partial_1 = partial_1 + partial_23
		if swap_point2 == 2: partial_1 = partial_1 + partial_22
		if swap_point2 == 1: partial_1 = partial_1 + partial_21

		partial_1 = partial_1 + partial_15

	if swap_point1 == 3:
		
		partial_1 = partial_11 + partial_12
		
		if swap_point2 == 5: partial_1 = partial_1 + partial_25
		if swap_point2 == 4: partial_1 = partial_1 + partial_24		
		if swap_point2 == 3: partial_1 = partial_1 + partial_23
		if swap_point2 == 2: partial_1 = partial_1 + partial_22
		if swap_point2 == 1: partial_1 = partial_1 + partial_21
		
		partial_1 = partial_1 + partial_14 + partial_15
		
	if swap_point1 == 2:
		
		partial_1 = partial_11
		
		if swap_point2 == 5: partial_1 = partial_1 + partial_25
		if swap_point2 == 4: partial_1 = partial_1 + partial_24		
		if swap_point2 == 3: partial_1 = partial_1 + partial_23
		if swap_point2 == 2: partial_1 = partial_1 + partial_22
		if swap_point2 == 1: partial_1 = partial_1 + partial_21
		
		partial_1 = partial_1 + partial_13 + partial_14 + partial_15
		
	if swap_point1 == 1:
				
		if swap_point2 == 5: partial_1 = partial_1 + partial_25
		if swap_point2 == 4: partial_1 = partial_1 + partial_24		
		if swap_point2 == 3: partial_1 = partial_1 + partial_23
		if swap_point2 == 2: partial_1 = partial_1 + partial_22
		if swap_point2 == 1: partial_1 = partial_1 + partial_21
		
		partial_1 = partial_1 + partial_12 + partial_13 + partial_14 + partial_15

# ******************************

	if swap_point2 == 5:
		
		partial_2 = partial_21 + partial_22 + partial_23 + partial_24
		
		if swap_point1 == 5: partial_2 = partial_2 + partial_15
		if swap_point1 == 4: partial_2 = partial_2 + partial_14		
		if swap_point1 == 3: partial_2 = partial_2 + partial_13
		if swap_point1 == 2: partial_2 = partial_2 + partial_12
		if swap_point1 == 1: partial_2 = partial_2 + partial_11

	if swap_point2 == 4:
		
		partial_2 = partial_21 + partial_22 + partial_23
		
		if swap_point1 == 5: partial_2 = partial_2 + partial_15
		if swap_point1 == 4: partial_2 = partial_2 + partial_14		
		if swap_point1 == 3: partial_2 = partial_2 + partial_13
		if swap_point1 == 2: partial_2 = partial_2 + partial_12
		if swap_point1 == 1: partial_2 = partial_2 + partial_11

		partial_2 = partial_2 + partial_25

	if swap_point2 == 3:
		
		partial_2 = partial_21 + partial_22
		
		if swap_point1 == 5: partial_2 = partial_2 + partial_15
		if swap_point1 == 4: partial_2 = partial_2 + partial_14		
		if swap_point1 == 3: partial_2 = partial_2 + partial_13
		if swap_point1 == 2: partial_2 = partial_2 + partial_12
		if swap_point1 == 1: partial_2 = partial_2 + partial_11
		
		partial_2 = partial_2 + partial_24 + partial_25
		
	if swap_point2 == 2:
		
		partial_2 = partial_21
		
		if swap_point1 == 5: partial_2 = partial_2 + partial_15
		if swap_point1 == 4: partial_2 = partial_2 + partial_14		
		if swap_point1 == 3: partial_2 = partial_2 + partial_13
		if swap_point1 == 2: partial_2 = partial_2 + partial_12
		if swap_point1 == 1: partial_2 = partial_2 + partial_11
		
		partial_2 = partial_2 + partial_23 + partial_24 + partial_25
		
	if swap_point2 == 1:
				
		if swap_point1 == 5: partial_2 = partial_2 + partial_15
		if swap_point1 == 4: partial_2 = partial_2 + partial_14		
		if swap_point1 == 3: partial_2 = partial_2 + partial_13
		if swap_point1 == 2: partial_2 = partial_2 + partial_12
		if swap_point1 == 1: partial_2 = partial_2 + partial_11
		
		partial_2 = partial_2 + partial_22 + partial_23 + partial_24 + partial_25

	solutions[j] = partial_1
	solutions[j+1] = partial_2
	
	#print "After cross ", len(solutions[j]),len(solutions[j+1])

	return solutions
	
def mutation(solutions,j):
	global mut_rate
	k = list(solutions[j])
	l = list(solutions[j+1])
	for i in xrange(len(k)):
		toss = random.randint(0,1000)
		if toss < mut_rate:
			#print "mutate"
			if k[i] == "1":
				k[i] = "0"
			else:
				k[i] = "1"
		toss = random.randint(0,1000)
		if toss < mut_rate:
			#print "mutate"
			if l[i] == "1":
				l[i] = "0"
			else:
				l[i] = "1"
	solutions[j] = ''.join(k)
	solutions[j+1] = ''.join(l)
	return solutions
		
color1 = (255,0,0)
color2 = (0,255,0)
size = 25

population_size = 200	
solutions = []
newsolutions = []
fitness_record = []
selections = ["",""]
Done = False
generation = 1
mut_rate = 10
initial_pop(solutions)
constraints = marks()
mul_f = 1



#plt.plot(fitness_record)
#plt.show()
#print fitness_record
first = True
running = True
timer_event = pygame.USEREVENT + 1
pygame.time.set_timer(timer_event, 1)
screen.fill(background_colour)
while running:
	event = pygame.event.wait()
	if event.type == pygame.QUIT:
		raise StopIteration
		
	if not(Done):
		screen.fill(background_colour)
		newsolutions = []
		
		generation += 1
		
		fitness_f = fitness(solutions)

		for i in xrange(len(fitness_f)):
			if fitness_f[i] == -1:
				winner = min(fitness_f)
				win = decode(solutions[fitness_f.index(winner)])
				print win
				print "Done"
				
# ***********************************************

				for hh in xrange(size):
					for ii in xrange(size):
						x = ii*15 + 15
						y = hh*15 + 15
						w = 15
						h = 15
						Rect = (x,y,w,h)
						wid = 1
						if win[ii][hh][0] == "1": wid = 0
						pygame.draw.rect(screen, (0,0,0), Rect, wid) 

# ***********************************************

				Done = True
		if not(Done):
			i = 0
			winner = max(fitness_f)
			win = decode(solutions[fitness_f.index(winner)])
			
			#print "************************"
			#print win
			#print "************************"
			
# ***********************************************

			for hh in xrange(size):
				for ii in xrange(size):
					x = ii*15 + 15
					y = hh*15 + 15
					w = 15
					h = 15
					Rect = (x,y,w,h)
					wid = 1
					if win[ii][hh][0] == "1": wid = 0
					pygame.draw.rect(screen, (0,0,0), Rect, wid) 


# ***********************************************
			
			


			while i < (population_size):
				selections = select_genes2(fitness_f,solutions)
				newsolutions.append(selections[0])
				newsolutions.append(selections[1])
				newsolutions = crossover(newsolutions,i)
				newsolutions = mutation(newsolutions,i)
				i = i + 2
			solutions = newsolutions

		fitness_record.append(winner)




		#print generation

		pygame.display.flip()
	


