from __future__ import division
import pygame
from pygame import gfxdraw
import math
import random
from random import shuffle
from copy import deepcopy

background_colour = (255,255,255)
height = int(500)
width = int(500)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Lattice Gas')
screen.fill(background_colour)

def grid_create():
	global size
	grid = [[0 for i in xrange(size)] for j in xrange(size)]
	return grid

		
def marks_r():
	
	mark = [[[0 for i in xrange(9)] for j in xrange(25)] for k in xrange(2)]

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
	
def marksttt():
	
	global size
	
	mark = [[[0 for i in xrange(9)] for j in xrange(size)] for k in xrange(2)]

	mark[0][0] = [size-3]
	mark[0][1] = [0]
	mark[0][2] = [size-3]
	mark[0][3] = [0]
	mark[0][4] = [size-3]
	mark[0][5] = [0]
	mark[0][6] = [size-3]
	mark[0][7] = [0]
	mark[0][8] = [1,0,size-3]
	mark[0][9] = [2]
	mark[0][10] = [2,0,size-3]
	mark[0][11] = [2]
	mark[0][12] = [1,0,size-3]
	mark[0][13] = [0]
	mark[0][14] = [size-3]
	mark[0][15] = [0]
	mark[0][16] = [size-3]
	mark[0][17] = [0]
	mark[0][18] = [size-3]
	mark[0][19] = [0]

	
			
	mark[1][0] = [3]
	mark[1][1] = [5]
	mark[1][2] = [0]
	mark[1][3] = [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0]
	mark[1][4] = [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0]
	mark[1][5] = [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0]
	mark[1][6] = [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0]
	mark[1][7] = [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0]
	mark[1][8] = [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0]
	mark[1][9] = [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0]
	mark[1][10] = [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0]
	mark[1][11] = [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0]
	mark[1][12] = [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0]
	mark[1][13] = [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0]
	mark[1][14] = [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0]
	mark[1][15] = [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0]
	mark[1][16] = [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0]
	mark[1][17] = [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0]
	mark[1][18] = [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0]
	mark[1][19] = [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0]
	
	return mark
	
def marksddd():
	
	global size
	
	mark = [[[0 for i in xrange(9)] for j in xrange(size)] for k in xrange(2)]

	mark[0][0] = []
	mark[0][1] = [size-3]
	mark[0][2] = []
	mark[0][3] = [size-3]
	mark[0][4] = []
	mark[0][5] = [size-3]
	mark[0][6] = []
	mark[0][7] = []
	mark[0][8] = [1,,size-3]
	mark[0][9] = [2]
	mark[0][10] = [2,,size-3]
	mark[0][11] = [2]
	mark[0][12] = [1,,size-3]
	mark[0][13] = []
	mark[0][14] = []
	mark[0][15] = []
	mark[0][16] = []
	mark[0][17] = []
	mark[0][18] = []
	mark[0][19] = []

	
			
	mark[1][0] = [3]
	mark[1][1] = [5]
	mark[1][2] = []
	mark[1][3] = [1,1,1,1,1,1]
	mark[1][4] = [1,1,1,1,1,1]
	mark[1][5] = [1,1,1,1,1,1]
	mark[1][6] = [1,1,1,1,1,1]
	mark[1][7] = [1,1,1,1,1,1]
	mark[1][8] = [1,1,1,1,1,1]
	mark[1][9] = [1,1,1,1,1,1]
	mark[1][10] = [1,1,1,1,1,1]
	mark[1][11] = [1,1,1,1,1,1]
	mark[1][12] = [1,1,1,1,1,1]
	mark[1][13] = [1,1,1,1,1,1]
	mark[1][14] = [1,1,1,1,1,1]
	mark[1][15] = [1,1,1,1,1,1]
	mark[1][16] = [1,1,1,1,1,1]
	mark[1][17] = [1,1,1,1,1,1]
	mark[1][18] = [1,1,1,1,1,1]
	mark[1][19] = [1,1,1,1,1,1]
	
	return mark
	
	
def marksk():
	
	global size
	
	mark = [[[0 for i in xrange(9)] for j in xrange(size)] for k in xrange(2)]

	mark[0][0] = [size]
	mark[0][1] = [0]
	mark[0][2] = [size]
	mark[0][3] = [0]
	mark[0][4] = [size]
	
	mark[1][0] = [1,0,1,0,1]
	mark[1][1] = [1,0,1,0,1]
	mark[1][2] = [1,0,1,0,1]
	mark[1][3] = [1,0,1,0,1]
	mark[1][4] = [1,0,1,0,1]
	
	return mark
	
