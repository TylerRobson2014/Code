from __future__ import division
import pygame
import math

coins = [9,8,7,6,5,4,3,2,1]

money = 111
mychange = []
memory = []
minlength = 1000000

def change(cash,level,memory):
	global coins
	global mychange
	global minlength
	
	for coin in [c for c in coins if c <= cash]:
		if level <= minlength:
			if level == 0:
				memory = []
			memory.append(coin)
			change(cash - coin,level+1,memory)
	if cash == 0:
		if len(memory) < minlength:
			minlength = len(memory)
			mychange = memory
	while len(memory) > minlength:
		memory.pop()



change(money,0,memory)
print "The required change is: ",mychange


