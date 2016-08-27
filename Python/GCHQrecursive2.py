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
	global grid,size
	grid = [["" for i in xrange(size)] for j in xrange(size)]
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
	
def marks_t1():
	
	global size
	
	mark = [[[0 for i in xrange(9)] for j in xrange(size)] for k in xrange(2)]

	mark[0][0] = [size]
	mark[0][1] = [1]
	mark[0][2] = [1,3]
	mark[0][3] = []
	mark[0][4] = [2,1]
	
	mark[1][0] = [1,1,1]
	mark[1][1] = [1,1]
	mark[1][2] = [3]
	mark[1][3] = [1,1]
	mark[1][4] = [1,1,1]
	
	return mark
	
def marks():
	
	global size
	
	mark = [[[0 for i in xrange(9)] for j in xrange(size)] for k in xrange(2)]

	mark[0][0] = [2]
	mark[0][1] = [1,2]
	mark[0][2] = [2,3]
	mark[0][3] = [2,3]
	mark[0][4] = [3,1,1]
	mark[0][5] = [2,1,1]
	mark[0][6] = [1,1,1,2,2]
	mark[0][7] = [1,1,3,1,3]
	mark[0][8] = [2,6,4]
	mark[0][9] = [3,3,9,1]
	mark[0][10] = [5,3,2]
	mark[0][11] = [3,1,2,2]
	mark[0][12] = [2,1,7]
	mark[0][13] = [3,3,2]
	mark[0][14] = [2,4]
	mark[0][15] = [2,1,2]
	mark[0][16] = [2,2,1]
	mark[0][17] = [2,2]
	mark[0][18] = [1]
	mark[0][19] = [1]
	
	mark[1][0] = [3]
	mark[1][1] = [5]
	mark[1][2] = [3,1]
	mark[1][3] = [2,1]
	mark[1][4] = [3,3,4]
	mark[1][5] = [2,2,7]
	mark[1][6] = [6,1,1]
	mark[1][7] = [4,2,2]
	mark[1][8] = [1,1]
	mark[1][9] = [3,1]
	mark[1][10] = [6]
	mark[1][11] = [2,7]
	mark[1][12] = [6,3,1]
	mark[1][13] = [1,2,2,1,1]
	mark[1][14] = [4,1,1,3]
	mark[1][15] = [4,2,2]
	mark[1][16] = [3,3,1]
	mark[1][17] = [3,3]
	mark[1][18] = [3]
	mark[1][19] = [2,1]
	
	return mark
	

		
def criteria(i,j,constraints):
	
	pass_state = 0
	
	if len(constraints[0][j]) > 0:
		if constraints[0][j][0] > 0:
			if len(constraints[1][i]) > 0:
				if constraints[1][i][0] > 0:
					
					pass_state = 1

	if len(constraints[0][j]) == 0:
		if len(constraints[1][i]) > 0:
			if constraints[1][i][0] > 0:
					
					pass_state = 2
					
	if len(constraints[1][i]) == 0:
		if len(constraints[0][j]) > 0:
			if constraints[0][j][0] > 0:
					
					pass_state = 2

	if len(constraints[1][i]) == 0:
		if len(constraints[0][j]) == 0:
			pass_state = 2
					
	if j == 0 and i > 0:
		if len(constraints[1][i-1]) > 0:
			pass_state = 0

	if len(constraints[1][i]) == 0:
		if len(constraints[0][j]) == 1:
			if constraints[0][j][0] == size-i:
					
					pass_state = 0
					