def marks():
	
	global size
	
	mark = [[[0 for i in xrange(9)] for j in xrange(size)] for k in xrange(2)]

	mark[0][0] = [2]
	mark[0][1] = [1,0,2]
	mark[0][2] = [2,0,3]
	mark[0][3] = [2,0,3]
	mark[0][4] = [3,0,1,0,1]
	mark[0][5] = [2,0,1,0,1]
	mark[0][6] = [1,0,1,0,1,0,2,0,2]
	mark[0][7] = [1,0,1,0,3,0,1,0,3]
	mark[0][8] = [2,0,6,0,4]
	mark[0][9] = [3,0,3,0,9,0,1]
	mark[0][10] = [5,0,3,0,2]
	mark[0][11] = [3,0,1,0,2,0,2]
	mark[0][12] = [2,0,1,0,7]
	mark[0][13] = [3,0,3,0,2]
	mark[0][14] = [2,0,4]
	mark[0][15] = [2,0,1,0,2]
	mark[0][16] = [2,0,2,0,1]
	mark[0][17] = [2,0,2]
	mark[0][18] = [1]
	mark[0][19] = [1]
	
	mark[1][0] = [3]
	mark[1][1] = [5]
	mark[1][2] = [3,0,1]
	mark[1][3] = [2,0,1]
	mark[1][4] = [3,0,3,0,4]
	mark[1][5] = [2,0,2,0,7]
	mark[1][6] = [6,0,1,0,1]
	mark[1][7] = [4,0,2,0,2]
	mark[1][8] = [1,0,1]
	mark[1][9] = [3,0,1]
	mark[1][10] = [6]
	mark[1][11] = [2,0,7]
	mark[1][12] = [6,0,3,0,1]
	mark[1][13] = [1,0,2,0,2,0,1,0,1]
	mark[1][14] = [4,0,1,0,1,0,3]
	mark[1][15] = [4,0,2,0,2]
	mark[1][16] = [3,0,3,0,1]
	mark[1][17] = [3,0,3]
	mark[1][18] = [3]
	mark[1][19] = [2,0,1]
	
	return mark
	
def decide(grid,constraints,i,j):
	
	global size
	
	flag = 0
	count1 = 0
	count = 0
	
	populatei = False
	populatej = False
	
	vector = []
	
	for x in xrange(size):
		if grid[i][x] == 1:
			flag = 1
			count1 += 1
		if grid[i][x] == 0:
			if flag == 1:
				flag = 0
				count += 1
				vector.append(count1)
				count1 = 0

		if len(vector) <= len(constraints[1][i]):
			for c in xrange(len(vector)):
				if vector[c] == constraints[1][i][c]:
					populatei = True
				elif vector[c] < constraints[1][i][c]:
					if c == len(constraints[1][i]):
						populatei = True
						
	for y in xrange(size):
		if grid[y][j] == 1:
			flag = 1
			count1 += 1
		if grid[y][j] == 0:
			if flag == 1:
				flag = 0
				count += 1
				vector.append(count1)
				count1 = 0

		if len(vector) <= len(constraints[0][j]):
			for c in xrange(len(vector)):
				if vector[c] == constraints[0][j][c]:
					populatej = True
				elif vector[c] < constraints[0][j][c]:
					if c == len(constraints[0][j]):
						populatej = True
						
	populate = populatei and populatej
				
	return populate


	
def solve(grid,i,j,x,y,constraints,track):
	
	global size,stop,newgrid,pop
	
	if not (stop):
		
		if j > size - 1: 
			
			j = 0
			i += 1
		
		if i > size - 2 and j > size - 2:

			stop = True
			
		decide(grid,constraints,i,j)
			
		if test == 1:
			
			grid[i][j] = 1
			
			#print "A",i,j
			#print "A",constr[1][i],constr[0][j]

			#raw_input()

			screen.fill(background_colour)
			

			for jj in xrange(size):
				for ii in xrange(size):
					xx = ii*15 + 15
					yy = jj*15 + 15
					w = 15
					h = 15
					Rect = (xx,yy,w,h)
					wid = 1
					if grid[jj][ii] == 1: wid = 0
					pygame.draw.rect(screen, (0,0,0), Rect, wid)
			
			newgrid = deepcopy(grid) 

			pygame.display.flip()
			
			solve(deepcopy(grid),i,j+1,i,j,deepcopy(constr),track+1)
			
			if not (stop):
				
#				if j - 1 >= 0:
				#print "******** pop",pop 
				if grid[i][j-1] == "1" :#and (pop == 0 or pop == 1):
					grid[i][j] = ""
					test = 0
					#print "fall1"					
				else:					
					test = 2
					grid[i][j] = ""
				
				#print "C",i,j,test
				#print "C",constr[1][i],constr[0][j]
				#raw_input()
		
		if test == 0:
			pass
			
			#print "zer",i,j,test
			#print "zer",constr[1][i],constr[0][j]
			#raw_input()
						
			
		if test == 2 and not(stop):
			#print "miss step",constr[1][i],constr[0][j]
			#raw_input()

			if grid[i-1][j] == "1":
				if len(constr[0][j]) > 0:
					#print "&&&&&&",constr[0][j],i,j
					if constr[0][j][0] > 0:
						test = 0
						#print "fall4"
					else:
						test = 2
						solve(deepcopy(grid),i,j+1,i,j,deepcopy(constr),track+1)						
				elif len(constr[0][j]) == 0:
					test = 2
					solve(deepcopy(grid),i,j+1,i,j,deepcopy(constr),track+1)
			else:					
				test = 2
				solve(deepcopy(grid),i,j+1,i,j,deepcopy(constr),track+1)
			
	

pop = 0
size = 20
#size = 5
mygrid = grid_create()
newgrid = grid_create()
constraints = marks()
testgoodness = deepcopy(constraints)

i = 0
j = 0
(x,y) = (0,0)
stop = False
track = 1
newgrid = []
solve(mygrid,i,j,x,y,constraints,track)
#print "newgrid",newgrid
	
running = True
timer_event = pygame.USEREVENT + 1
pygame.time.set_timer(timer_event, 1)
screen.fill(background_colour)
while running:
	event = pygame.event.wait()
	
	screen.fill(background_colour)
	

	for j in xrange(size):
		for i in xrange(size):
			x = i*15 + 15
			y = j*15 + 15
			w = 15
			h = 15
			Rect = (x,y,w,h)
			wid = 1
			if newgrid[j][i] == 1: wid = 0
			pygame.draw.rect(screen, (0,0,0), Rect, wid) 

	pygame.display.flip()
