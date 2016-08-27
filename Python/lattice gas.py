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

number_cells = 10
spacing = 50
lattice_side = 50
number_particles = 1
lattice = [[[0 for z in xrange(4)] for x in xrange(number_cells)] for y in xrange(number_cells)]
count = 0
x = 0

def create_lattice(lattice):
	for ni in xrange(number_cells):
		for nj in xrange(number_cells):
			if not((nj)%2):
				x = ni * lattice_side / math.sqrt(2) + lattice_side
				y = nj * lattice_side / math.sqrt(2) + lattice_side
				colour = (0,0,0)
			else:
				x = (ni + 1/2) * lattice_side / math.sqrt(2) + lattice_side
				y = nj * lattice_side / math.sqrt(2) + lattice_side
				colour = (255,0,0)	
			lattice[ni][nj][0] = x
			lattice[ni][nj][1] = y
			lattice[ni][nj][2] = -99
			lattice[ni][nj][3] = 0

def initial_pop(lattice, number_particles):
	population = number_particles
	global number_cells
#	for ni in xrange(1):
#		for nj in xrange(1):
	lattice[4][7][3] = 1
	lattice[4][7][2] = 2
	lattice[1][1][3] = 1
	lattice[1][1][2] = 5


def display_lattice(lattice):
	global number_cells
	for i in xrange(number_cells):
		for j in xrange(number_cells):
			x = lattice[i][j][0]
			y = lattice[i][j][1]
			if lattice[i][j][3] == 0:
				colour = (255,0,0)
				pygame.draw.circle(screen, colour, (int(x), int(y)), 2, 2)
			else:
				colour = (0,0,0)
				pygame.draw.circle(screen, colour, (int(x), int(y)), 4, 4)

def move(lattice):
	global number_cells
	lattice_update = [[[0 for z in xrange(4)] for x in xrange(number_cells)] for y in xrange(number_cells)]
	for i in xrange(number_cells):
		for j in xrange(number_cells):				
			lattice_update[i][j][0] = lattice[i][j][0]
			lattice_update[i][j][1] = lattice[i][j][1]
			lattice_update[i][j][2] = lattice[i][j][2]
			lattice_update[i][j][3] = lattice[i][j][3]
			
			if lattice_update[i][j][3] == 1:
				print "old i,j", i,j
				print "now",lattice_update[i][j]

	count = 0
	
	for j in xrange(number_cells):
		for i in xrange(number_cells):
			(count,array) = collision_check(lattice,i,j)
			if count == 0:
				if lattice[i][j][2] == -99:
					if lattice[i][j][3]:
						lattice_update[i][j][3] = 1
						lattice_update[i][j][2] = -99
					else:
						lattice_update[i][j][3] = 0
						lattice_update[i][j][2] = -99
				#if lattice[i][j][2] > -99:
				#	lattice_update[i][j][3] = 0
				#	lattice_update[i][j][2] = -99
			elif count == 1:
				lattice_update[i][j][3] = 1
				lattice_update[i][j][2] = lattice[array[0][0]][array[0][1]][2]
			elif count == 2:
				lattice_update[array[0][0]][array[0][1]][2] = lattice[array[1][0]][array[1][1]][2]
				lattice_update[array[1][0]][array[1][1]][2] = lattice[array[0][0]][array[0][1]][2]
#				print "new",lattice_update[array[1][0]][array[1][1]][2],lattice_update[array[0][0]][array[0][1]][2]
				lattice_update[array[0][0]][array[0][1]][3] = 1
				lattice_update[array[1][0]][array[1][1]][3] = 1
				print "update", array[0][0],array[0][1],array[1][0],array[1][1]
				print "expected",lattice_update[array[0][0]][array[0][1]]
				print "expected",lattice_update[array[1][0]][array[1][1]]
				print "expected",lattice[array[0][0]][array[0][1]]
				print "expected",lattice[array[1][0]][array[1][1]]
				

	for i in xrange(number_cells):
		for j in xrange(number_cells):				
			lattice[i][j][0] = lattice_update[i][j][0]
			lattice[i][j][1] = lattice_update[i][j][1]
			lattice[i][j][2] = lattice_update[i][j][2]
			lattice[i][j][3] = lattice_update[i][j][3]
			if lattice_update[i][j][3] != 0:
				print "new i,j", i,j
				

