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

def populate_sphere():
	radius = 50
	global sphere,dev
	phi = 0
	count = 0
	for phi in xrange(0,dev):
		theta = 0
		for theta in xrange(0,dev):
			sphere[count][0] = radius * math.sin(phi * 2 * math.pi/dev) * math.cos(theta * 2 * math.pi/dev) 
			sphere[count][1] = radius * math.sin(theta * 2 * math.pi/dev)
			sphere[count][2] = radius * math.cos(theta * 2 * math.pi/dev) * math.cos(phi * 2 * math.pi/dev)
			count += 1
			theta += 1
		phi += 1


def display_sphere():
	global xpos,ypos,zpos
	global sphere,dev
	newsphere = [[0 for x in xrange(3)] for y in xrange(dev*dev)]

	color1 = (255,0,0)
	color2 = (0,255,0)
	color3 = (0,0,255)
	
	phi = 0
	count = 0
	for phi in xrange(0,dev):
		theta = 0
		for theta in xrange(0,dev):
			x = int(sphere[count][0] * abs(sphere[count][2]*0.0015+1) * abs(zpos*0.0015+1)) + xpos
			y = int(sphere[count][1] * abs(sphere[count][2]*0.0015+1) * abs(zpos*0.0015+1)) + ypos
			pygame.draw.circle(screen, color1, (x,y), 1, 1)
			theta += 1
			count += 1
		phi += 1


def rotate(matrix):
	global sphere,dev
	newsphere = [[0 for x in xrange(3)] for y in xrange(dev*dev)]
	for k in xrange(dev*dev):
		for m in xrange(3):
			for j in xrange(3):
				newsphere[k][m] += matrix[m][j]*sphere[k][j]

	for k in xrange(dev*dev):
		for n in xrange(3):
			sphere[k][n] = newsphere[k][n]

		
def movesphere():
	global xpos,ypos,zpos,dvx,dvy,dvz

	if xpos < 50: dvx = -dvx
	if xpos > width - 50: dvx = -dvx
	if ypos < 50: dvy = -dvy
	if ypos > height - 50: dvy = -dvy
	if zpos < 0: dvz = -dvz
	if zpos > height: dvz = -dvz
	xpos += dvx
	ypos += dvy
	zpos += dvz

dev = 50

sphere = [[0 for x in xrange(3)] for y in xrange(dev*dev)]
populate_sphere()
xpos = 100
ypos = 100
zpos = 0
dvx = 24
dvy = 10
dvz = 10

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
	movesphere()
	display_sphere()
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
	

	
	#raw_input()
		
	pygame.display.flip()

