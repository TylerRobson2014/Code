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
	limit = 1000
	side = w - x
	
	for i in xrange(n):
		test1 = False
		test2 = False
		count = 0
		while not(test1 and test2) and count < limit:
			count += 1
			c = False
			overlap = False
			radius = random.randint(1,int(side/5))
			posx = random.randint(x+radius,w-radius)
			posy = random.randint(y+radius,w-radius)
			test1 = posx + radius <= w and posx - radius >= x and posy + radius <= w and posy - radius >=y
			if len(positions) > 0:
				for j in xrange(len(positions)):
					c = math.sqrt((posx - positions[j][0])**2 + (posy - positions[j][1])**2) < (radius + positions[j][2])
					print i,test1, test2,math.sqrt((posx - positions[j][0])**2 + (posy - positions[j][1])**2) - (radius + positions[j][2])
					if c:
						overlap = True
				test2 = not(overlap)		
			else:
				test2 = True
			print "*****",test1,test2
			
		if count < limit:
			positions.append([posx,posy,radius])

size = 0
positions = []
n = 10
w = 210
(x,y) = (10,10)
circles(n,x,y,w)
	
running = True
print positions
timer_event = pygame.USEREVENT + 1
pygame.time.set_timer(timer_event, 100)
screen.fill(background_colour)
while running:
	event = pygame.event.wait()
	if event.type == pygame.QUIT:
		raise StopIteration
	screen.fill(background_colour)
	
	pygame.draw.rect(screen, color1, (x,y,w-x,w-y), 1)

	for i in xrange(len(positions)):
		pygame.draw.circle(screen, color1, (positions[i][0],positions[i][1]), positions[i][2], 1)
		
	pygame.display.flip()

