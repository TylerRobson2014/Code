from __future__ import division

import math
import random
import sys
from copy import deepcopy
#import numpy as np
#import matplotlib.pyplot as plt

def initial_pop(solutions):
	
	global population_size
	global w,x,y
	
	for j in xrange(population_size):
		global number_stops
		gene_string = ''
		string = ''
		dist = 0
		#print "pop"
		for i in xrange(number_stops):
			string = ''
			newdist = random.randint(0,1000)
			if dist + newdist <= 1000:
				dist += newdist
				string += bin(newdist)[2:]
				#print "dist1",dist
			if i == number_stops - 2:
				if dist < 1000:
					newdist = 1000 - dist
					dist = dist + newdist
					#print "dist2",dist
					string += bin(newdist)[2:]
			while len(string) < len(bin(1000)[2:]):
				string = '0' + string
			#print string
			gene_string += string
		solutions.append(gene_string)
			
def decode(gene_string):
	result = []
	i = 0
	#print gene_string
	while i < len(gene_string):
		string = gene_string[i:i+10]
		#print string
		#raw_input()
		conversion = int(string,2)
		#print conversion
		#raw_input()
		result.append(conversion)
		i = i + 10
	return result
	
def fitness(solutions):
	fitness_function = []
	converted = []
	global fitness_record
	carry = 1000
	tax = 1
	for i in xrange(len(solutions)):
		apples = 3000
		fitness_function.append(0)
		converted = decode(solutions[i])
		distances = converted
		#print distances
		#raw_input()
		total_d = 0
		for d in distances:
			total_d += d
			#print "apples 1",apples
			oldapples = apples
			transfer = True
			storedapples = 0
			while transfer:
				if oldapples >= carry:
					oldapples = oldapples - carry
					storedapples = storedapples + carry - tax * d
				elif oldapples > 0 and oldapples >= tax * d:
					storedapples = storedapples + oldapples - tax * d
					oldapples = 0
				else:
					storedapples = 0
					transfer = False
				if oldapples <= 0:
					transfer = False
			apples = storedapples
			#print "apples", apples
			#raw_input()
		try:
			fitness_value = apples
		except:
			fitness_value = 0
		if total_d > 1000:
			fitness_value = 0
		if total_d < 1000:
			fitness_value = 0
		fitness_function[i] = fitness_value
	fitness_record.append(max(fitness_function))
	#print "fitness",fitness_function
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
		rand_num = int(random.uniform(0,sum_fit))
		sum_fit = 0
		flag = 0
		for i in xrange(len(fitness_f)):
			sum_fit += dummy[i][0]
			if dummy[i][0] > 800:
				print sum_fit,rand_num,dummy[i][0],decode(dummy[i][1])
				#raw_input()
			if sum_fit > rand_num and flag == 0:
				selections.append(dummy[i][1])
				flag = 1
	return selections	

def crossover(solutions,j):
	
	global number_stops,size
	
	#print "Before cross", solutions[j],solutions[j+1]

	swap_point1 = random.randint(1,number_stops)
	swap_point2 = random.randint(1,number_stops)
	
	div = int(size/number_stops)
	
	partial_1 = ""
	partial_2 = ""
	
	partial_11 = solutions[j][:div]
	partial_12 = solutions[j][div:2*div]
	partial_13 = solutions[j][2*div:3*div]
	partial_21 = solutions[j+1][:div]
	partial_22 = solutions[j+1][div:2*div]
	partial_23 = solutions[j+1][2*div:3*div]
		
	if swap_point1 == 3:
		
		partial_1 = partial_11 + partial_12
		
		if swap_point2 == 3: partial_1 = partial_1 + partial_23
		if swap_point2 == 2: partial_1 = partial_1 + partial_22
		if swap_point2 == 1: partial_1 = partial_1 + partial_21
		
	if swap_point1 == 2:
		
		partial_1 = partial_11
		
		if swap_point2 == 3: partial_1 = partial_1 + partial_23
		if swap_point2 == 2: partial_1 = partial_1 + partial_22
		if swap_point2 == 1: partial_1 = partial_1 + partial_21
		
		partial_1 = partial_1 + partial_13
		
	if swap_point1 == 1:
				
		if swap_point2 == 3: partial_1 = partial_1 + partial_23
		if swap_point2 == 2: partial_1 = partial_1 + partial_22
		if swap_point2 == 1: partial_1 = partial_1 + partial_21
		
		partial_1 = partial_1 + partial_12 + partial_13

