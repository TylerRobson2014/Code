from __future__ import division
import pygame
from pygame import gfxdraw
import math
import random

background_colour = (255,255,255)
height = int(500)
width = int(500)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Lattice Gas')
screen.fill(background_colour)


running = True
drawg = 0
timer_event = pygame.USEREVENT + 1
pygame.time.set_timer(timer_event, 1000)
while running:
	event = pygame.event.wait()
	if event.type == pygame.QUIT:
		raise StopIteration
	if event.type == pygame.MOUSEBUTTONDOWN:
		drawg = 1
	if event.type == pygame.MOUSEBUTTONUP:
		drawg = 0
	if event.type == pygame.MOUSEMOTION:
		if drawg:
			(x,y) = pygame.mouse.get_pos()
			pygame.draw.circle(screen, (178,34,34), (int(x), int(y)), 2, 2)

	pygame.display.flip()
