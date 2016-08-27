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

color1 = (255,0,0)

def circles(n,x,y,w):
	global positions,size
	side = w - x
	side = side / n
	size = int(side/2)
	
	for j in xrange(n):
		for i in xrange(n):
			radius = random.randint(1,size)
			#radius = size
			print radius,w - x
			posx = int(x + (2*i+1)*side/2)
			posy = int(y + (2*j+1)*side/2)
			positions.append([posx,posy,radius])

size = 0
positions = []
n = 4
w = 210
(x,y) = (10,10)
circles(n,x,y,w)
	
running = True
#rint positions
timer_event = pygame.USEREVENT + 1
pygame.time.set_timer(timer_event, 100)
screen.fill(background_colour)
while running:
	event = pygame.event.wait()
	if event.type == pygame.QUIT:
		raise StopIteration
	screen.fill(background_colour)
	
	pygame.draw.rect(screen, color1, (x,y,w-x,w-y), 1)

	for i in xrange(n*n):
		pygame.draw.circle(screen, color1, (positions[i][0],positions[i][1]), positions[i][2], 5)
		
	pygame.display.flip()

