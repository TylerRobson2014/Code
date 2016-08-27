from __future__ import division
import pygame
from pygame import gfxdraw
import math
import random
from random import shuffle
import numpy as np
import matplotlib.pyplot as plt

background_colour = (255,255,255)
height = int(500)
width = int(600)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Evolution')
screen.fill(background_colour)

# ****************** Main def Block ****************
class creature(object):
	def __init__(self,name,pred,size,view,attraction,fertility,(x,y),healrate,agression,direction,globaltime,lifespan):
		self.name = name
		self.x = x
		self.y = y
		self.birthd = globaltime
		self.size = size
		self.Maxsize = size
		self.strength = 1*self.size
		self.Maxstrength = self.strength
		self.resistance = self.size
		self.attraction = attraction
		self.fertitility = fertility
		self.maxfert = self.fertitility
		self.view = view
		if self.view > math.pi/2: self.view = math.pi/2
		self.healrate = healrate
		self.agression = agression
		self.direction = direction
		self.pred = pred
		self.lifespan = lifespan
		self.sex = random.randint(1,2)
		if self.sex == 1:
			self.sex = "M"
			self.color = (255,0,0)
			if self.pred == 1: self.color = (0,0,205)
			self.speed = random.randint(30,35)/(self.size * self.attraction)
		if self.sex == 2:
			self.sex = "F"
			self.color = (0,0,0)
			if self.pred == 1: self.color = (253,253,0)
			self.speed = (random.randint(30,35)/self.size)	
		if self.speed < 0: self.speed = 0
		self.Maxspeed = self.speed
		#self.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
		self.dead = False
		self.attacked = False
		self.eaten = False
		self.mate = True
		self.pregnant = False
		self.gestation = 0
		self.hungry = 100
		
	def decide(self):
		count = 0
		global creatures,globaltime
		close = False
		
		for c in creatures:
			if not(c.name == self.name):
				if self.pred == c.pred:
						
					attackZone = 15*int(1+abs(self.view)/(math.pi/2))
					#print attackZone
					if (self.x - c.x)**2 + (self.y - c.y)**2 < (attackZone)**2:
						close = True
						anglebetweencreatures = math.atan2((c.y - self.y),(c.x - self.x))
						if anglebetweencreatures < 0 : anglebetweencreatures += 2 * math.pi
						if self.mate == True:
							if self.sex == "F":
								if c.attraction > 3:
									if self.fertitility > 3 and self.hungry > 40 and globaltime - self.birthd > self.lifespan/1000:
										if self.pregnant == False:
											self. pregnant = True
											self.fertitility = 0
											self.gestation = globaltime
											#print "Mate"
						if self.eaten == True:
							self.dead = True
							print "got me"
						else:		
							if self.attacked == True:
								if self.agression == 5:
									#print "Attacked and attacking back"
									self.attack(count,anglebetweencreatures)
								else:
									#print "Attacked and flee"
									self.attack(count,anglebetweencreatures)
									self.flee(anglebetweencreatures)
							else:						
								first_cond = anglebetweencreatures < self.direction + self.view
								second_cond = anglebetweencreatures > self.direction - self.view
								if first_cond and second_cond:
									diffStrength = self.strength - c.strength
									diffAgression = self.agression - c.agression
									diffSpeed = self.speed - c.speed
									pygame.draw.line(screen, (0,0,0), (int(self.x),int(self.y)), (int(c.x),int(c.y)), 1)
									pygame.draw.circle(screen, self.color, (int(self.x),int(self.y)), attackZone, 1)
									#raw_input()
									if self.sex == c.sex:
										if diffStrength < 0:
											if self.agression == 5:
												#print "weak but attack"
												self.attack(count,anglebetweencreatures)
											else:
												#print "flee"
												self.flee(anglebetweencreatures)
										else:
											if self.agression > 3:
												#print "attack"
												c.attacked = True
												#print "being att", c.name,c.attacked
												self.attack(count,anglebetweencreatures)
											else:
												pass
												#print "not aggressive - leave alone"
									else:
										if self.sex == "M":
											c.mate = True
											#print "ask mate"
										if self.sex == "F":
											#print "choose mate",c.attraction ,self.fertitility,self.pregnant
											if c.attraction > 3:
												if self.fertitility > 3 and self.hungry > 40 and globaltime - self.birthd > self.lifespan/1000:
													if self.pregnant == False:
														self.pregnant = True
														self.fertitility = 0
														#print "Mate"
														self.gestation = globaltime								
				else:
					#print "eat1"
					if self.pred == 1:
						attackZone = int(10*(1+(math.pi/2)/(abs(self.view))))
						#print attackZone
						if (self.x - c.x)**2 + (self.y - c.y)**2 < (attackZone)**2:
							close = True
							anglebetweencreatures = math.atan2((c.y - self.y),(c.x - self.x))
							if anglebetweencreatures < 0 : anglebetweencreatures += 2 * math.pi
						#print "eat2"
							if self.agression > 3 and self.speed > c.speed and self.hungry < 100 and c.size < 1.8 * self.size:
								pygame.draw.line(screen, (0,0,0), (int(self.x),int(self.y)), (int(c.x),int(c.y)), 1)
								pygame.draw.circle(screen, self.color, (int(self.x),int(self.y)), attackZone, 1)
								#raw_input()
								#print "eat3"
								c.eaten = True
								self.eat(count,anglebetweencreatures)
					else:
						attackZone = 20*int(1+abs(self.view)/(math.pi/2))
						#print attackZone
						if (self.x - c.x)**2 + (self.y - c.y)**2 < (attackZone)**2:
							close = True
							anglebetweencreatures = math.atan2((c.y - self.y),(c.x - self.x))
							if anglebetweencreatures < 0 : anglebetweencreatures += 2 * math.pi
							self.flee(anglebetweencreatures)	
					
			count += 1											
		if not(close):
			self.attacked = False
			self.eaten = False	
	
	def checkattacked(self):
		global creatures,attackzone
		attacked = False
		for c in creatures:
			if not(c.name == self.name):
				if (self.x - c.x)**2 + (self.y - c.y)**2 < attackZone**2:
					attacked = True				
					c.attacked = attacked
	
	def setfert(self):
		global globaltime
		if self.sex == "F":
			if self.pregnant == False:
				if self.fertitility < self.maxfert:
					self.fertitility += 0.005
				
	def eat(self,creatureName,angle):
		global globaltime,creatures
		self.direction = angle
		if not(self.eaten):
			factorAttacker = 1.5
			if self.size < self.Maxsize:	
				self.speed = factorAttacker * self.speed
				self.strength = factorAttacker * self.strength
				self.size = factorAttacker * self.size
				self.resistance = self.size
		else:
			self.dead = True
			print "eaten"
					
					
	def attack(self,creatureName,angle):
		self.injure(creatureName)
		if self.agression >= 4 and not(self.attacked):
			self.direction = angle
						
	def injure(self,creatureName):
		global creatures
		
		if not(self.attacked):
			factorAttacker = 1 - 1/(3*self.resistance)
				
			self.speed = factorAttacker * self.speed
			self.strength = factorAttacker * self.strength
			self.size = factorAttacker * self.size
			self.resistance = self.size

		else:
			factorAttacked = 1 - 1/self.resistance

			self.speed = factorAttacked * self.speed
			self.strength = factorAttacked  * self.strength
			self.size = factorAttacked  * self.size
			self.resistance = self.size
		
	def heal(self):
		if self.speed < self.Maxspeed:
			self.speed = self.healrate * self.speed
		if self.strength < self.Maxstrength:
			self.strength = self.healrate* self.strength
			self.size = self.healrate * self.size
			self.resistance = self.size

	def flee(self,angle):
		if angle > math.pi:
			angle -= math.pi
		elif angle <= math.pi:
			angle += math.pi
		self.direction = angle

	def birth(self):
		global globaltime,creatures
		loop = 1
		if self.fertitility > 6: loop = 2
		if self.fertitility > 8: loop = 3
		if self.pregnant == True:
			if globaltime - self.gestation >= 20:
				for jj in xrange(loop):
					print "Give brith"
					self.pregnant = False
					self.gestation = 0
					direction = random.uniform(0,2*math.pi)
					name = len(creatures)
					pred = self.pred

					size = random.gauss(self.Maxsize,self.Maxsize/10)
					attraction = random.gauss(self.attraction,self.attraction/10)
					fertility = random.gauss(self.maxfert,self.maxfert/10)
					view = random.gauss(self.view,self.view/10)
					healrate = random.gauss(self.healrate,self.healrate/10)
					agression = random.gauss(self.agression,self.agression/10)
					lifespan = random.gauss(self.lifespan,self.lifespan/100)
					x = random.randint(0,400)
					y = random.randint(0,400)
					
					creatures.append(creature(name,pred,size,view,attraction,fertility,(x,y),healrate,agression,direction,globaltime,lifespan))
				
	def feed(self):
		global food
		feedZone = 30*self.view/(math.pi/2)
		if self.pred == 2:
			for fee in food:
				if (self.x - fee.x)**2 + (self.y - fee.y)**2 < feedZone**2:
					factor = (1 + fee.nutritionValue/200)*self.healrate
					self.hungry *= factor
					if self.hungry > 100: self.hungry = 100
					self.speed = (self.hungry/100) * self.speed
					self.strength = (self.hungry/100) * self.strength
					self.size = (self.hungry/100) * self.size
					self.resistance = self.size
					fee.consumed()
	def reproduce(self):
		pass
	def hunger(self):
		factor = 0.9999999#0.99999
		#print factor
		self.hungry *= factor
		self.speed = (self.hungry/100)  * self.speed
		self.strength = (self.hungry/100) * self.strength
		self.size = (self.hungry/100) * self.size
		self.resistance = self.size
		
		
	def age(self):
		global globaltime
		if globaltime - self.birthd > self.lifespan/4:
			factor = 1.0/((globaltime - self.birthd) + 1)
			self.speed = factor * self.speed
			self.Maxspeed = self.speed
			self.strength = factor * self.strength
			self.Maxstrength = self.strength
			self.healrate = factor * self.healrate
			self.maxfert = factor * self.maxfert
			self.size = factor * self.size
			self.Maxsize = self.size
			self.resistance = self.size

	def die(self):
		global globaltime
		if globaltime - self.birthd > self.lifespan: self.dead = True
		if self.strength <= 1: self.dead = True

	def move(self):
		global width,height
		
		#print self.x,self.y,self.direction
		flag = 0
		if self.x > width or self.x < 0:
			self.direction = self.direction + math.pi/4
			if self.direction > 2 * math.pi: self.direction -= 2 * math.pi
			flag = 1
		if self.y > height or self.y < 0:
			if not(flag):
				self.direction = self.direction + math.pi/4
				if self.direction > 2 * math.pi: self.direction -= 2 * math.pi
		
		self.x = self.x + self.speed * math.cos(self.direction)
		self.y = self.y + self.speed * math.sin(self.direction)
		#print self.x,self.y,self.direction	
		
	def display(self):
		pygame.draw.circle(screen, self.color, (int(self.x),int(self.y)), int(self.size), int(self.size))
		pygame.draw.line(screen, (0,0,0), (int(self.x),int(self.y)), (int(self.x+(self.size*5)*math.cos(self.direction)), int(self.y+(self.size*5)*math.sin(self.direction))), 1)
		pygame.draw.line(screen, (0,0,0), (int(self.x),int(self.y)), (int(self.x+(self.size*5)*math.cos(self.direction+self.view)), int(self.y+(self.size*5)*math.sin(self.direction+self.view))), 1)
		pygame.draw.line(screen, (0,0,0), (int(self.x),int(self.y)), (int(self.x+(self.size*5)*math.cos(self.direction-self.view)), int(self.y+(self.size*5)*math.sin(self.direction-self.view))), 1)


