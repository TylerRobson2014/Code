from __future__ import division
import pygame
from pygame import gfxdraw
import math
import random
from random import shuffle

background_colour = (255,255,255)
height = int(500)
width = int(500)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Lattice Gas')
screen.fill(background_colour)

def grid_create():
	global grid,size
	grid = [[[""] for i in xrange(size)] for j in xrange(size)]
	
	return grid

		
def marks_r():
	
	mark = [[[0 for i in xrange(9)] for j in xrange(25)] for k in xrange(25)]

	mark[0][0] = [7,2,1,1,7]
	mark[0][1] = [1,1,2,2,1,1]
	mark[0][2] = [1,3,1,3,1,3,1,3,1]
	mark[0][3] = [1,3,1,1,5,1,3,1]
	mark[0][4] = [1,3,1,1,4,1,3,1]
	mark[0][5] = [1,1,1,2,1,1]
	mark[0][6] = [7,1,1,1,1,1,7]
	mark[0][7] = [1,1,3]
	mark[0][8] = [2,1,2,1,8,2,1]
	mark[0][9] = [2,2,1,2,1,1,1,2]
	mark[0][10] = [1,7,3,2,1]
	mark[0][11] = [1,2,3,1,1,1,1,1]
	mark[0][12] = [4,1,1,2,6]
	mark[0][13] = [3,3,1,1,1,3,1]
	mark[0][14] = [1,2,5,2,2]
	mark[0][15] = [2,2,1,1,1,1,1,2,1]
	mark[0][16] = [1,3,3,2,1,8,1]
	mark[0][17] = [6,2,1]
	mark[0][18] = [7,1,4,1,1,3]
	mark[0][19] = [1,1,1,1,4]
	mark[0][20] = [1,3,1,3,7,1]
	mark[0][21] = [1,3,1,1,1,2,1,1,4]
	mark[0][22] = [1,3,1,4,3,3]
	mark[0][23] = [1,1,2,2,2,6,1]
	mark[0][24] = [7,1,3,2,1,1]
	
	mark[1][0] = [7,3,1,1,7]
	mark[1][1] = [1,1,2,2,1,1]
	mark[1][2] = [1,3,1,3,1,1,3,1]
	mark[1][3] = [1,3,1,1,6,1,3,1]
	mark[1][4] = [1,3,1,5,2,1,3,1]
	mark[1][5] = [1,1,2,1,1]
	mark[1][6] = [7,1,1,1,1,1,7]
	mark[1][7] = [3,3]
	mark[1][8] = [1,2,3,1,1,3,1,1,2]
	mark[1][9] = [1,1,3,2,1,1]
	mark[1][10] = [4,1,4,2,1,2]
	mark[1][11] = [1,1,1,1,1,4,1,3]
	mark[1][12] = [2,1,1,1,2,5]
	mark[1][13] = [3,2,2,6,3,1]
	mark[1][14] = [1,9,1,1,2,1]
	mark[1][15] = [2,1,2,2,3,1]
	mark[1][16] = [3,1,1,1,1,5,1]
	mark[1][17] = [1,2,2,5]
	mark[1][18] = [7,1,2,1,1,1,3]
	mark[1][19] = [1,1,2,1,2,2,1]
	mark[1][20] = [1,3,1,4,5,1]
	mark[1][21] = [1,3,1,3,10,2]
	mark[1][22] = [1,3,1,1,6,6]
	mark[1][23] = [1,1,2,1,1,2]
	mark[1][24] = [7,2,1,2,5]
	
	return mark
	
def marks_test():
	
	global size
	
	mark = [[[0 for i in xrange(9)] for j in xrange(size)] for k in xrange(size)]

	mark[0][0] = [size]
	mark[0][1] = [1]
	mark[0][2] = [1,3]
	mark[0][3] = []
	mark[0][4] = [2,1]
	
	mark[1][0] = [1,1,1]
	mark[1][1] = [1,1]
	mark[1][2] = [3]
	mark[1][3] = [1,1]
	mark[1][4] = [1,1,1]
	
	return mark
	
