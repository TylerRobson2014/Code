from __future__ import division
import pygame
from pygame import gfxdraw
import math
import random
import sys

def toss_coin():
	r = random.randint(1,2)
	if r == 1:
		return "heads"
	if r == 2:
		return "tails"

number_of_tries = 10000

count_too_many = 0

maximum = 1000

for i in xrange(number_of_tries):
	
	cost_per_game = 2
	fortune = 5
	pot = 1
	count_games = 0
	too_many = False

	while (fortune >= cost_per_game) and not(too_many):
		pot = 1
		count_games += 1
		if count_games > maximum:
			too_many = True
			count_too_many += 1
			
		fortune -= cost_per_game
		
		coin = toss_coin()
		
		while (coin == "heads"):
			pot *= 2
			coin = toss_coin()
		win = pot
		fortune += win

		
print "probablity of playing 4 ever = ", count_too_many/number_of_tries
	
print "Finished"
		
