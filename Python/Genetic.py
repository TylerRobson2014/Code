from __future__ import division
import pygame
from pygame import gfxdraw
import math
import random
import sys

dictionary_numtobin = {"1":"0001","2":"0010","3":"0011","4":"0100","5":"0101","6":"0110","7":"0111","8":"1000","9":"1001","+":"1010","-":"1011","*":"1100","/":"1101"}
dictionary_bintonum = {"0001":"1","0010":"2","0011":"3","0100":"4","0101":"5","0110":"6","0111":"7","1000":"8","1001":"9","1010":"+","1011":"-","1100":"*","1101":"/"}

population_size = 50
number_operations = 7
target = 11

def initial_pop(solutions):
	
	global dictionary_numtobin
	global population_size
	global number_operations
	
	for j in xrange(population_size):
		gene_string = ""
		for i in xrange(number_operations):
			gene_string += dictionary_numtobin[random.choice(dictionary_numtobin.keys())]
		solutions.append(gene_string)
			
def decode(gene_string):
	global dictionary_bintonum
	result = ""
	i = 0
	while i <= len(gene_string):
		string = gene_string[i:i+4]
		try:
			conversion = dictionary_bintonum[string]
		except:
			e = sys.exc_info()[0]
		else:
			result += conversion
		i = i + 4
	return result
	
	
def evaluate(solution):
	global number_operations
	index = 0
	operation = ""
	expression = ""
	next_number = True
	count_numbers = 0
	count_operators = 0
	look_for_operator = False
	look_for_number = True
	for index in xrange(len(solution)):
		if solution[index] in ["1","2","3","4","5","6","7","8","9"] and look_for_number:
			look_for_operator = True
			look_for_number = False
			count_numbers += 1
			expression = expression + operation + solution[index]
		elif solution[index] in ["+","-","/","*"] and look_for_operator:
			look_for_operator = False
			look_for_number = True
			operation = solution[index]

	if count_numbers >=2 and (number_operations+1)/2:
		return expression
	else:
		return 9999

def fitness(solutions):
	fitness_function = []
	global target
	for i in xrange(len(solutions)):
		fitness_function.append(0)
		converted = decode(solutions[i])
		expression = evaluate(converted)
		if expression == 9999:
			evaluated = 100
		else:
			evaluated = eval(expression)
			#print expression,"=",evaluated
		try:
			fitness_value = 1/abs(target - evaluated)
		except:
			fitness_value = -1

		fitness_function[i] = fitness_value
	return fitness_function

def sort(fitness,res,depth):
	depth += 1
	if depth < 100:
		minimum = 1000000000000
		for i in range(len(fitness)):
			xi = fitness[i]
			if xi < minimum:
				minimum = xi
				topop = i
		try:
			res.append(fitness[topop])
			fitness.pop(topop)
		except:
			e = sys.exc_info()[0]
		if len(fitness) > 0:
			sort(fitness,res,depth)

def select_genese(fitness_f,solutions):
	res = []
	pie = []
	dummy = []
	for i in xrange(len(fitness_f)):
		dummy.append(fitness_f[i])
	selections = ["",""]
	sort(dummy,res,0)
	#print res[0]
	for i in xrange(len(fitness_f)):
		fitness_f[i] = fitness_f[i]/res[0]

		for j in xrange(int(fitness_f[i])):
			pie.append(i)
	selections[0] = solutions[random.choice(pie)]
	selections[1] = solutions[random.choice(pie)]
	return selections

def crossover(solutions,j):
	global number_operations
	swap_point = random.randint(0,number_operations*4)
	partial_1 = ""
	partial_2 = ""
	if swap_point > 0 and swap_point < number_operations*4:
		for i in xrange(swap_point):
			partial_1 += solutions[j][i]
		for i in xrange(swap_point):
			partial_2 += solutions[j+1][i]
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
	global number_operations
	global mut_rate
	k = list(solutions[j])
	l = list(solutions[j+1])
	for i in xrange(len(k)):
		toss = random.randint(0,1000)
		if toss < 10:
			if k[i] == "1":
				k[i] = "0"
			else:
				k[i] = "1"
		toss = random.randint(0,1000)
		if toss < 10:
			if l[i] == "1":
				l[i] = "0"
			else:
				l[i] = "1"
	solutions[j] = ''.join(k)
	solutions[j+1] = ''.join(l)
	return solutions
		
	
solutions = []
newsolutions = []
selections = ["",""]
Done = False
generation = 1
mut_rate = 100
initial_pop(solutions)
while not(Done):
	print "generation = ",generation
	generation += 1
	fitness_f = fitness(solutions)
	for i in xrange(len(fitness_f)):
		if fitness_f[i] == -1: 
			print "Done"
			print solutions[i]
			print evaluate(decode(solutions[i]))
			Done = True
	if not(Done):
		i = 0
		while i <= (population_size):
			selections = select_genese(fitness_f,solutions)
			newsolutions.append(selections[0])
			newsolutions.append(selections[1])
			newsolutions = crossover(newsolutions,i)
			newsolutions = mutation(newsolutions,i)
			i = i + 2
		solutions = newsolutions
		
#	print newsolutions
	
#print solutions

