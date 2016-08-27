from __future__ import division
import math
import random
import sys
#import numpy as np
#import matplotlib.pyplot as plt


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
	
def fitness(solutions,NodesH,NodesO,hiddenL,outL,inode):
	fitness_function = []

	global constraints,size
	global fitness_record
	for i in xrange(len(solutions)):
	
		fitness_function.append(0)

		net_input_H = []
		for j in xrange(len(hiddenL)):
			net_input_H.append(netinput(inode,HLW,j,0))
		#Get the activation of each hidden node
		activation_H = []	
		for j in xrange(len(hiddenL)):
			aa = activation(net_input_H[j])
			activation_H.append(aa)

		#print activation_H
			
		# **** Output Layer ****

		# Get net input of each hidden node
		net_input_O = []
		for j in xrange(len(outL)):
			net_input_O.append(netinput(activation_H,OLW,j,0))
		#Get the activation of each hidden node
		activation_O = []	
		for j in xrange(len(outL)):
			activation_O.append(activation(net_input_O[j]))
			
		#**** Check result ****
		testo = []
		for kk in activation_O:
			r = int(round(kk,1))
			testo.append(r)
			
		#print "Check results"
		#print testo
		#print activation_O
		#print Required_output
		
		error_function = 0
		
		for t in xrange(len(Required_output)):
			error_function += 0.5 * (Required_output[t] - activation_O[t])**2

		try:

		except:
			fit = -1
		fitness_function[i] = fit
	fitness_record.append(max(fitness_function))
	#print "max",max(fitness_function)
	return fitness_function

	
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
	
def select_genes3(fitness_f,solutions):
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
	
def runGA(NodesH,NodesO,hiddenL,outL,inode):	
	size = len(NodesH)+len(NodesO)
	population_size = 200	
	solutions = []
	newsolutions = []
	fitness_record = []
	selections = ["",""]
	Done = False
	generation = 1
	mut_rate = 10

	size = LayerNodes
	initial_pop(solutions)

	mul_f = 1

	first = True

	newsolutions = []
	
	while not(Done):

		generation += 1

		fitness_f = fitness(solutions,NodesH,NodesO,hiddenL,outL)

		for i in xrange(len(fitness_f)):
			if fitness_f[i] == -1:
				winner = min(fitness_f)
				win = decode(solutions[fitness_f.index(winner)])
				print win
				print "Done"
				Done = True
		if not(Done):
			i = 0
			winner = max(fitness_f)
			win = decode(solutions[fitness_f.index(winner)])

			while i < (population_size):
				selections = select_genes2(fitness_f,solutions)
				newsolutions.append(selections[0])
				newsolutions.append(selections[1])
				newsolutions = crossover(newsolutions,i)
				newsolutions = mutation(newsolutions,i)
				i = i + 2
			solutions = newsolutions

		fitness_record.append(winner)

