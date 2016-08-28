from __future__ import division
import pygame
from pygame import gfxdraw
import math
import random
import sys
from copy import deepcopy


def randomise(array,gSize):
	zr = gSize-1
	zc = gSize-1
	(i,j) = (zr,zc)
	for x in xrange(1000):
		
		r = random.randint(1,4)
		print "r = ",r
		print "i+1 = ", i+1
		print "j+1 = ", j+1
		
		if r == 1:
			if i-1 >= 0:
				(grid[i][j],grid[i-1][j]) = (grid[i-1][j],grid[i][j])
				(i,j) = (i-1,j)
				myPrint(grid)
		if r == 2:
			if j-1 >= 0:
				(grid[i][j],grid[i][j-1]) = (grid[i][j-1],grid[i][j])
				(i,j) = (i,j-1)
				myPrint(grid)

		if r == 3:
			if i+1 <= gSize-1:
				(grid[i][j],grid[i+1][j]) = (grid[i+1][j],grid[i][j])
				(i,j) = (i+1,j)
				myPrint(grid)
		if r == 4:
			if j+1 <= gSize-1:
				(grid[i][j],grid[i][j+1]) = (grid[i][j+1],grid[i][j])
				(i,j) = (i,j+1)
				myPrint(grid)
		print ""

	return array

def myPrint(array):
	for row in array:
		print row
		

gSize = 4
m = 5
grid = [[x+y*(m-1) for x in xrange(1,m)] for y in xrange(4)]

grid[gSize-1][gSize-1] = 0

myPrint(grid)
print ""

grid = deepcopy(randomise(grid,gSize))

myPrint(grid)
