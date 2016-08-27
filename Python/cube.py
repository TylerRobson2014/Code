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

def populate_cube():
	global cube
	for x in xrange(8):
		if x < 2:
			cube[x][0] = 100
			cube[x][1] = 100 + x*100
			cube[x][2] = 0
		if x >=2 and x < 4:
			cube[x][0] = 200
			cube[x][1] = 100 + (x-2)*100
			cube[x][2] = 0
		if x >=4 and x < 6:
			cube[x][0] = 100
			cube[x][1] = 100 + (x-4)*100
			cube[x][2] = 100
		if x >=6 and x < 8:
			cube[x][0] = 200
			cube[x][1] = 100 + (x-6)*100
			cube[x][2] = 100
	
def display_cube():
	global cube
	color1 = (255,0,0)
	color2 = (0,255,0)
	color3 = (0,0,255)
	pointlist = ((cube[0][0],cube[0][1]),(cube[1][0],cube[1][1]),(cube[3][0],cube[3][1]),(cube[2][0],cube[2][1]))
	pygame.draw.polygon(screen, color1, pointlist, 0)
	pointlist = ((cube[0][0],cube[0][1]),(cube[1][0],cube[1][1]),(cube[5][0],cube[5][1]),(cube[4][0],cube[4][1]))
	pygame.draw.polygon(screen, color3, pointlist, 0)
	pointlist = ((cube[5][0],cube[5][1]),(cube[7][0],cube[7][1]),(cube[6][0],cube[6][1]),(cube[4][0],cube[4][1]))
	pygame.draw.polygon(screen, color1, pointlist, 0)
	pointlist = ((cube[3][0],cube[3][1]),(cube[7][0],cube[7][1]),(cube[6][0],cube[6][1]),(cube[2][0],cube[2][1]))
	pygame.draw.polygon(screen, color3, pointlist, 0)
	pointlist = ((cube[0][0],cube[0][1]),(cube[2][0],cube[2][1]),(cube[6][0],cube[6][1]),(cube[4][0],cube[4][1]))
	pygame.draw.polygon(screen, color2, pointlist, 0)
	pointlist = ((cube[1][0],cube[1][1]),(cube[5][0],cube[5][1]),(cube[7][0],cube[7][1]),(cube[3][0],cube[3][1]))
	pygame.draw.polygon(screen, color2, pointlist, 0)

def rotate(matrix,angle):
	global cube
	newcube = [[0 for x in xrange(3)] for y in xrange(8)]
	for k in xrange(8):
		for m in xrange(3):
			for j in xrange(3):
				newcube[k][m] = matrix[m][j]*cube[k][j]

	for k in xrange(8):
		for n in xrange(3):
			cube[k][n] = newcube[k][n]

cube = [[0 for x in xrange(3)] for y in xrange(8)]
populate_cube()

running = True

angle = 0

timer_event = pygame.USEREVENT + 1
pygame.time.set_timer(timer_event, 500)
screen.fill(background_colour)
while running:
	event = pygame.event.wait()
	if event.type == pygame.QUIT:
		raise StopIteration
	screen.fill(background_colour)

	display_cube()
	angle += math.pi/10
	c = math.cos(angle)
	s = math.sin(angle)
	RX = [[1,0,0],[0,c,s],[0,-s,c]]
	RY = [[c,0,-s],[0,1,0],[s,0,c]]
	RZ = [[c,s,0],[-s,c,0],[0,0,1]]
	print cube
	rotate(RY,angle)
	print cube

		
	pygame.display.flip()

