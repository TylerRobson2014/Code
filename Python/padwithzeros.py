from __future__ import division
import math
import random
from random import shuffle

def pad(index,vec,padl,pos):
	
	global vectors,a,stop

	zeros = []
	if vec[0] == 1: zeros.append(0)
	for j in xrange(len(vec)-1):
		if vec[j] == 0 and vec[j+1] == 1: zeros.append(j)
	if vec[len(vec)-1] == 1: zeros.append(len(vec))

	if pos < len(zeros):

#************************************************
		vector2 = []

		for jj in xrange(len(vec)):
			vector2.append(vec[jj])

		for i in xrange(padl):
			vector2.insert(zeros[pos],0)
			dummy = pad(index,vector2,padl-(i+1),pos+1)
		if padl > 0:
			vectors.append(vector2)
			if len(vectors) == index:
				a = vector2
#************************************************
			
			pad(index,vec,padl,pos+1)	

vector = [1,1,0,1]
vectors = []
a = []
stop = 0
paddlength = 5
pos = 0
index = 2
pad(index,vector,paddlength,pos)
for i in vectors:
	print i
	raw_input()