class Food(object):
	def __init__(self):
		(self.x,self.y) = (random.randint(0,width),random.randint(0,height))
		self.MaxnutritionValue = random.randint(1,5)
		self.poisonValue = random.randint(1,5)
		self.growthRate = random.uniform(0.001,0.008)
		self.nutritionValue  = 0
		self.size = 0
	def grow(self):
		if self.size < 5:
			self.size = (self.size + self.growthRate)
			self.nutritionValue = (self.size/5)*self.MaxnutritionValue
	def consumed(self):
		self.size = (0.50 * self.size)
		
	def display(self):
		color = (5,5,5)
		pygame.draw.circle(screen, color, (int(self.x),int(self.y)), int(self.size), int(self.size))
	

# **********************************************

# ****************** creation block ************
number_of_creatures = 10

creatures = []
globaltime = 0


for i in xrange(number_of_creatures):
	x = random.randint(0,400)
	y = random.randint(0,400)
	direction = random.uniform(0,2*math.pi)
	name = i
	
	size = random.randint(5,10)
	attraction = random.randint(1,10)
	fertility = random.randint(1,10)
	view = random.uniform(math.pi/20,math.pi/2)
	healrate = random.uniform(1,1.05)
	agression = random.randint(1,5)
	lifespan = random.gauss(15000,1000)
	pred = random.randint(1,2)
	
	creatures.append(creature(name,pred,size,view,attraction,fertility,(x,y),healrate,agression,direction,globaltime,lifespan))
	
