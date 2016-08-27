from __future__ import division
import math
import random

def Scalc(apples,distance):
	oldapples = apples
	tax = 1
	carry = 1000
	transfer = True
	storedapples = 0
	while transfer:
		if oldapples >= carry:
			oldapples = oldapples - carry
			storedapples = storedapples + carry - tax * distance
		elif oldapples > 0 and oldapples >= tax * distance:
			storedapples = storedapples + oldapples - tax * distance
			oldapples = 0
		else:
			storedapples = -100
			transfer = False
		if oldapples <= 0:
			transfer = False
	return storedapples


carry = 1000
S0 = 3000
tax = 1
totalD = 1000
maxS = 0
for d1 in xrange(0,1000):
	for d2 in xrange(d1,1000):
		S1 = Scalc(S0, d1)
		S2 = Scalc (S1, d2)
		d3 = totalD - (d1 + d2)
		S3 = Scalc(S2, d3)
		if S3 > maxS:
			maxS = S3
			print "Apples delivered ", S3
			print "Distances: Distance 1: ",d1,"Distance 2: ",d2,"Distance 3: ",d3
			print "Sum ", d1+d2+d3
		