# *************************************************
	if size == 25:
			
		if i == 3 and j == 3 and not (grid[3][3] == "1"): pass_state = 0
		if i == 3 and j == 4 and not (grid[3][4] == "1"): pass_state = 0
		if i == 3 and j == 12 and not (grid[3][12] == "1"): pass_state = 0
		if i == 3 and j == 13 and not (grid[3][13] == "1"): pass_state = 0
		if i == 3 and j == 21 and not (grid[3][21] == "1"): pass_state = 0
		if i == 8 and j == 6 and not (grid[8][6] == "1"): pass_state = 0
		if i == 8 and j == 7 and not (grid[8][7] == "1"): pass_state = 0
		if i == 8 and j == 10 and not (grid[8][10] == "1"): pass_state = 0
		if i == 8 and j == 14 and not (grid[8][14] == "1"): pass_state = 0
		if i == 8 and j == 15 and not (grid[8][15] == "1"): pass_state = 0
		if i == 8 and j == 18 and not (grid[8][18] == "1"): pass_state = 0
		if i == 16 and j == 6 and not (grid[16][6] == "1"): pass_state = 0
		if i == 16 and j == 11 and not (grid[16][11] == "1"): pass_state = 0
		if i == 16 and j == 16 and not (grid[16][16] == "1"): pass_state = 0
		if i == 16 and j == 20 and not (grid[16][20] == "1"): pass_state = 0
		if i == 21 and j == 3 and not (grid[21][3] == "1"): pass_state = 0
		if i == 21 and j == 4 and not (grid[21][4] == "1"): pass_state = 0
		if i == 21 and j == 9 and not (grid[21][9] == "1"): pass_state = 0
		if i == 21 and j == 10 and not (grid[21][10] == "1"): pass_state = 0
		if i == 21 and j == 15 and not (grid[21][15] == "1"): pass_state = 0
		if i == 21 and j == 20 and not (grid[21][20] == "1"): pass_state = 0
		if i == 21 and j == 21 and not (grid[21][21] == "1"): pass_state = 0

# *************************************************



					
	return pass_state
	
def update_constraints(x,y,grid,cons,track):
	
	if grid[x][y] == "1":
		
#		print "update",track,x,y

		if len(cons[0][y]) > 0:
			cons[0][y][0] -= 1
			if cons[0][y][0] == 0:
				cons[0][y].pop(0)

		if len(cons[1][x]) > 0:
			cons[1][x][0] -= 1
			if cons[1][x][0] == 0:
				cons[1][x].pop(0)

	return cons

	
def solve(ngrid,i,j,x,y,constraints,track):
	
	global size,stop,newgrid
	
	if not (stop):
		
		newcon = []
		
		newcon = deepcopy(constraints)
		
		constr = deepcopy(update_constraints(x,y,deepcopy(grid),newcon,track))
		
		if j > size - 1: 
			
			j = 0
			i += 1
		
		if i > size - 2 and j > size - 2:

			stop = True
		
		test = criteria(i,j,constr)
			
		if test == 1:
			
			grid[i][j] = "1"
			
			print "A",i,j,test, "track = ",track
			print "A",constr[1][i]
			print "A",constr[0][j]
			print "*********"
			print grid
			print "*********"
			raw_input()

			screen.fill(background_colour)
			

			for jj in xrange(size):
				for ii in xrange(size):
					xx = ii*15 + 15
					yy = jj*15 + 15
					w = 15
					h = 15
					Rect = (xx,yy,w,h)
					wid = 1
					if grid[jj][ii] == "1": wid = 0
					pygame.draw.rect(screen, (0,0,0), Rect, wid) 

			pygame.display.flip()
			
			solve(deepcopy(grid),i,j+1,i,j,deepcopy(constr),track+1)
			
			if not (stop):
				
				test = 2
				grid[i][j] = ""
				
				print "C",i,j,test, "track = ",track
				print "C",constr[1][i]
				print "C",constr[0][j]
		
		if test == 0:
			#pass
			
			print "zer",i,j,test, "track = ",track
			print "zer",constr[1][i]
			print "zer",constr[0][j]
						
			
		if test == 2 and not(stop):
			print "miss step",constr[1][i],constr[0][j]
			solve(deepcopy(grid),i,j+1,i,j,deepcopy(constr),track+1)
			
	newgrid = deepcopy(grid)

size = 20

mygrid = grid_create()
newgrid = grid_create()
constraints = marks()

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
pygame.time.set_timer(timer_event, 100)
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
			if newgrid[j][i] == "1": wid = 0
			pygame.draw.rect(screen, (0,0,0), Rect, wid) 

	pygame.display.flip()
