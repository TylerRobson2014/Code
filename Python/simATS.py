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
	
def cost(sol,board,dimw,dimh,rpos,cpos):
	d2 = 0
	startr = rpos
	startc = cpos
	for s in sol:
		endr = s[0]
		endc = s[1]
		d2 = d2 + (endr-startr)**2 + (endc-startc)**2
		startr = endr
		startc = endc
	fitness_value = d2
	return fitness_value

def gensol(board,dimh,dimw):
	listD = []
	for i in xrange(0,dimh):
		for j in xrange(0,dimw):
			if board[i][j] == 'd':
				listD.append([i,j])
	solution = deepcopy(listD)
	return solution
	
def neighbor(sol):
	sol2 = random.sample(sol,len(sol))
	return deepcopy(sol2)
	
def acceptance_probability(ocost,ncost,temp):
	ap = math.exp(-(ncost - ocost)/(temp))
	return ap
	
color1 = (255,0,0)
color2 = (0,255,0)

size = 30

dim = [size,size]
dimh = dim[0]
dimw = dim[1]
board = [['-' for j in xrange(dim[0])] for k in xrange(dim[1])]
pos = [random.randint(0,dim[0]-1),random.randint(0,dim[1]-1)]
board[pos[0]][pos[1]] = 'b'
for y in xrange(dim[1]):
	for x in xrange(dim[0]):
		toss = random.randint(0,3)
		if toss == 1:
			fill = 'd'
			board[x][y] = fill


solution = gensol(board,dimh,dimw)

old_cost = cost(solution,board,dimw,dimh,pos[0],pos[1])

T = 1.0
T = 0.1
T_min = 0.0001
alpha = 0.99

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
	
	if T > T_min:
		
		i = 1
		while i < 100:
			new_solution = neighbor(solution)
	
			new_cost = cost(new_solution,board,dimw,dimh,pos[0],pos[1])
			#print "new cost",new_cost
			#print "test sol",new_solution
			if new_cost <= old_cost:
				old_cost = new_cost
				solution = new_solution
			else:
				ap = acceptance_probability(old_cost, new_cost, T)
				r = random.uniform(0,1)
				if ap > r:
					solution = new_solution
					old_cost = new_cost
			i += 1
		T = T * alpha
		print "Temperature = ",T
		print "Cost = ",old_cost
		#print pos
		#print solution
#		raw_input()
	else:
		running = False
		print "End ",solution

# ***********************************************

	for hh in xrange(size):
		for ii in xrange(size):
			x = hh*15 + 15
			y = ii*15 + 15
			w = 15
			h = 15
			wid = 1
			Rect = (x,y,w,h)
			if board[ii][hh] == "-":
				wid = 0
				pygame.draw.rect(screen, (255,255,0), Rect, wid)
			if board[ii][hh] == "d":
				wid = 0
				pygame.draw.rect(screen, (0,0,0), Rect, wid) 
			if board[ii][hh] == "b":
				wid = 0
				pygame.draw.rect(screen, (255,0,0), Rect, wid) 

	for hh in xrange(size):
		for ii in xrange(size):
			x = hh*15 + 15
			y = ii*15 + 15
			w = 15
			h = 15
			wid = 1
			Rect = (x,y,w,h)
			wid = 1
			pygame.draw.rect(screen, (0,0,0), Rect, wid)
			
# ***********************************************

		
	pygame.display.flip()
	