amount_of_food = 100
attackZone = 30

food = []

for i in xrange(amount_of_food):
	food.append(Food())

# **********************************************

# ****************** Set params ****************


# **********************************************

running = True

#** Gather stats **

population_count = []
males_count = []
females_count = []
faggression_check = []
fertility_count = []
fspeed_count = []
fsize_count = []
fmaxsize_count = []
fhunger_count = []
fview_count = []
flife_count = []
fhealrate_count = []
maggression_check = []
mattraction_count = []
#fertility_count = []
mspeed_count = []
msize_count = []
mmaxsize_count = []
mhunger_count = []
mview_count = []
mhealrate_count = []
mlife_count = []
pred_count = []
pred

#*******************

timer_event = pygame.USEREVENT + 1
pygame.time.set_timer(timer_event, 1)
screen.fill(background_colour)
while running:
	event = pygame.event.wait()
	
	screen.fill(background_colour)
	
	if event.type == pygame.QUIT:
		raise StopIteration

# **************** screen block ********************
	count = 0
	males = 0
	females = 0
	maggress = 0
	mattraction = 0
	#fert = 0
	mspee = 0
	mmaxsiz = 0
	msiz = 0
	mhung = 0
	mvie = 0
	mhealrate = 0
	faggress = 0
	fert = 0
	fspee = 0
	fmaxsiz = 0
	fsiz = 0
	fhung = 0
	fvie = 0
	fhealrate = 0
	mlife = 0
	flife = 0
	pred = 0
	population_count.append(len(creatures))
	for creat in creatures:
		pred += creat.pred
		if creat.sex == "M":
			males += 1
			maggress += creat.agression
			#fert += creat.maxfert
			mspee += creat.Maxspeed
			msiz += creat.size
			mmaxsiz += creat.Maxsize
			mhung += creat.hungry
			mvie += creat.view
			mattraction += creat.attraction
			mhealrate += creat.healrate
			mlife += creat.lifespan
		if creat.sex == "F":
			females += 1
			faggress += creat.agression
			fert += creat.maxfert
			fspee += creat.Maxspeed
			fsiz += creat.size
			fmaxsiz += creat.Maxsize
			fhung += creat.hungry
			fvie += creat.view
			fhealrate += creat.healrate
			flife += creat.lifespan
		creat.display()
		creat.move()
		creat.setfert()
		creat.hunger()
		creat.feed()
		creat.decide()
		if creat.dead: print "DEAD"
		if creat.dead: creatures.pop(count)