# ******************************

	if swap_point2 == 3:
		
		partial_2 = partial_21 + partial_22
		
		if swap_point1 == 3: partial_2 = partial_2 + partial_13
		if swap_point1 == 2: partial_2 = partial_2 + partial_12
		if swap_point1 == 1: partial_2 = partial_2 + partial_11
		
	if swap_point2 == 2:
		
		partial_2 = partial_21
		
		if swap_point1 == 3: partial_2 = partial_2 + partial_13
		if swap_point1 == 2: partial_2 = partial_2 + partial_12
		if swap_point1 == 1: partial_2 = partial_2 + partial_11
		
		partial_2 = partial_2 + partial_23
		
	if swap_point2 == 1:
				
		if swap_point1 == 3: partial_2 = partial_2 + partial_13
		if swap_point1 == 2: partial_2 = partial_2 + partial_12
		if swap_point1 == 1: partial_2 = partial_2 + partial_11
		
		partial_2 = partial_2 + partial_22 + partial_23

	solutions[j] = partial_1
	solutions[j+1] = partial_2
	
	#print "After cross ", solutions[j],solutions[j+1]
	#raw_input()

	return solutions


def oldcrossover(solutions,j):
	
	global size,number_stops,repeat
	
	#print "Before cross", solutions[j],solutions[j+1]
	#print "solutios",solutions

	#number_to_swap = random.randint(25,len(solutions[j])-1)
	number_to_swap = 30
	
	swap_point1 = []
	for i in xrange(number_to_swap):
		swap_point1.append(random.randint(1,len(solutions[j])-1))
	swap_point1 = list(set(swap_point1))
	swap_point2 = []
	for i in xrange(number_to_swap):
		swap_point2.append(random.randint(1,len(solutions[j])-1))
	swap_point2 = list(set(swap_point2))
	dummy1j = list(deepcopy(solutions[j]))
	dummy2j1 = list(deepcopy(solutions[j+1]))
	dummy3j = list(deepcopy(solutions[j]))
	dummy4j1 = list(deepcopy(solutions[j+1]))

	for i in swap_point1:
		dummy4j1[i] = dummy1j[i]
	for i in swap_point2:
		dummy3j[i] = dummy2j1[i]
	
	solutions[j] = "".join(dummy3j)
	solutions[j+1] = "".join(dummy4j1)
	#print "After cross ", solutions[j],solutions[j+1]
	#print "solutios",solutions
	
	#raw_input()

	return solutions
	
def mutation(solutions,j):
	global mut_rate
	maxmut = 10000
	k = list(solutions[j])
	l = list(solutions[j+1])
	for i in xrange(len(k)):
		toss = random.randint(0,maxmut)
		if toss < mut_rate:
#			print "mutate"
			if k[i] == "1":
				k[i] = "0"
			else:
				k[i] = "1"
		toss = random.randint(0,maxmut)
		if toss < mut_rate:
#			print "mutate"
			if l[i] == "1":
				l[i] = "0"
			else:
				l[i] = "1"
	solutions[j] = ''.join(k)
	solutions[j+1] = ''.join(l)
	return solutions

population_size = 50
number_stops = 3
size = number_stops * len(bin(1000)[2:])
solutions = []
newsolutions = []
fitness_record = []
selections = ["",""]
Done = False
generation = 1
mut_rate = 10
repeat = 2
initial_pop(solutions)
mul_f = 1

first = True
#print fitness_f
count  = 0
old_max = 0
mem_win = 0
mem_winner = 0
while not(count > 1000000000):
	
	generation += 1
	newsolutions = []
	
	fitness_f = fitness(solutions)
	i = 0
	count += 1
	#while mut_rate > 5:
	#	mut_rate = int(500*(1/count)**(0.05))
	#while repeat > 5:
	#	repeat = int(50*(1/count)**(0.05))
	#print mut_rate,repeat

	winner = max(fitness_f)
	win = decode(solutions[fitness_f.index(winner)])
	if winner > old_max:
		print "winner",generation,winner
		top = winner
		print win
		old_max = winner
	while i < (population_size):
		selections = []
		selections = select_genes2(fitness_f,solutions)
		#print len(selections), len(solutions)
		#print "selections",selections[0],selections[1]
		newsolutions.append(selections[0])
		newsolutions.append(selections[1])
		if random.randint(1,10) < 7:
			newsolutions = crossover(newsolutions,i)
			#print "cross"
		newsolutions = mutation(newsolutions,i)
		#print count
		i = i + 2
	solutions = newsolutions
	#if not(winner == mem_winner or win == mem_win):
	#	print "*****************************************"
	#	print top,winner,win
	mem_winner = winner
	mem_win = win

	fitness_record.append(winner)
#print "winners", fitness_record


