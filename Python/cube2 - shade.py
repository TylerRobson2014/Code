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
	global xpos,ypos,zpos
	global cube
	newcube = [[0 for x in xrange(3)] for y in xrange(8)]
	fillcube = [[0 for x in xrange(3)] for y in xrange(8)]
	fill = 0
	factor = 90
	color1 = (255,0,0)
	color2 = (0,255,0)
	color3 = (0,0,255)
	
	for k in xrange(8):
		#print "point = ",k," x = ",cube[k][0]," y = ",cube[k][1]," z = ",cube[k][2]
		for n in xrange(3):
			if n < 2:
				newcube[k][n] = cube[k][n] * abs(cube[k][2]*0.0015+1)
				fillcube[k][n] = (cube[k][n])* abs(cube[k][2]*0.0015+1)
			else:
				newcube[k][n] = cube[k][n]
				fillcube[k][n] = cube[k][n]
	
	
	#pointlist = ((fillcube[0][0]+off1,fillcube[0][1]+off1),(fillcube[1][0]+off1,fillcube[1][1]+off1),(fillcube[5][0]+off1,fillcube[5][1]+off1),(fillcube[4][0]+off1,fillcube[4][1]+off1))
	#pygame.draw.polygon(screen, color2, pointlist, fill)
	#pointlist = ((fillcube[5][0]+off1,fillcube[5][1]+off1),(fillcube[7][0]+off1,fillcube[7][1]+off1),(fillcube[6][0]+off1,fillcube[6][1]+off1),(fillcube[4][0]+off1,fillcube[4][1]+off1))
	#pygame.draw.polygon(screen, color2, pointlist, fill)
	#pointlist = ((fillcube[3][0]+off1,fillcube[3][1]+off1),(fillcube[7][0]+off1,fillcube[7][1]+off1),(fillcube[6][0]+off1,fillcube[6][1]+off1),(fillcube[2][0]+off1,fillcube[2][1]+off1))
	#pygame.draw.polygon(screen, color1, pointlist, fill)
	#pointlist = ((fillcube[0][0]+off1,fillcube[0][1]+off1),(fillcube[2][0]+off1,fillcube[2][1]+off1),(fillcube[6][0]+off1,fillcube[6][1]+off1),(fillcube[4][0]+off1,fillcube[4][1]+off1))
	#pygame.draw.polygon(screen, color1, pointlist, fill)
	#pointlist = ((fillcube[1][0]+off1,fillcube[1][1]+off1),(fillcube[5][0]+off1,fillcube[5][1]+off1),(fillcube[7][0]+off1,fillcube[7][1]+off1),(fillcube[3][0]+off1,fillcube[3][1]+off1))
	#pygame.draw.polygon(screen, color3, pointlist, fill)
	#pointlist = ((fillcube[0][0]+off1,fillcube[0][1]+off1),(fillcube[1][0]+off1,fillcube[1][1]+off1),(fillcube[3][0]+off1,fillcube[3][1]+off1),(fillcube[2][0]+off1,fillcube[2][1]+off1))
	#pygame.draw.polygon(screen, color3, pointlist, fill)
	
	pygame.draw.line(screen, color1, (newcube[0][0]+xpos,newcube[0][1]+ypos), (newcube[1][0]+xpos,newcube[1][1]+ypos), 1)	
	pygame.draw.line(screen, color1, (newcube[0][0]+xpos,newcube[0][1]+ypos), (newcube[2][0]+xpos,newcube[2][1]+ypos), 1)
	pygame.draw.line(screen, color3, (newcube[0][0]+xpos,newcube[0][1]+ypos), (newcube[4][0]+xpos,newcube[4][1]+ypos), 1)
	pygame.draw.line(screen, color3, (newcube[1][0]+xpos,newcube[1][1]+ypos), (newcube[5][0]+xpos,newcube[5][1]+ypos), 1)
	pygame.draw.line(screen, color1, (newcube[1][0]+xpos,newcube[1][1]+ypos), (newcube[3][0]+xpos,newcube[3][1]+ypos), 1)
	pygame.draw.line(screen, color3, (newcube[2][0]+xpos,newcube[2][1]+ypos), (newcube[6][0]+xpos,newcube[6][1]+ypos), 1)
	pygame.draw.line(screen, color1, (newcube[2][0]+xpos,newcube[2][1]+ypos), (newcube[3][0]+xpos,newcube[3][1]+ypos), 1)
	pygame.draw.line(screen, color3, (newcube[3][0]+xpos,newcube[3][1]+ypos), (newcube[7][0]+xpos,newcube[7][1]+ypos), 1)
	pygame.draw.line(screen, color2, (newcube[4][0]+xpos,newcube[4][1]+ypos), (newcube[5][0]+xpos,newcube[5][1]+ypos), 1)
	pygame.draw.line(screen, color2, (newcube[4][0]+xpos,newcube[4][1]+ypos), (newcube[6][0]+xpos,newcube[6][1]+ypos), 1)
	pygame.draw.line(screen, color2, (newcube[5][0]+xpos,newcube[5][1]+ypos), (newcube[7][0]+xpos,newcube[7][1]+ypos), 1)
	pygame.draw.line(screen, color2, (newcube[6][0]+xpos,newcube[6][1]+ypos), (newcube[7][0]+xpos,newcube[7][1]+ypos), 1)

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
		
def move_cube():
	global cube
	global xpos,ypos,dvx,dvy
	xpos += dvx
	ypos += dvy
	if xpos < 150: dvx = -dvx
	if xpos > width - 150: dvx = -dvx
	if ypos < 150: dvy = -dvy
	if ypos > height - 150: dvy = -dvy
	xpos += dvx
	ypos += dvy


cube = [[0 for x in xrange(3)] for y in xrange(8)]
populate_cube()
xpos = 200
ypos = 200
(dvx,dvy) = (5,5)

running = True

angle = 0

timer_event = pygame.USEREVENT + 1
pygame.time.set_timer(timer_event, 100)
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

	if a == 1: rotate(RX)
	if a == 2: rotate(RY)
	if a == 3: rotate(RZ)
	if a == 4: rotate(I)
	
	move_cube()


	#raw_input()
		
	pygame.display.flip()

