from __future__ import division
import pygame
import math
import random


background_colour = (255,255,255)
(width, height) = (800, 500)

screen = pygame.display.set_mode((width, height))
screen.fill(background_colour)

class ship():
	def __init__(self,x=100,y=400):
		(self.x,self.y) = (x,y)
		self.radius = 20

	
	def move(self,x_direction,y_direction):
		self.x += x_direction*5
		self.y += y_direction*5
		
	def shoot(self):
		global mybullets
		bull = bullet(self.x,self.y-self.radius)
		mybullets.append(bull)
	
		
	def draw(self):
		pygame.draw.circle(screen, (255,0,0), (self.x, self.y), self.radius, self.radius)


class bullet():
	def __init__(self,x,y):
		(self.x,self.y) = (x,y)
		self.radius = 5
	def __del__(self):
		pass
	def move(self):
		self.y -= 5
	def draw(self):
		pygame.draw.circle(screen, (0,0,0), (self.x, self.y), self.radius, self.radius)
	def destroy(self):
		global mybullets
		if self.y < 0:
			mybullets.pop(mybullets.index(self))		


class alien():
	def __init__(self,x=100,y=0):
		(self.x,self.y) = (x,y)
		self.radius = 20
	def __del__(self):
		pass
	def move(self):
		self.y += 0.25
	def draw(self):
		pygame.draw.circle(screen, (0,255,0), (self.x, int(self.y)), self.radius, self.radius)
	def destroy(self):
		global height, aliens, mybullets
		if self.y > height:
			aliens.pop(aliens.index(self))	
		for bullett in mybullets:
			dist2 = (self.x-bullett.x)**2 + (self.y-bullett.y)**2
			if dist2 <= self.radius**2 :
				aliens.pop(aliens.index(self))
				mybullets.pop(mybullets.index(bullett))
 
running = True
timer_event = pygame.USEREVENT + 1
pygame.time.set_timer(timer_event, 1)
screen.fill(background_colour)

(x,y) = (100,400)
mybullets = []
aliens = []
myship = ship()

down = False
up = False

(x_direction,y_direction) = (0,0)

clock_tick = 0

while running:
	clock_tick += 1
	event = pygame.event.wait()

	screen.fill(background_colour)

	fire = False

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			# User pressed down on a key
		elif event.type == pygame.KEYDOWN:
			# Figure out if it was an arrow key. If so
			# move.
			if event.key == pygame.K_LEFT:
				x_direction = -1
				down = True
				up = False
			elif event.key == pygame.K_RIGHT:
				x_direction = +1
				down = True
				up = False
			elif event.key == pygame.K_UP:
				y_direction = -1
				down = True
				up = False
			elif event.key == pygame.K_DOWN:
				y_direction = +1
				down = True
				up = False
			elif event.key == pygame.K_SPACE:
				fire = True
				down = True
				up = False
		elif event.type == pygame.KEYUP:
			down = False
			up = True
			fire = False
			(x_direction,y_direction) = (0,0)

	if not clock_tick%255:
		for i in xrange(0,width,int(width/5)):
			al = alien(i,0)
			aliens.append(al)
	if down:
		myship.move(x_direction,y_direction)
	myship.draw()
	
	if fire:
		myship.shoot()
	num_bullets = len(mybullets)
	bullets_to_delete = []
	for bullett in mybullets:
		bullett.move()
		bullett.draw()
		bullett.destroy()
	for an_alien in aliens:
		an_alien.move()
		an_alien.draw()
		an_alien.destroy()

	pygame.display.flip()

