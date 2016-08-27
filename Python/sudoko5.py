import sys
import time
import datetime

def setup(grid):
	problem25 = "85...24..72......9..4.........1.7..23.5...9...4...........8..7..17..........36.4."
	problem26 = "..............3.85..1.2.......5.7.....4...1...9.......5......73..2.1........4...9"
	problem27 = "..3......4.6.......8.231..62...9..715.......8....4...3....7...........9...1.68..7"
	problem28 = "...16..2...2...8.5..5..36.9....5.18...........96.7....1.89..3..4.9...7...5..16..."
	problem29 = "..6...94.9.....3....4.92...6.7.1..2.5.23.64.9.3..4.7.5...68.5....5.....4.98...1.."
	problem30 = "...28.94.1.4...7......156.....8..57.4.......8.68..9.....196......5...8.3.43.28..."
	problem31 = "53..7....6..195....98....6.8...6...34..8.3..17...2...6.6....28....419..5....8..79"
	offset = -1
	for i in range(9):
		offset += 1
		for j in range(9):
			grid[i][j][0] = problem25[offset*9+j]
			if grid[i][j][0] != ".":
				for m in range(1,10):
					try:
						grid[i][j].pop(len(grid[i][j])-1)
					except:
						e = sys.exc_info()[0]
def printgrid(grid):
	for t in range(9):
		for s in range(9):
			print grid[t][s][0],
		print ""
	print "++++++++++++++++"

		
def checkRow(grid,i,j):
	for k in range(9):
		if k != j:
			if grid[i][k][0] != ".":
				try:
					grid[i][j].pop(grid[i][j].index(grid[i][k][0]))
				except:
					e = sys.exc_info()[0]

					
			
def checkColumn(grid,i,j):
	if grid[i][j][0] == ".":
		for k in range(9):
			if k != i:
				if grid[k][j][0] != ".":
					try:
						grid[i][j].pop(grid[i][j].index(grid[k][j][0]))
					except:
						e = sys.exc_info()[0]
					
						
def checkSquare(grid,i,j,xx,yy):
	if grid[i][j][0] == ".":
		if i in range(xx-3,xx):
			if j in range(yy-3,yy):
				for k in range(xx-3,xx):
					for l in range(yy-3,yy):
						if grid[k][l][0] != ".":
							try:
								grid[i][j].pop(grid[i][j].index(grid[k][l][0]))
							except:
								e = sys.exc_info()[0]			

def checkGrid(grid,i,j):

	checkColumn(grid,i,j)

	checkRow(grid,i,j)

	for xx in range(3,10,3):
		for yy in range(3,10,3):
			checkSquare(grid,i,j,xx,yy)
	
def simplify(arr,grid,res):
	minimum = 10000
	for i in range(len(arr)):
		xi = arr[i][0]
		yi = arr[i][1]
		if len(grid[xi][yi]) < minimum:
			minimum = len(grid[xi][yi])
			topop = i
	try:
		res.append(arr[topop])
		arr.pop(topop)
	except:
		e = sys.exc_info()[0]
	
	if len(arr) > 0:
		simplify(arr,grid,res)
	
def solve(mylist,p):

	global clash
	global grid
	global stopall
	
	if not(stopall):
		x = mylist[p][0]
		y = mylist[p][1]

		for d in range(1,len(grid[x][y])):
			
			grid[x][y][0] = grid[x][y][d]
			#printgrid(grid)
			
			clash = 0
												
			for kk in range(9):

				if grid[kk][y][0] == grid[x][y][0] and kk != x  and (grid[x][y][0] != "."):
							
					clash = 1
					grid[x][y][0] = "."

				if grid[x][kk][0] == grid[x][y][0] and kk != y  and (grid[x][y][0] != "."):
							
					clash = 1
					grid[x][y][0] = "."	
					
				for xx in range(3,10,3):
					for yy in range(3,10,3):
						
						if x in range(xx-3,xx):
							if y in range(yy-3,yy):
								for mm in range(xx-3,xx):
									for nn in range(yy-3,yy):
										if grid[mm][nn][0] == grid[x][y][0] and (mm != x and nn !=y) and (grid[x][y][0] != "."):
											clash = 1
											grid[x][y][0] = "."	
								
			if not(clash):
				flag = 0
				for mmm in range(9):
					for nnn in range(9):
						if grid[mmm][nnn][0] == ".":
							flag = 1
				if not(flag) and not(clash):
					print "***  SOLVED  ***"
					printgrid(grid)
					stopall = True
					
					#filename = raw_input()

				solve(mylist,p+1)
				if clash:
					grid[x][y][0] = "."
				
grid = [[[str(i) for i in range(0,10)] for x in range(9)] for x in range(9)]
mylist = [[99,99] for x in range(81)]
dummy = [[99,99] for x in range(81)]
res = []

setup(grid)

index = 0
stopall = False

for i in range(9):
	for j in range(9):
		checkGrid(grid,i,j)
		if grid[i][j][0] == ".":
			mylist[index] = [i,j]
			dummy[index] = [i,j]
			index = index + 1

printgrid(grid)

loop = True
while loop:
	try:
		mylist.pop(mylist.index([99,99]))
		dummy.pop(dummy.index([99,99]))
	except:
		loop = False

clash = 0
p = 0
filename = raw_input()
#print mylist
simplify(dummy,grid,res)
print datetime.datetime.now().time()
solve(mylist,p)
print datetime.datetime.now().time()
