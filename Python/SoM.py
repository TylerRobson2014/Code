from __future__ import division
import random
import numpy as np
import math
import pygame
import json

def distance(learn,outputLayer):
	mindist = 10000
	for o in outputLayer:
		dist = (o[1][0] - learn[0])**2 + (o[1][1] - learn[1])**2 + (o[1][2] - learn[2])**2
		dist = math.sqrt(dist)
		if dist < mindist:
			mindist = dist
			index = outputLayer.index(o)
	return index

background_colour = (255,255,255)
(width, height) = (500, 500)

screen = pygame.display.set_mode((width, height))
screen.fill(background_colour)

running = True
timer_event = pygame.USEREVENT + 1
pygame.time.set_timer(timer_event, 1)
screen.fill(background_colour)
# *********** My Code
inputs = []

inputs.append([255,0,0])
inputs.append([0,255,0])
inputs.append([0,0,255])
inputs.append([255,255,0])
inputs.append([0,255,255])
inputs.append([255,0,255])
#inputs.append([192,192,192])
#inputs.append([128,128,128])
#inputs.append([128,0,0])
#inputs.append([128,128,0])
#inputs.append([0,128,0])
#inputs.append([128,0,128])
#inputs.append([0,128,128])
#inputs.append([0,0,128])
#inputs.append([128,0,0])
#inputs.append([139,0,0])
#inputs.append([165,42,42])
#inputs.append([178,34,34])
#inputs.append([220,20,60])
#inputs.append([255,99,71])
#inputs.append([255,127,80])
#inputs.append([205,92,92])
#inputs.append([240,128,128])
#inputs.append([233,150,122])
#inputs.append([250,128,114])
#inputs.append([255,160,122])
#inputs.append([255,69,0])
#inputs.append([255,140,0])
#inputs.append([255,165,0])
#inputs.append([255,215,0])
#inputs.append([184,134,11])
#inputs.append([218,165,32])
#inputs.append([238,232,170])
#inputs.append([189,183,107])
#inputs.append([240,230,140])
#inputs.append([128,128,0])
#inputs.append([255,255,0])
#inputs.append([154,205,50])
#inputs.append([85,107,47])
#inputs.append([107,142,35])
#inputs.append([124,252,0])
#inputs.append([127,255,0])
#inputs.append([173,255,47])
#inputs.append([0,100,0])
#inputs.append([0,128,0])
#inputs.append([34,139,34])
#inputs.append([0,255,0])
#inputs.append([50,205,50])
#inputs.append([72,209,204])
#inputs.append([175,238,238])
#inputs.append([127,255,212])
#inputs.append([176,224,230])
#inputs.append([95,158,160])
#inputs.append([70,130,180])
#inputs.append([100,149,237])
#inputs.append([0,191,255])
#inputs.append([30,144,255])
#inputs.append([173,216,230])
#inputs.append([135,206,235])
#inputs.append([135,206,250])
#inputs.append([25,25,112])
#inputs.append([0,0,128])
#inputs.append([0,0,139])
#inputs.append([0,0,205])
#inputs.append([0,0,255])
#inputs.append([65,105,225])
#inputs.append([138,43,226])
#inputs.append([75,0,130])
#inputs.append([72,61,139])
#inputs.append([106,90,205])
#inputs.append([123,104,238])
#inputs.append([147,112,219])
#inputs.append([139,0,139])
#inputs.append([148,0,211])
#inputs.append([153,50,204])
#inputs.append([186,85,211])
#inputs.append([128,0,128])
#inputs.append([216,191,216])
#inputs.append([221,160,221])
#inputs.append([238,130,238])
#inputs.append([255,0,255])
#inputs.append([218,112,214])
#inputs.append([199,21,133])
#inputs.append([219,112,147])
#inputs.append([255,20,147])
#inputs.append([255,105,180])

#inputs.append([255,0,0])
#inputs.append([255,0,0])
#inputs.append([255,0,0])

inputDim = 3
sqrtOutDim = 20
radius = int(40/(2*math.sqrt(sqrtOutDim)))
outputDim = sqrtOutDim**2
inputLayer = inputs
ans = raw_input("Select [1] to train and [2] to test : ")
if ans == "1":
	outputLayer = [[[0,0],[random.random() for x in xrange(inputDim)]] for y in xrange(outputDim)]
	count = 0
	for countX in xrange(sqrtOutDim):
		for countY in xrange(sqrtOutDim):
			(x,y) = (int(countX*400/sqrtOutDim+50),int(countY*400/sqrtOutDim+50))
			(outputLayer[count][0][0],outputLayer[count][0][1]) = (x,y)
			count += 1
else:
	inputLayer = []
	inp = raw_input("Enter color code 1: ")
	colx = int(inp)
	inp = raw_input("Enter color code 2: ")
	coly = int(inp)
	inp = raw_input("Enter color code 3: ")
	colz = int(inp)
	inputLayer.append([colx,coly,colz])
	SOMfile = open("SOM.txt")
	outputLayer = json.load(SOMfile)	
# ** Radius
radiusn0 = sqrtOutDim * radius * 6
L0 = 0.01
# ************* Start PYGAME
mcount = 0
while running:
	event = pygame.event.wait()
	screen.fill(background_colour)
	BREAK = False
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
# ************ My code
	for i in inputLayer:
		winner = distance(i,outputLayer)
		x = outputLayer[winner][0][0]
		y = outputLayer[winner][0][1]
		if ans == "1":
			radiusn = radiusn0 * math.exp(-mcount/500)
			for j in outputLayer:
				dist = math.sqrt((j[0][0] - x)**2 + (j[0][1] - y)**2)
				L = L0 * math.exp(-mcount/500)
				PHI = math.exp(-(dist**2)/(2*radiusn**2))
				if dist <= radiusn:
					j[1][0] = j[1][0] + PHI * L * (i[0] - j[1][0])
					j[1][1] = j[1][1] + PHI * L * (i[1] - j[1][1])
					j[1][2] = j[1][2] + PHI * L * (i[2] - j[1][2])
		
	mcount += 1	

# draw

	for count in xrange(outputDim):
		x = outputLayer[count][0][0]
		y = outputLayer[count][0][1]
		if count == winner and ans == "2":
			col = (0,0,0)
			pygame.draw.circle(screen, col, (x,y), 5*radius, 5*radius)
		else:
			col = (int(outputLayer[count][1][0]),int(outputLayer[count][1][1]),int(outputLayer[count][1][2]))
			pygame.draw.circle(screen, col, (x,y), 2*radius, 2*radius)

# ************ Refresh screen
	pygame.display.update()
if ans == "1":
	target = open("SOM.txt","w")
	json.dump(outputLayer, target)
	target.close()