#		creat.checkattacked()
		creat.birth()
		creat.age()
		creat.die()
		if creat.dead: creatures.pop(count)
		count += 1
	if len(creatures) > 0:
		pred_count.append(pred/len(creatures))
	if males > 0 and len(creatures) > 0: 
		maggression_check.append(maggress/males)
		males_count.append(males/len(creatures))
		females_count.append(females/males)
		#fertility_count.append(fert/len(creatures))
		mspeed_count.append(mspee/males)
		mhunger_count.append(mhung/males)
		msize_count.append(msiz/males)
		mmaxsize_count.append(mmaxsiz/males)
		mview_count.append(mvie/males)
		mattraction_count.append(mattraction/males)
		mhealrate_count.append(mhealrate/males)
		mlife_count.append(mlife/males)
	if females > 0 and len(creatures) > 0: 
		faggression_check.append(faggress/females)
		#males_count.append(males/len(creatures))
		females_count.append(females/len(creatures))
		fertility_count.append(fert/females)
		fspeed_count.append(fspee/females)
		fhunger_count.append(fhung/females)
		fsize_count.append(fsiz/females)
		fmaxsize_count.append(fmaxsiz/females)
		fview_count.append(fvie/females)
		fhealrate_count.append(fhealrate/females)
		flife_count.append(flife/females)
	for foo in food:
		foo.grow()
		foo.display()
