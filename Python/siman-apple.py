from __future__ import division
import pygame
from pygame import gfxdraw
import matplotlib.pyplot as plt
import math
import random
import sys
from copy import deepcopy


def cost(sol):

	carry = 1000
	tax = 1
	apples = 3000
	total_d = 0
	fitness_value = 100
	for d in sol: 
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

		try:
			fitness_value = 3000/apples
		except:
			fitness_value = 100
			
		if total_d > 1000:
			fitness_value = 100

		if total_d < 1000:
			fitness_value = 100

	return fitness_value

def gensol():
	global howMany
	
	solution = []
	
	while (not (len(solution) == howMany)) or not (sum(solution) == 1000):
		
		solution = []

		distance = random.randint(0,1000)
		solution.append(distance)
		
		while sum(solution) < 1000:
			distance = random.randint(0,1000)
			solution.append(distance)
	
	return solution
	
def neighbor(sol):
	global howMany
	
	SD = 50

	toss = random.randint(1,3)
	dum = []
	fact = 1
	summ = 6666
	while not sum(dum) == 1000:
		dum = []
		for i in xrange(howMany):
			dum.append(abs(int(random.gauss(sol[i],SD))))
	
	sol = deepcopy(dum)
#	raw_input()

	return sol
	
def acceptance_probability(ocost,ncost,temp):
	ap = math.exp(-(ncost - ocost)/(temp))
	return ap



howMany = 5

solution = gensol()

old_cost = cost(solution)
T = 1.0
T = 0.5
T_min = 0.0000001
alpha = 0.98

resultsT = []
resultsC = []

while T > T_min:
	
	i = 1
	print T,solution, 3000/cost(solution)
	while i < 100:
		#new_solution = neighbor(solution)

		new_solution = gensol()
		new_solution = neighbor(solution)
		new_cost = cost(new_solution)
		if new_cost <= old_cost:
			old_cost = new_cost
			solution = new_solution
		else:
			ap = acceptance_probability(old_cost, new_cost, T)
			#print ap
			r = random.uniform(0,1)
			if ap > r:
				solution = new_solution
				old_cost = new_cost
		i += 1
	
	resultsT.append(T)
	resultsC.append(old_cost)
	T = T * alpha
	
else:
	running = False
	print "Solution = ", solution,3000/old_cost
		

plt.plot(resultsT)
plt.plot(resultsC)
plt.show()
	

