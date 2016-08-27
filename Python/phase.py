from __future__ import division
import pygame
from pygame import gfxdraw
import math
import random
from random import shuffle

background_colour = (255,255,255)
height = int(600)
width = int(600)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Lattice Gas')
screen.fill(background_colour)




running = True

color = (0,0,0)

count = 0

maximum = 200

timer_event = pygame.USEREVENT + 1
pygame.time.set_timer(timer_event, 1)
screen.fill(background_colour)
while running:
	event = pygame.event.wait()
	
	screen.fill(background_colour)
	
	if event.type == pygame.QUIT:
		raise StopIteration

	
	for i in xrange(1,maximum):
		if i % 2:
			color = (0,0,0)#(255,255,0)
		else:
			color = (0,0,0)
		start_angle = count*i
		stop_angle = math.pi + count*i
		x = 250-i*(250/maximum)
		y = 250-i*(250/maximum)
		w = (500/maximum)*i
		h = (500/maximum)*i
		thickness = int(200/maximum)
		pygame.draw.arc(screen, color, (x,y,w,h), start_angle, stop_angle, thickness)
		
	count += 0.005

	pygame.display.flip()