# ***************************************************
	globaltime += 1
	#print globaltime
	if globaltime > 10000 or len(creatures) == 0: running = False
	pygame.display.flip()
	
plt.plot(population_count)
plt.ylabel('population_count')
plt.show()
plt.plot(females_count)
plt.ylabel('females_count')
plt.show()
plt.plot(faggression_check)
plt.ylabel('faggression_check')
plt.show()
plt.plot(fertility_count)
plt.ylabel('fertility_count')
plt.show()
plt.plot(fspeed_count)
plt.ylabel('fspeed_count')
plt.show()
plt.plot(fsize_count)
plt.ylabel('fsize_count')
plt.show()
plt.plot(fmaxsize_count)
plt.ylabel('fmaxsize_count')
plt.show()
plt.plot(fhunger_count)
plt.ylabel('fhunger_count')
plt.show()
plt.plot(fview_count)
plt.ylabel('fview_count')
plt.show()
plt.plot(fhealrate_count)
plt.ylabel('fhealrate_count')
plt.show()
plt.plot(flife_count)
plt.ylabel('flife_count')
plt.show()

plt.plot(males_count)
plt.ylabel('males_count')
plt.show()
plt.plot(maggression_check)
plt.ylabel('maggression_check')
plt.show()
plt.plot(mattraction_count)
plt.ylabel('mattraction_count')
plt.show()
plt.plot(mspeed_count)
plt.ylabel('mspeed_count')
plt.show()
plt.plot(msize_count)
plt.ylabel('msize_count')
plt.show()
plt.plot(mmaxsize_count)
plt.ylabel('mmaxsize_count')
plt.show()
plt.plot(mhunger_count)
plt.ylabel('mhunger_count')
plt.show()
plt.plot(mview_count)
plt.ylabel('mview_count')
plt.show()
plt.plot(fhealrate_count)
plt.ylabel('fhealrate_count')
plt.show()
plt.plot(mlife_count)
plt.ylabel('mlife_count')
plt.show()