def collision_check(lattice,i,j):
	global number_cells
	count = 0
	neighbor = [[0,0],[0,0],[0,0],[0,0],[0,0]]
	#print i,j
	if j%2:
		if i - 1 >= 0:
			if lattice[i-1][j][3]:
				if lattice[i-1][j][2] == 0:
					print "here",0
					count = 1
					(neighbor[count-1][0],neighbor[count-1][1]) = (i-1,j)
		if i+1 < number_cells:
			if lattice[i+1][j][3]:
				if lattice[i+1][j][2] == 3:
					print "here",3
					count += 1
					(neighbor[count-1][0],neighbor[count-1][1]) = (i+1,j)
		if i + 1 < number_cells and j - 1 >= 0:
			if lattice[i+1][j-1][3]:
				if lattice[i+1][j-1][2] == 4:
					print "here",4
					count += 1
					(neighbor[count-1][0],neighbor[count-1][1]) = (i+1,j-1)
		if j - 1 >= 0:
			if lattice[i][j-1][3]:
				if lattice[i][j-1][2] == 5:
					print "here",5
					count += 1
					(neighbor[count-1][0],neighbor[count-1][1]) = (i,j-1)
		if i + 1 < number_cells and j + 1 < number_cells:
			if lattice[i+1][j+1][3]:
				if lattice[i+1][j+1][2] == 2:
					print "here",2
					count += 1
					(neighbor[count-1][0],neighbor[count-1][1]) = (i+1,j+1)
		if j + 1 < number_cells:
			if lattice[i][j+1][3]:
				if lattice[i][j+1][2] == 1:
					print "here1",1
					count += 1
					(neighbor[count-1][0],neighbor[count-1][1]) = (i,j+1)
	else:

		if i - 1 >= 0:
			if lattice[i-1][j][3]:
				if lattice[i-1][j][2] == 0:
					print "here",0
					count = 1
					(neighbor[count-1][0],neighbor[count-1][1]) = (i-1,j)
		if i+1 < number_cells:
			if lattice[i+1][j][3]:
				if lattice[i+1][j][2] == 3:
					print "here",3
					count += 1
					(neighbor[count-1][0],neighbor[count-1][1]) = (i+1,j)
		if j - 1 >= 0:
			if lattice[i][j-1][3]:
				if lattice[i][j-1][2] == 4:
					print "here",4
					count += 1
					(neighbor[count-1][0],neighbor[count-1][1]) = (i,j-1)
		if i - 1 >= 0 and j - 1 >= 0:
			if lattice[i-1][j-1][3]:
				if lattice[i-1][j-1][2] == 5:
					print "here",5
					count += 1
					(neighbor[count-1][0],neighbor[count-1][1]) = (i-1,j-1)
		if j + 1 < number_cells:
			if lattice[i][j+1][3]:
				if lattice[i][j+1][2] == 2:
					print "here",2
					count += 1
					(neighbor[count-1][0],neighbor[count-1][1]) = (i,j+1)
		if i - 1 >= 0 and j + 1 < number_cells:
			if lattice[i-1][j+1][3]:
				if lattice[i-1][j+1][2] == 1:
					print "here2",1
					count += 1
					(neighbor[count-1][0],neighbor[count-1][1]) = (i-1,j+1)
		
	return (count,neighbor)

create_lattice(lattice)
initial_pop(lattice,number_particles)

# lattice

running = True
timer_event = pygame.USEREVENT + 1
pygame.time.set_timer(timer_event, 1000)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

	screen.fill(background_colour)
	
	display_lattice(lattice)
	
	#raw_input()
	
	move(lattice)

    pygame.display.flip()
