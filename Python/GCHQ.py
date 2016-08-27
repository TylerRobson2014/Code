from __future__ import division
import pygame
from pygame import gfxdraw
import math
import random
from random import shuffle

background_colour = (255,255,255)
height = int(500)
width = int(500)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Lattice Gas')
screen.fill(background_colour)

def grid_create():
	global grid,size
	grid = [[["","0","1"] for i in xrange(size)] for j in xrange(size)]
	
	return grid

		
def marks():
	
	mark = [[[0 for i in xrange(9)] for j in xrange(25)] for k in xrange(25)]

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
	
def marks_t():
	
	global size
	
	mark = [[[0 for i in xrange(9)] for j in xrange(size)] for k in xrange(size)]

	mark[0][0] = [3]
	mark[0][1] = []
	mark[0][2] = [2]
	mark[0][3] = []
	mark[0][4] = [size]
	
	mark[1][0] = [1,1]
	mark[1][1] = [1,1]
	mark[1][2] = [1,1]
	mark[1][3] = [1,1]
	mark[1][4] = [1,1]
	
	return mark

def check(d):
	count = 0
	record = []
	for i in xrange(len(d)):
		if d[i][0] == "1":
			count += 1
		if d[i][0] == "0" or d[i][0] == "":
			if count == 0:
				pass
			else:
				record.append(count)
				count = 0
	if count > 0:
		record.append(count)
		count = 0
		
	return record

def solve(mygrid,constraints,rowc,colc):
	global size
	ones = 0
	p = 0
	q = 0
	for rc in xrange(size):
		cc = 0
		for i in xrange(len(constraints[1][rc])):
			tomatch = constraints[1][rc][i]
			for k in xrange(tomatch):
				match = False
				while not(match):
					if len(constraints[0][cc]) > 0:
						if constraints[0][cc][0] > 0:
							constraints[0][cc][0] -= 1
							if constraints[0][cc][0] == 0:
								constraints[0][cc].pop(0)
							mygrid[rc][cc][0] = "1"
							print rc,cc
							match = True
							cc += 1
						else:
							cc += 1
					else:
						cc += 1
			cc += 1
	return mygrid
					
def printgrid(mygrid):
	global size
	for t in range(size):
		for s in range(size):
			print mygrid[t][s][0],
		print ""
		
def summ(l):
	count = 0
	for i in xrange(len(l)):
		count += int(l[i])
	return count
		
def prepop(constraints,mygrid):
	global size
	for k in xrange(2):
		count = 0
		for j in xrange(size):
			s = summ(constraints[k][j])
			count = 0
			if s + len(constraints[k][j]) - 1 == size:
				for m in xrange(len(constraints[k][j])):
					for n in xrange(int(constraints[k][j][m])):

						if k == 0 and count <= size-1:
							mygrid[j][count][0] = "1"
							count += 1
							
						if k == 1 and count <= size-1:
							mygrid[count][j][0] = "1"
							count += 1

					if k == 0 and count <= size-1:
						mygrid[j][count][0] = "0"
						count += 1

					if k == 1  and count <= size-1:
						mygrid[count][j][0] = "0"
						count += 1
	for t in range(size):
		for s in range(size):
			if len(mygrid[s][t]) > 1:
				mygrid[s][t].pop(1)
				mygrid[s][t].pop(1)

index = 0
stopall = False
rowc = 0
colc = 0
size = 25					

mygrid = grid_create()
constraints = marks()
#prepop(constraints,mygrid)
#printgrid(mygrid)

mynewgrid = solve(mygrid,constraints,rowc,colc)

printgrid(mynewgrid)

for t in range(size):
	for s in range(size):
		print mynewgrid[s][t][0]


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
			if mynewgrid[j][i][0] == "1": wid = 0
			pygame.draw.rect(screen, (0,0,0), Rect, wid) 

	pygame.display.flip()

