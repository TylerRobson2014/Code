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
	
def next_move(posr, posc, dimh, dimw, board,first):
	global orderedSol
	
	if first:
		solution = deepcopy(gensol(board,dimh,dimw))
		neighborT(solution,posr,posc)
	
	solut = deepcopy(orderedSol)
	#drawLines(solut)

	move = decideMove(posr,posc,board,solut)
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

	(nr,nc) = (sol[0][0],sol[0][1])

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

def gensol(board,dimh,dimw):
	listD = []
	for i in xrange(0,dimh):
		for j in xrange(0,dimw):
			if board[i][j] == 'd':
				listD.append([i,j])
	solution = listD
	return solution
	
def neighborT(sol,pr,pc):
	global orderedSol
	print sol
	if len(sol) == 0:
		print "finished",orderedSol
	else:
		mind = 999999
		for s in sol:
			d = (pr - s[0])**2 + (pc - s[1])**2
			if d < mind:
				dummy = s
				mind = d
		orderedSol.append(dummy)
		sol.pop(sol.index(dummy))
		neighborT(sol,dummy[0],dummy[1])
		
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

size = 6
fact = width/(1.2*size)

dim = [size,size]
dimh = dim[0]
dimw = dim[1]

(board,pos) = genBoard()

solution = []
pointlist = []
orderedSol = []
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
		move = next_move(pos[0], pos[1], dim[0], dim[1], board,first)
		first = False
		
		print move
		raw_input()
		if move == 'CLEAN':
			(pos[0],pos[1]) = (pos[0],pos[1])
			board[pos[0]][pos[1]] = 'b'
			if len(orderedSol) > 0:		
				orderedSol.pop(orderedSol.index([pos[0],pos[1]]))
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
			
		for p in pointlist:
			pygame.draw.lines(screen, (0,255,255), False, p, 10)

		for r in radii:
			pygame.draw.circle(screen, (0,255,255), (int(r[0]),int(r[1])), 10, 10)


	# ***********************************************

			
		pygame.display.flip()
	

