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

number_cells = 100
lattice_side = 5
lattice = [[[0 for z in xrange(4)] for x in xrange(number_cells)] for y in xrange(number_cells)]
count = 0
x = 0

def create_lattice(lattice):
	for ni in xrange(number_cells):
		for nj in xrange(number_cells):
			if not((nj)%2):
				x = ni * lattice_side / math.sqrt(2) + lattice_side
				y = nj * lattice_side / math.sqrt(2) + lattice_side
			else:
				x = (ni + 1/2) * lattice_side / math.sqrt(2) + lattice_side
				y = nj * lattice_side / math.sqrt(2) + lattice_side	
			lattice[ni][nj][0] = x
			lattice[ni][nj][1] = y
			lattice[ni][nj][2] = 0
			lattice[ni][nj][3] = (255,255,255)										


def display_lattice(lattice):
	global number_cells
	for i in xrange(number_cells):
		for j in xrange(number_cells):
			x = lattice[i][j][0]
			y = lattice[i][j][1]
			pygame.draw.circle(screen, lattice[i][j][3], (int(x), int(y)), 2, 2)

def match(lattice,i,j):
	global number_cells
	count = 0

	if i - 1 >= 0:
		if lattice[i-1][j][2]:
			count += 1

	if i+1 < number_cells:
		if lattice[i+1][j][2]:
			count += 1
				
	if i + 1 < number_cells and j - 1 >= 0:
		if lattice[i+j%2][j-1][2]:
			count += 1
									
	if i - 1 >= 0 and j - 1 >= 0:
		if lattice[i-j%2][j-1][2]:
			count += 1
				
	if i + 1 < number_cells and j + 1 < number_cells:
		if lattice[i+j%2][j+1][2]:
			count += 1

	if i - 1 >= 0 and j + 1 < number_cells:
		if lattice[i-j%2][j+1][2]:
			count += 1

	return count


def update(lattice):
	global number_cells
	count = 0
	for i in xrange(number_cells):
		for j in xrange(number_cells):
			m = match(lattice,i,j)

			if m >= 2:
				lattice[i][j][2] = 1
				lattice[i][j][3] = (178,34,34)
			if 	m > 3:	
				lattice[i][j][2] = 0
				lattice[i][j][3] = (255,255,255)
			if 	m < 2:	
				lattice[i][j][2] = 0
				lattice[i][j][3] = (255,255,255)


create_lattice(lattice)


# lattice

running = True
first_time = True
drawg = 0
for i in xrange(5):
	for j in xrange(5):
		lattice[i][j][2] = 1
		lattice[i][j][3] = (178,34,34)

timer_event = pygame.USEREVENT + 1
pygame.time.set_timer(timer_event, 500)
while running:
	event = pygame.event.wait()
	if event.type == pygame.QUIT:
		raise StopIteration

	screen.fill(background_colour)

	update(lattice)
	display_lattice(lattice)

	pygame.display.flip()
