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
			cube[x][0] = -50
			cube[x][1] = -50 + x*100
			cube[x][2] = 150
		if x >=2 and x < 4:
			cube[x][0] = 50
			cube[x][1] = -50 + (x-2)*100
			cube[x][2] = 150
		if x >=4 and x < 6:
			cube[x][0] = -50
			cube[x][1] = -50 + (x-4)*100
			cube[x][2] = 50
		if x >=6 and x < 8:
			cube[x][0] = 50
			cube[x][1] = -50 + (x-6)*100
			cube[x][2] = 50
	
def display_cube():
	global cube
	newcube = [[0 for x in xrange(3)] for y in xrange(8)]
	fill = 5
	factor = 90
	color1 = (255,0,0)
	color2 = (0,255,0)
	color3 = (0,0,255)
	
	for k in xrange(8):
		#print "point = ",k," x = ",cube[k][0]," y = ",cube[k][1]," z = ",cube[k][2]
		for n in xrange(3):
			if n < 2:
				newcube[k][n] = cube[k][n] * abs(cube[k][2]*0.0015+1)
			else:
				newcube[k][n] = cube[k][n]
	
	pointlist = ((newcube[0][0]+200,newcube[0][1]+200),(newcube[1][0]+200,newcube[1][1]+200),(newcube[5][0]+200,newcube[5][1]+200),(newcube[4][0]+200,newcube[4][1]+200))
	#pygame.draw.polygon(screen, color3, pointlist, fill)
	pointlist = ((newcube[5][0]+200,newcube[5][1]+200),(newcube[7][0]+200,newcube[7][1]+200),(newcube[6][0]+200,newcube[6][1]+200),(newcube[4][0]+200,newcube[4][1]+200))
	#pygame.draw.polygon(screen, color1, pointlist, fill)
	pointlist = ((newcube[3][0]+200,newcube[3][1]+200),(newcube[7][0]+200,newcube[7][1]+200),(newcube[6][0]+200,newcube[6][1]+200),(newcube[2][0]+200,newcube[2][1]+200))
	#pygame.draw.polygon(screen, color1, pointlist, fill)
	pointlist = ((newcube[0][0]+200,newcube[0][1]+200),(newcube[2][0]+200,newcube[2][1]+200),(newcube[6][0]+200,newcube[6][1]+200),(newcube[4][0]+200,newcube[4][1]+200))
	#pygame.draw.polygon(screen, color1, pointlist, fill)
	pointlist = ((newcube[1][0]+200,newcube[1][1]+200),(newcube[5][0]+200,newcube[5][1]+200),(newcube[7][0]+200,newcube[7][1]+200),(newcube[3][0]+200,newcube[3][1]+200))
	#pygame.draw.polygon(screen, color3, pointlist, fill)
	pointlist = ((newcube[0][0]+200,newcube[0][1]+200),(newcube[1][0]+200,newcube[1][1]+200),(newcube[3][0]+200,newcube[3][1]+200),(newcube[2][0]+200,newcube[2][1]+200))
	#pygame.draw.polygon(screen, color3, pointlist, fill)
	
	pygame.draw.line(screen, color1, (newcube[0][0]+200,newcube[0][1]+200), (newcube[1][0]+200,newcube[1][1]+200), 1)	
	pygame.draw.line(screen, color1, (newcube[0][0]+200,newcube[0][1]+200), (newcube[2][0]+200,newcube[2][1]+200), 1)
	pygame.draw.line(screen, color3, (newcube[0][0]+200,newcube[0][1]+200), (newcube[4][0]+200,newcube[4][1]+200), 1)
	pygame.draw.line(screen, color3, (newcube[1][0]+200,newcube[1][1]+200), (newcube[5][0]+200,newcube[5][1]+200), 1)
	pygame.draw.line(screen, color1, (newcube[1][0]+200,newcube[1][1]+200), (newcube[3][0]+200,newcube[3][1]+200), 1)
	pygame.draw.line(screen, color3, (newcube[2][0]+200,newcube[2][1]+200), (newcube[6][0]+200,newcube[6][1]+200), 1)
	pygame.draw.line(screen, color1, (newcube[2][0]+200,newcube[2][1]+200), (newcube[3][0]+200,newcube[3][1]+200), 1)
	pygame.draw.line(screen, color3, (newcube[3][0]+200,newcube[3][1]+200), (newcube[7][0]+200,newcube[7][1]+200), 1)
	pygame.draw.line(screen, color2, (newcube[4][0]+200,newcube[4][1]+200), (newcube[5][0]+200,newcube[5][1]+200), 1)
	pygame.draw.line(screen, color2, (newcube[4][0]+200,newcube[4][1]+200), (newcube[6][0]+200,newcube[6][1]+200), 1)
	pygame.draw.line(screen, color2, (newcube[5][0]+200,newcube[5][1]+200), (newcube[7][0]+200,newcube[7][1]+200), 1)
	pygame.draw.line(screen, color2, (newcube[6][0]+200,newcube[6][1]+200), (newcube[7][0]+200,newcube[7][1]+200), 1)

def rotate(matrix):
	global cube
	newcube = [[0 for x in xrange(3)] for y in xrange(8)]
	for k in xrange(8):
		for m in xrange(3):
			for j in xrange(3):
				newcube[k][m] += matrix[m][j]*cube[k][j]

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
	angle = math.pi/10
	c = math.cos(angle)
	s = math.sin(angle)
	RX = [[1,0,0],[0,c,s],[0,-s,c]]
	#print RX
	RY = [[c,0,-s],[0,1,0],[s,0,c]]
	RZ = [[c,s,0],[-s,c,0],[0,0,1]]
	I  = [[1,0,0],[0,1,0],[0,0,1]]
	#print cube
	a = random.randint(1,3)
	#a = 1
	if a == 1: rotate(RX)
	if a == 2: rotate(RY)
	if a == 3: rotate(RZ)
	if a == 4: rotate(I)

	raw_input()
		
	pygame.display.flip()

