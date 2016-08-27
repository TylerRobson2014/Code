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
	

def still_to_clean(board,dimh,dimw):
	result = False
	for y in xrange(dimh):
		for x in xrange(dimw):
			if board[x][y] == 'd':
				result = True
	return result
	
def next_move(posr, posc, dimh, dimw, board):
	solution = deepcopy(gensol(board,dimh,dimw))
	old_cost = cost(deepcopy(solution),board,dimw,dimh,posr,posc)

	T = 1.0
	T_min = 0.01
	alpha = 0.98
	cool = True

	while T > T_min and cool:
		
		i = 1
		while i < 100:
			#new_solution = deepcopy(neighbor(deepcopy(solution)))
			new_solution = deepcopy(neighborT(board,dimh,dimw))
			new_cost = cost(deepcopy(new_solution),board,dimw,dimh,posr,posc)
			if new_cost <= old_cost:
				old_cost = new_cost
				solution = deepcopy(new_solution)
			else:
				#print "ap",new_cost,old_cost
				#raw_input()
				ap = acceptance_probability(old_cost, new_cost, T)
				r = random.uniform(0,1)
				if ap > r:
					solution = deepcopy(new_solution)
					old_cost = new_cost
			i += 1
			#print solution
		T = T * alpha
		#print "w", posr,posc
		#print "sol",solution
		#print "Temperature = ",T
		#print "Cost = ",old_cost
	#	raw_input()
	else:
		running = False
		print "where",posr,posc
		print "End ",solution
		drawLines(solution)
		#raw_input()

#	move = "NONE"
#	factor = 0.1
	move = decideMove(posr,posc,board,solution)
	return move	


def drawLines(solution):
	global fact,pointlist,raddii
	for s in xrange(len(solution)-1):
		a = solution[s][1]*fact + fact + fact/2
		b = solution[s][0]*fact + fact + fact/2
		c = solution[s+1][1]*fact + fact + fact/2
		d = solution[s+1][0]*fact + fact + fact/2
		pointlist.append( [(a,b),(c,d)] )
		radii.append([a,b])
		radii.append([c,d])

def decideMove(r,c,board,sol):
#	oldd2 = 99999
#	for s in sol:
#		nr = s[0]
#		nc = s[1]
#		d2 = (r-nr)**2 + (c-nc)**2
#		if d2 < oldd2:
#			oldd2 = d2
#			(x,y) = (nr,nc)
#	(nr,nc) = (x,y)
	(nr,nc) = (sol[0][0],sol[0][1])
	#print "check", r,c,nr,nc
	
	if (nr,nc) == (r,c):
		m = "CLEAN"
		
	if nr > r and nc == c:
		m = "DOWN"
	if nr < r and nc == c:
		m = "UP"
		
	if nr < r and not nc == c:
		m = "UP"
	if nr > r and not nc == c:
		m = "DOWN"
		
	if nc > c and nr == r:
		m = "RIGHT"
	if nc < c and nr == r:
		m = "LEFT"

	if nc > c and not nr == r:
		m = "RIGHT"
	if nc < c and not nr == r:
		m = "LEFT"

	return m
	
def checkNeighbors(r,c,board,dimh,dimw):
	m = 'NONE'
	old_d2 = 9999
	(nr,nc) = (r,c)
	dvr1 = dimh/2
	dvr2 = dimh - dvr1
	dvc1 = dimw/2
	dvc2 = dimw - dvc1
	
	if r < dvr1 and c < dvc1:
		rstart = 0
		rend = dvr1
		cstart = 0
		cend = dvc1
	if r >= dvr1 and c < dvc1:
		rstart = dvr1
		rend = dimh
		cstart = 0
		cend = 	dvc1
		
	if r < dvr1 and c >= dvc1:
		rstart = 0
		rend = dvr1
		cstart = dvc1
		cend = dimw
	if r >= dvr1 and c >= dvc1:
		rstart = dvr1
		rend = dimh
		cstart = dvc1
		cend = 	dimw
		
	count = 0
	for i in xrange(rstart,rend):
		for j in xrange(cstart,cend):
			if board[i][j] == 'd':
				count += 1
	if count == 0:
		for i in xrange(0,dimh):
			for j in xrange(0,dimw):
				if board[i][j] == 'd':
					d2 = (i-r)**2 + (j-c)**2
					if d2 < old_d2:
						old_d2 = d2
						(nr,nc) = (i,j)
	else:
		for i in xrange(rstart,rend):
			for j in xrange(cstart,cend):
				if board[i][j] == 'd':
					d2 = (i-r)**2 + (j-c)**2
					if d2 < old_d2:
						old_d2 = d2
						(nr,nc) = (i,j)		
	if (nr,nc) == (r,c):
		m = "CLEAN"
		
	if nr > r and nc == c:
		m = "DOWN"
	if nr < r and nc == c:
		m = "UP"
		
	if nr < r and not nc == c:
		m = "UP"
	if nr > r and not nc == c:
		m = "DOWN"
		
	if nc > c and nr == r:
		m = "RIGHT"
	if nc < c and nr == r:
		m = "LEFT"

	if nc > c and not nr == r:
		m = "RIGHT"
	if nc < c and not nr == r:
		m = "LEFT"

	return m

