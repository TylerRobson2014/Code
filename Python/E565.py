from __future__ import division
import pygame
from pygame import gfxdraw
import math
import random
import sys
from copy import deepcopy
import matplotlib.pyplot as plt
#import numpy as np

def getDivisors(n):
	div = []
	for i in xrange(1,n+1):
		if not(n % i): div.append(i)
	return div

results = []
index = []
upp = 101
low = 100
diff = []
for maxN in xrange(low,upp):

	#diviS = int(raw_input("Input the divisor : "))
	diviS = 5
	answers = []
	for n in xrange(4,maxN+1):
		divisors = getDivisors(n)
		sumD = sum(divisors)
		if not(sumD % diviS):
			answers.append(n)
			index.append(n)
			#print n
	if sum(answers) > 0:
		results.append(sum(answers))
	
	old_k = 0
	for k in index:
		print k-old_k
		diff.append(k-old_k)
		old_k = k
		
		
	#print results

	old_r = 0
	count = low
	c = []
	d = []
	z = []
	nz = []
	for r in results:
		#print r
		d.append(r-old_r)
		if r - old_r == 0:
			z.append(count)
		else:
			nz.append(count)
		old_r = r
		count += 1


#plt.plot(results)
#plt.show()
plt.plot(index)
plt.show()
plt.plot(diff)
plt.show()
plt.plot(z)
plt.show()
plt.plot(nz)
plt.show()
