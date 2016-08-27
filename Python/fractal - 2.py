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

def shape(sx,sy,ex,ey):
	startx = sx 
	starty = sy
	endx = ex
	endy = ey

	pygame.draw.line(screen, (0,0,255), (int(startx),int(starty)),(int(endx),int(endy)), 1)
	#pygame.draw.circle(screen, (0,0,255), (int(startx),int(starty)), 3, 3)	

def draw(sx,sy,ex,ey,i,d,angle):
	
	l = math.sqrt((sx-ex)**2 + (sy-ey)**2)
		
	for j in xrange(4):
		
		if j == 0 or j == 3:
			angle1 = angle

		if j == 1 or j == 2:
			angle1 = ((-1)**(j))*math.pi/3 + angle
			
		endx = math.cos(angle1)*l/(3)+sx
		endy = math.sin(angle1)*l/(3)+sy
		
		if i == d:
			shape(sx,sy,endx,endy)
		else:
			draw(sx,sy,endx,endy,i+1,d,angle1)
		
		sx = endx
		sy = endy


running = True

timer_event = pygame.USEREVENT + 1
pygame.time.set_timer(timer_event, 500)
screen.fill(background_colour)
while running:
	event = pygame.event.wait()
	if event.type == pygame.QUIT:
		raise StopIteration


	angle = 0
	k = 5
	
	draw(100,100,350,100,1,k,0)
	draw(350,100,350,350,1,k,math.pi/2)
	draw(350,350,100,350,1,k,math.pi)
	draw(100,350,100,100,1,k,3*math.pi/2)
		
	pygame.display.flip()