def marks():
	
	global size
	
	mark = [[[0 for i in xrange(9)] for j in xrange(size)] for k in xrange(size)]

	mark[0][0] = [size]
	mark[0][1] = []
	mark[0][2] = []
	mark[0][3] = [size]
	mark[0][4] = []
	#mark[0][5] = []
	#mark[0][6] = []
	#mark[0][7] = []
	#mark[0][8] = []
	#mark[0][9] = []
	
	mark[1][0] = [1,1]
	mark[1][1] = [1,1]
	mark[1][2] = [1,1]
	mark[1][3] = [1,1]
	mark[1][4] = [1,1]
	#mark[1][5] = [1,1]
	#mark[1][6] = [1,1]
	#mark[1][7] = [1]
	#mark[1][8] = [1]
	#mark[1][9] = [1]
	
	return mark

def check(d):
	count = 0
	record = []
	for i in xrange(len(d)):
		if d[i][0] == "1":
			count += 1
		if d[i][0] == "0" or d[i][0] == "":
			if count == 0:
				pass
			else:
				record.append(count)
				count = 0
	if count > 0:
		record.append(count)
		count = 0
		
	return record

def convert(constraints):
	
	global size, stringc, stringr
	
	for i in xrange(size):
		stringc.append([])
		count = 0
		for j in constraints[0][i]:
			count += 1
			for k in xrange(j):
				stringc[i].append("1")
			if count < len(constraints[0][i]):
				stringc[i].append("0")
		if len(constraints[0][i]) == 0:
			for k in xrange(size):
				stringc[i].append("0")			
	
	for i in xrange(size):
		stringr.append([])
		count = 0
		for j in constraints[1][i]:
			count += 1
			for k in xrange(j):
				stringr[i].append("1")
			if count < len(constraints[1][i]):
				stringr[i].append("0")
		if len(constraints[1][i]) == 0:
			for k in xrange(size):
				stringc[i].append("0")	
		
	print "len(stringc)",len(stringc)
	print "len(stringr)",len(stringr)	
#	print "stc",stringc
#	print "str",stringr

def pad(vec,padl,pos):
	
	global vectors,ans,vector_count
	
	print "pad: padl, pos",padl,pos

	zeros = []
	if vec[0] == "1": zeros.append(0)
	for j in xrange(len(vec)-1):
		if vec[j] == "0" and vec[j+1] == "1": zeros.append(j)
		print "test point #1"
	if vec[len(vec)-1] == "1": zeros.append(len(vec))

	if pos < len(zeros):
		print "test point #2"
#************************************************
		vector2 = []

		for jj in xrange(len(vec)):
			vector2.append(vec[jj])

		for i in xrange(padl):
			vector2.insert(zeros[pos],"0")
			print "test point #3"
			pad(vector2,padl-(i+1),pos+1)
		if padl > 0:
					
# *** Exclusion check ***************************

			reject = False
			if size == 25:
				if (vector_count == 3 and not(vector2[3] == "1")): reject = True
				if (vector_count == 3 and not(vector2[4] == "1")): reject = True
				if (vector_count == 3 and not(vector2[12] == "1")): reject = True
				if (vector_count == 3 and not(vector2[13] == "1")): reject = True
				if (vector_count == 3 and not(vector2[21] == "1")): reject = True
				if (vector_count == 8 and not(vector2[6] == "1")): reject = True
				if (vector_count == 8 and not(vector2[7] == "1")): reject = True
				if (vector_count == 8 and not(vector2[10] == "1")): reject = True
				if (vector_count == 8 and not(vector2[14] == "1")): reject = True
				if (vector_count == 8 and not(vector2[15] == "1")): reject = True
				if (vector_count == 8 and not(vector2[18] == "1")): reject = True
				if (vector_count == 16 and not(vector2[6] == "1")): reject = True
				if (vector_count == 16 and not(vector2[11] == "1")): reject = True
				if (vector_count == 16 and not(vector2[16] == "1")): reject = True
				if (vector_count == 16 and not(vector2[20] == "1")): reject = True
				if (vector_count == 21 and not(vector2[3] == "1")): reject = True
				if (vector_count == 21 and not(vector2[4] == "1")): reject = True
				if (vector_count == 21 and not(vector2[9] == "1")): reject = True
				if (vector_count == 21 and not(vector2[10] == "1")): reject = True
				if (vector_count == 21 and not(vector2[15] == "1")): reject = True
				if (vector_count == 21 and not(vector2[20] == "1")): reject = True
				if (vector_count == 21 and not(vector2[21] == "1")): reject = True				

			if size == 5:
				if (vector_count == 0 and not(vector2[0] == "1")): reject = True
				if (vector_count == 5 and not(vector2[3] == "1")): reject = True

