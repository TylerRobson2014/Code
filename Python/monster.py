from __future__ import division
import pygame
from pygame import gfxdraw
import math
import random
from random import shuffle
import numpy as np

grid = [[[""] for x in xrange(4)] for x in xrange(4)]

grid[0][0][0] = "B"
grid[0][1][0] = "R"
grid[0][2][0] = "G"
grid[0][3][0] = "B"

grid[1][0][0] = "B"
grid[1][1][0] = ""
grid[1][2][0] = "R"
grid[1][3][0] = ""

grid[2][0][0] = "G"
grid[2][1][0] = "R"
grid[2][2][0] = "G"
grid[2][3][0] = ""

grid[3][0][0] = "B"
grid[3][1][0] = ""
grid[3][2][0] = ""
grid[3][3][0] = "G"

def landingRule(r1,c1,r2,c2,grid):
	
	lx = len(grid[r1][c1][0])-1
	ly = len(grid[r2][c2][0])-1
	if grid[r1][c1][0]!="":
		X = grid[r1][c1][0][lx]
	else:
		X = ""
	if grid[r2][c2][0]!="":
		Y = grid[r2][c2][0][0]
	else:
		Y = ""
	
	#print "x,y",X,Y,r1,c1,r2,c2
	
	if X == "R" and Y == "B":
		return True
	elif X == "G" and Y == "R":
		return True
	elif X == "B" and Y == "G":
		return True
	else:
		return False
		
def jumpRule(r1,c1,r2,c2,grid):
	allow = True
	if r2 == r1 and c1 != c2:
		if c1 < c2:
			for x in xrange(1,abs(c2-c1)):
				if grid[r1][c1+x] != "":
					allow = False
		if c1 > c2:
			for x in xrange(1,abs(c2-c1)):
				if grid[r1][c2-x] != "":
					allow = False
	if c2 == c1 and r1 != r2:
		if r1 < r2:
			for x in xrange(1,abs(r2-r1)):
				if grid[r1+x][c1] != "":
					allow = False
		if r1 > r2:
			for x in xrange(1,abs(r2-r1)):
				if grid[r2-x][c1] != "":
					allow = False
	if c1 != c2 and r1 != r2:
		allow = False
	if c2 > 3 or r2 > 3:
		allow = False
	
	return allow

def updateJump(r1,c1,r2,c2,grid):
	print "1",grid[r1][c1][0],grid[r2][c2][0]
	grid[r2][c2][0] += grid[r1][c1][0]
	grid[r1][c1][0] = ""

def jump(r1,c1,r2,c2,grid):
	if jumpRule(r1,c1,r2,c2,grid) and landingRule(r1,c1,r2,c2,grid):
		updateJump(r1,c1,r2,c2,grid)

def move(r1,c1,grid):
	for r2 in xrange(r1,4):
		for c2 in xrange(c1,4):
			jump(r1,c1,r2,c2,grid)
			#move(r2,c2,grid)

def myprint(grid):
	for i in xrange(4):
		print grid[i]
	print "************"

def mycount(grid):
	count = 0 
	for i in xrange(0,4):
		for j in xrange(0,4):
			if grid[i][j][0] != "":
				count += 1
	return count

myprint(grid)

for r1 in xrange(0,4):
	for c1 in xrange(0,4):
		count = mycount(grid)
		if count > 1:
			#print r1,c1
			move(r1,c1,grid)

myprint(grid)