def cost(sol,board,dimw,dimh,rpos,cpos):
	d2 = 0
	startr = rpos
	startc = cpos
	for s in sol:
		endr = s[0]
		endc = s[1]
		d2 = d2 + math.sqrt((endr-startr)**2 + (endc-startc)**2)
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
	solution = listD
	return solution
	
def neighbor(sol):
	if len(sol) > 2:
		pick = random.sample(sol,2)
		index1 = sol.index(pick[0])
		index2 = sol.index(pick[1])
		(sol[index1],sol[index2]) = (sol[index2],sol[index1])
	return sol

def neighborT(board,dimh,dimw):
	listD = []
	for i in xrange(0,dimh):
		for j in xrange(0,dimw):
			if board[i][j] == 'd':
				listD.append([i,j])
	solution = deepcopy(listD)
	solution = random.sample(solution,len(solution))
	return solution
	
def acceptance_probability(ocost,ncost,temp):
	ap = math.exp(-(ncost - ocost)/(temp))
	return ap

def genBoard():
	board = [['-' for j in xrange(dim[0])] for k in xrange(dim[1])]
	pos = [random.randint(0,dim[0]-1),random.randint(0,dim[1]-1)]
	board[pos[0]][pos[1]] = 'b'
	for y in xrange(dim[1]):
		for x in xrange(dim[0]):
			toss = random.randint(0,3)
			if toss == 1:
				fill = 'd'
				board[x][y] = fill
	return (board,pos)

def genBoardT():
	board = [['-' for j in xrange(dim[0])] for k in xrange(dim[1])]
	pos = [3,1]
	board[pos[0]][pos[1]] = 'b'
	for y in xrange(dim[1]):
		for x in xrange(dim[0]):
			if x > 0 and y > 0:
				if x % 2 and y % 2:
					fill = 'd'
					board[x][y] = fill
	return (board,pos)

color1 = (255,0,0)
color2 = (0,255,0)

size = 50
fact = width/(1.2*size)

dim = [size,size]
dimh = dim[0]
dimw = dim[1]

(board,pos) = genBoardT()

solution = []
pointlist = []
radii = []
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
	count = 0
	while still_to_clean(board,dim[0],dim[1]):
		count = count + 1
		pointlist = []
		radii = []
		move = next_move(pos[0], pos[1], dim[0], dim[1], board)
		
		print move
		#raw_input()
		if move == 'CLEAN':
			(pos[0],pos[1]) = (pos[0],pos[1])
			board[pos[0]][pos[1]] = 'b'
		if move == 'LEFT':
			board[pos[0]][pos[1]] = '-'
			(pos[0],pos[1]) = (pos[0],pos[1]-1)
			if board[pos[0]][pos[1]] == '-':
				board[pos[0]][pos[1]] = 'b'
		if move == 'RIGHT':
			board[pos[0]][pos[1]] = '-'
			(pos[0],pos[1]) = (pos[0],pos[1]+1)
			if board[pos[0]][pos[1]] == '-':
				board[pos[0]][pos[1]] = 'b'
		if move == 'UP':
			board[pos[0]][pos[1]] = '-'
			(pos[0],pos[1]) = (pos[0]-1,pos[1])
			if board[pos[0]][pos[1]] == '-':
				board[pos[0]][pos[1]] = 'b'
		if move == 'DOWN':
			board[pos[0]][pos[1]] = '-'
			(pos[0],pos[1]) = (pos[0]+1,pos[1])
			if board[pos[0]][pos[1]] == '-':
				board[pos[0]][pos[1]] = 'b'

	
# ***********************************************

		for hh in xrange(size):
			for ii in xrange(size):
				x = hh*fact + fact
				y = ii*fact + fact
				w = fact
				h = fact
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
				x = hh*fact + fact
				y = ii*fact + fact
				w = fact
				h = fact
				wid = 1
				Rect = (x,y,w,h)
				wid = 1
				pygame.draw.rect(screen, (0,0,0), Rect, wid)
		
		#raw_input()			
		for p in pointlist:
			pygame.draw.lines(screen, (0,255,255), False, p, 10)
		#print len(radii)
		#raw_input()
		for r in radii:
			pygame.draw.circle(screen, (0,255,255), (int(r[0]),int(r[1])), 10, 10)


	# ***********************************************

			
		pygame.display.flip()
	

