from __future__ import division
import pygame
from pygame import gfxdraw
import math
import random


background_colour = (255,255,255)
(width, height) = (500, 500)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Flock')
screen.fill(background_colour)
blue = (0, 0, 255)		

x = 100
y = 0

point2 = (x,y)

running = True
count = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

	screen.fill(background_colour)

	x1 = x
	y1 = y

	x = x1*math.cos(-count*0.001) - y1*math.sin(-count*0.001)
	y = x1*math.sin(-count*0.001) + y1*math.cos(-count*0.001)
	
	pygame.draw.line(screen, blue, (200,200), (x+200,y+200))
	
	count = count + 1

	pygame.display.flip()

