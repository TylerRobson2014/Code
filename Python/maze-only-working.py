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

#### define maze ####




def processcell(x,y):
	global maze
	neighbours = [0,1,2,3]
	shuffle(neighbours)
	
	if maze[x][y][4] == 1:
		pass
	else:		
		maze[x][y][4] = 1
		
		for neighbour in neighbours:
			
			if neighbour == 0:
				a = x-1 if x-1 >= 0 else -99
				b = y
			if neighbour == 1:
				a = x+1 if x+1 <= number_cells-1 else -99
				b = y
			if neighbour == 2:
				a = x
				b = y-1 if y-1 >= 0 else -99
			if neighbour == 3:
				a = x
				b = y+1 if y+1 <= number_cells-1 else -99
			
			if a > -99 and b > -99:
				#print "xy",x,y
				if maze[a][b][4] == 0:
					#print "ab",a,b
					#maze[a][b][4] = 1
					maze[x][y][neighbour] = 0
					if neighbour == 0:
						coneighbour = 1
					if neighbour == 1:
						coneighbour = 0
					if neighbour == 2:
						coneighbour = 3
					if neighbour == 3:
						coneighbour = 2
					maze[a][b][coneighbour] = 0
					processcell(a,b)

number_cells = 30
maze = [[[1,1,1,1,0] for i in xrange(number_cells)] for j in xrange(number_cells)]
x = random.randint(0,number_cells-1)
y = random.randint(0,number_cells-1)
print x,y
processcell(x,y)

deltashift = 15

for l in xrange(number_cells):
	for k in xrange(number_cells):
		print "n = ",l , "m = ",k, "val = ",maze[k][l]
					
			
running = True

timer_event = pygame.USEREVENT + 1
pygame.time.set_timer(timer_event, 500)
screen.fill(background_colour)
while running:
	event = pygame.event.wait()
	if event.type == pygame.QUIT:
		raise StopIteration

	startx = 10
	starty = 10

	endx = number_cells * deltashift
	endy = number_cells * deltashift
	
	pygame.draw.rect(screen, (0,0,0), (startx,starty,endx,endy), 2)
	pygame.draw.circle(screen, (255,0,0), (int(startx+(x+0.5)*deltashift),int(starty+(y+0.5)*deltashift)), 3, 3)


	for j in xrange(number_cells):
		for i in xrange(number_cells):
			
			if maze[i][j][0] == 1:
			
				placeSX = startx + i*deltashift
				placeSY = starty + j*deltashift
				placeEX = placeSX
				placeEY = placeSY + deltashift
					
				pointlist = [(placeSX,placeSY),(placeEX,placeEY)]
				pygame.draw.lines(screen, (0,0,0), False, pointlist, 1)

	for j in xrange(number_cells):
		for i in xrange(number_cells):

			if maze[i][j][2] == 1:

				placeSX = startx + i*deltashift
				placeSY = starty + j*deltashift
				placeEX = placeSX + deltashift
				placeEY = placeSY
								
				pointlist = [(placeSX,placeSY),(placeEX,placeEY)]
				pygame.draw.lines(screen, (0,0,0), False, pointlist, 1)

	
	pygame.display.flip()

