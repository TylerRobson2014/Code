from __future__ import division
import math
import random
from random import shuffle


def populate_good(grid,p,c):
	
	global size, outp
	
	stop = False
	k = 0
	
	while not(stop):

		i = grid[c]
			
		if type(i[0]) is int:
			outp[len(outp)-1].append(i)
			stop = True
			if c+1 < size:
					populate(grid,len(outp)-1,c+1)
		else:
			if k < len(i):
				j = i[k]
				outp[len(outp)-1].append(j)
				if c+1 < size:
					populate(grid,len(outp)-1,c+1)
				k += 1
				if k < len(i):
					outp.append([])
					count = 0
					for m in outp[p]:
						if count < c: outp[len(outp)-1].append(m)
						count += 1
					#p = len(outp)-1
			else:
				stop = True

def populate(grid,p,c):
	
	global size, outp
	
	stop = False
	k = 0
	
	while not(stop):

		i = grid[c]
			
		if type(i[0]) is int:
			outp[p].append(i)
			stop = True
			if c+1 < size:
					populate(grid,p,c+1)
		else:
			if k < len(i):
				j = i[k]
				outp[p].append(j)
				if c+1 < size:
					populate(grid,p,c+1)
				k += 1
				if k < len(i):
					outp.append([])
					count = 0
					for m in outp[p]:
						if count < c:
							outp[len(outp)-1].append(m)
						count += 1
					p = len(outp)-1
			else:
				stop = True


#ingrid = [[[1,0,1],[1,0,2]],[[2,0,1],[2,0,2],[2,0,3]],[[3,0,1],[3,0,2]]
ingrid = [[[1,0,1],[1,0,2]],[[2,0,1],[2,0,2],[2,0,3],[2,0,4],[2,0,5],[2,0,6]],[[3,0,1],[3,0,2]],[4,0,1],[[5,0,1],[5,0,2],[5,0,3],[5,0,4]]]
#ingrid = [[[1,0,1],[1,0,2]],[2,0,1],[[3,0,1],[3,0,2]]]
#ingrid = [[1,0,1],[2,0,1],[3,0,1]]
#ingrid = [[1,0,1],[2,0,1],[[3,0,1],[3,0,2],[3,0,3]]]
#ingrid = [[1,0,1],[[2,0,1],[2,0,2]],[3,0,1]]
outp = []
outp.append([])

p = 0
c = 0

size = len(ingrid)

populate(ingrid,p,c)
for i in outp:
	print i
