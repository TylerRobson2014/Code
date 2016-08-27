from __future__ import division
import pygame
from pygame import gfxdraw
import math
import random
from random import shuffle

background_colour = (255,255,255)
height = int(700)
width = int(850)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Lattice Gas')
screen.fill(background_colour)

#### define maze ####

def shape(sx,sy,ex,ey):
	startx = sx 
	starty = sy
	endx = ex
	endy = ey
	
	pygame.draw.line(screen, (0,0,255), (startx,starty),(endx,endy), 1)
		

def draw(leg,i,d,angle):
	global A,sx,sy,endx,endy
		
	for j in xrange(4):
		
		if j == 0 or j == 3:
			angle1 = angle

		if j == 1:
			angle1 = -math.pi * (A/180) + angle
		
		if j == 2:
			angle1 = math.pi * (A/180) + (angle)
		
		if i == d:
			#print "ss",sx,"se",endx
			endx = math.cos(angle1)*leg+sx
			endy = math.sin(angle1)*leg+sy
			shape(sx,sy,endx,endy)
			sx = endx
			sy = endy
			#raw_input()
		else:
			#print "ds",sx,"de",endx
			draw(leg/3,i+1,d,angle1)
			#raw_input()



A = 89
k = 1

running = True

timer_event = pygame.USEREVENT + 1
pygame.time.set_timer(timer_event, 500)
screen.fill(background_colour)
while running:
	event = pygame.event.wait()
	if event.type == pygame.QUIT:
		raise StopIteration

	screen.fill(background_colour)

	angle = 0

	sx = 25
	sy = 400
	leg = 100*k
	if k < 9:
		r = k
	draw(leg,1,r,0)
	k = k+1
	raw_input()
	#draw(350,100,350,350,1,k,math.pi/2)
	#draw(350,350,100,350,1,k,math.pi)
	#draw(100,350,100,100,1,k,3*math.pi/2)
		
	pygame.display.flip()

