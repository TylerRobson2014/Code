from __future__ import division

import math
import random
import sys
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
					storedapples = -100
					transfer = False
				if oldapples <= 0:
					transfer = False
			apples = storedapples
			#print "apples", apples
			#raw_input()
		try:
			fitness_value = apples
		except:
			fitness_value = 30000
		if total_d > 1000:
			fitness_value = -100
		if total_d < 1000:
			fitness_value = -100
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
	
	global size,number_stops,repeat
	
	#print "Before cross", len(solutions[j]),len(solutions[j+1])
	#print "solutios",solutions
	for i in xrange(repeat):
		
		choose = random.randint(1,2)

		swap_point = random.randint(1,number_stops)

		div = int(size/number_stops)*swap_point
		
		if choose == 1:
			
			partial_11 = solutions[j][:div]
			partial_12 = solutions[j][div:]

			partial_21 = solutions[j+1][:div]
			partial_22 = solutions[j+1][div:]
			

			solutions[j] = partial_11 + partial_22
			solutions[j+1] = partial_21 + partial_12

		else:

			partial_11 = solutions[j][:div]
			partial_12 = solutions[j][div:]

			partial_21 = solutions[j+1][:div]
			partial_22 = solutions[j+1][div:]
			

			solutions[j] = partial_12 + partial_21
			solutions[j+1] = partial_22 + partial_11
	
	#print "After cross ", len(solutions[j]),len(solutions[j+1])
	print "solutios",solutions
	
	raw_input()

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

population_size = 150
number_stops = 3
size = number_stops * len(bin(1000)[2:])
solutions = []
newsolutions = []
fitness_record = []
selections = ["",""]
Done = False
generation = 1
mut_rate = 100
repeat = 2
initial_pop(solutions)
mul_f = 1

first = True
#print fitness_f
count  = 0
old_max = 0
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
		print "winner",winner
		print win
		old_max = winner
	while i < (population_size):
		selections = select_genes2(fitness_f,solutions)
		#print "selections",selections[0],selections[1]
		newsolutions.append(selections[0])
		newsolutions.append(selections[1])
		newsolutions = crossover(newsolutions,i)
		newsolutions = mutation(newsolutions,i)
		i = i + 2
	solutions = newsolutions

	fitness_record.append(winner)
#print "winners", fitness_record