#			print reject,vector_count,vector2
			raw_input()
			if not(reject):
				vectors.append(vector2)
				print "len(vectors)",len(vectors)

#************************************************
		print "test point #4"	
		pad(vec,padl,pos+1)
		print "test point #5"					

def solve(mygrid,constraints,testgrid):
	global size,stringc,stringr,vectors,ans,outp,vector_count
	
	testgrid = []
	
	for i in xrange(size):
		length = len(stringr[i])
		diff = size - length
		if diff == 0:
			testgrid.append(stringr[i])
		else:			
			vector = stringr[i]
			vector_count = i
			ans = []
			paddlength = diff
			pos = 0
			vectors = []
			print "Enter pad"
			pad(vector,paddlength,pos)
			print "Leave pad"
			testgrid.append(vectors)

	count_true = 0
	trog = []
	stop = False
	while not(stop):
		outp = []
		outp.append([])
		p = 0
		c = 0
		print "Enter populate"
		populate(testgrid,p,c)
		print "len(testgrid)",len(testgrid)

		trog = outp
		for j in trog:
			
			# check fixed points:
			reject = False

			if not(reject):

				count_true = 0
				coltest_z = 0
				coltest_o = 0
				strc_z = 0
				strc_o = 0
				for k in xrange(size):
					
					print "in solve: k",k

					coltotest = [j[m][k] for m in xrange(size)]

					for ccc in xrange(len(coltotest)):
						if coltotest[ccc] == "0": coltest_z += 1
						if coltotest[ccc] == "1": coltest_o += 1


					for ccc in xrange(len(stringc[k])):
						if stringc[k][ccc] == "0": strc_z += 1
						if stringc[k][ccc] == "1": strc_o += 1


					if strc_o == coltest_o:
						count_true += 1
						#print "hit"
						
				if count_true == size:
					print "The Answer is ..."
					print j
					return j
					stop = True			
				
def populate(grid,p,c):
	
	global size, outp
	
	stop = False
	k = 0
	
	print "In populate: len(grid),p,c",len(grid),p,c
	print "grid",len(grid)
	print "outp",len(outp)
	raw_input()
	
	while not(stop):

		i = grid[c]
		print "populate while loop: c",c
			
		if type(i[0]) is str:
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
						if count < c: outp[len(outp)-1].append(m)
						count += 1
					p = len(outp)-1
			else:
				stop = True
				
	
				
def printgrid(mygrid):
	global size
	for t in range(size):
		for s in range(size):
			print mygrid[t][s][0],
		print ""
		
def summ(l):
	count = 0
	for i in xrange(len(l)):
		count += int(l[i])
	return count
		
def prepop(constraints,mygrid):
	global size
	for k in xrange(2):
		count = 0
		for j in xrange(size):
			s = summ(constraints[k][j])
			count = 0
			if s + len(constraints[k][j]) - 1 == size:
				for m in xrange(len(constraints[k][j])):
					for n in xrange(int(constraints[k][j][m])):

						if k == 0 and count <= size-1:
							mygrid[j][count][0] = "1"
							count += 1
							
						if k == 1 and count <= size-1:
							mygrid[count][j][0] = "1"
							count += 1

					if k == 0 and count <= size-1:
						mygrid[j][count][0] = "0"
						count += 1

					if k == 1  and count <= size-1:
						mygrid[count][j][0] = "0"
						count += 1
	for t in range(size):
		for s in range(size):
			if len(mygrid[s][t]) > 1:
				mygrid[s][t].pop(1)
				mygrid[s][t].pop(1)

index = 0
vector_count = 0
stopall = False
rowc = 0
colc = 0
size = 5					
stringc = []
stringr = []
vectors = []
ans = []
testgrid = []
outp = []

mygrid = grid_create()
constraints = marks()
#prepop(constraints,mygrid)
#printgrid(mygrid)

convert(constraints)

newgrid = solve(mygrid,constraints,testgrid)

running = True

timer_event = pygame.USEREVENT + 1
pygame.time.set_timer(timer_event, 100)
screen.fill(background_colour)
while running:
	event = pygame.event.wait()
	
	screen.fill(background_colour)

	for j in xrange(size):
		for i in xrange(size):
			x = i*15 + 15
			y = j*15 + 15
			w = 15
			h = 15
			Rect = (x,y,w,h)
			wid = 1
			if newgrid[j][i][0] == "1": wid = 0
			pygame.draw.rect(screen, (0,0,0), Rect, wid) 

	pygame.display.flip()

