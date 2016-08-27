import sys

def setup(grid):
	
	#problem = "1"*9*9
	problem1 = ".................85.7.1..2...........3...6.....9..523..6...3.1...18...54.4.69...7"
	problem2 = "....3.7.2.41..................1.5.3..6.4.....7........2...7....5......4....6..8.."
	problem3 = "....3.7.2.41..................4.5.3..6.1.....7........2...7....5......4....6..8.."
	problem4 = "....3.7.2.91..................9.4.6.2...........1.....7..62.....4.....9.8.....5.."
	problem5 = "....3.7.54...9....8........6..1...8.......2......7.....2.4......5....3.....8.6..."
	problem6 = "....3.7.6.1..42............6.31.....7......8.......2.....6....3.2.....4.5........"
	problem7 = "....3.7.8.4.....5..1.......2...7.......6...1.3........8.......3...1.4......5..2.."
	problem8 = "....3.7.8.4.....5..1.......2...7.......6...1.3........8.......3...1.4......5..9.."
	problem9 = "....3.7.8.4.....5..1.......2...9.......6...1.3........7.......3...1.4......5..2.."
	problem10 = "....3.7.8.4.....5..1.......2...9.......6...1.3........7.......3...1.4......5..9.."
	problem11 = "....3.7.8.4.....5..1.......2...9.......6...1.3........8.......3...1.4......5..2.."
	problem12 = "....3.8...1.5...........2..8...5.....6.....4.........1..94.1...2.....73......6..."
	problem13 = "....3.8...5.6...........2.....5...4.2.....3....1.......4.1...6......7.5.8...2...."
	problem14 = "....3.8.175...................4.2.6.6..5..2..1..........8.1.....2.....5....7....."
	problem15 = "....3.8.2.41..................4.5.6..6.7.....8........2...8....5......4....1..7.."
	problem16 = "....3.8.2.61..................1.4.5..5.7.....8........2...8....4......1....6..7.."
	problem17 = "....3.8.4...1....6.936.8...534...2.............8...915...4.762.4....9...9.6.2...."
	problem18 = "....3.8.4...625......4..5...96..13.........6.1.8......3..7629....93.....7.....4.8"
	problem19 = "....3.85.7.4.6.............2..1....4.8..5..........6...3.....9....4.2......7....."
	problem20 = "....3.86..41..7............2......3..5.1........5.....3.....7..6...2.......4....1"
	problem21 = "....3.9..8.1.7....7....1.236431...................536842.7....9....2.5.1..8.4...."
	problem22 = "....3.9.2.41..................4.5.1..7.6.....9........2...9....6......4....8..3.."
	problem23 = "....3.9.2.41..................7.4.1..6.5.....9........2...9....5......4....8..3.."
	problem24 = "....3.9.5.6..1.7.....2.9..3.14...8....68.73....51..69.1..6.5.....7.4..1.5.2.9...."
	problem25 = "....31....1....7......6..2....7..4.1..62.....3............8..6..7.9.....5........"
	problem26 = "....31....2....9...........3.1....5....27.4..8........69.4........7....2.......3."
	problem27 = "....31....5.....2..........6.....1.7.4.2........5..8.....42..6.1.3......8........"
	problem28 = "....31...2......5.........75..2......3......6......1...61...4.....5..32....8....."
	problem29 = "....31...2......6.4.........7....8.36..2...............38.7.1..5..6...2.........."
	
	offset = -1
	for i in range(9):
		offset += 1
		for j in range(9):
			grid[i][j][0] = problem4[offset*9+j]
			if grid[i][j][0] != ".":
				for m in range(1,10):
					try:
						grid[i][j].pop(len(grid[i][j])-1)
						print grid[i][j]
					except:
						e = sys.exc_info()[0]
		
def checkRow(grid,i,j):
	if grid[i][j][0] == ".":
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
									
def checkSquare(grid,i,j):
	if grid[i][j][0] == ".":
		if i in range(3):
			if j in range(3):
				for k in range(3):
					for l in range(3):
						if grid[k][l][0] != ".":
							try:
								grid[i][j].pop(grid[i][j].index(grid[k][l][0]))
							except:
								e = sys.exc_info()[0]
							
							
			if j in range(3,6):
				for k in range(3):
					for l in range(3,6):
						if grid[k][l][0] != ".":
							try:
								grid[i][j].pop(grid[i][j].index(grid[k][l][0]))
							except:
								e = sys.exc_info()[0]
									
			if j in range(6,9):
				for k in range(3):
					for l in range(6,9):
						if grid[k][l][0] != ".":
							try:
								grid[i][j].pop(grid[i][j].index(grid[k][l][0]))
							except:
								e = sys.exc_info()[0]	
		if i in range(3,6):
			if j in range(3):
				for k in range(3,6):
					for l in range(3):
						if grid[k][l][0] != ".":
							try:
								grid[i][j].pop(grid[i][j].index(grid[k][l][0]))
							except:
								e = sys.exc_info()[0]
									
			if j in range(3,6):
				for k in range(3,6):
					for l in range(3,6):
						if grid[k][l][0] != ".":
							try:
								grid[i][j].pop(grid[i][j].index(grid[k][l][0]))	
							except:
								e = sys.exc_info()[0]
									
			if j in range(6,9):
				for k in range(3,6):
					for l in range(6,9):
						if grid[k][l][0] != ".":
							try:
								grid[i][j].pop(grid[i][j].index(grid[k][l][0]))									
							except:
								e = sys.exc_info()[0]
								
		if i in range(6,9):
			if j in range(3):
				for k in range(6,9):
					for l in range(3):
						if grid[k][l][0] != ".":
							try:
								grid[i][j].pop(grid[i][j].index(grid[k][l][0]))	
							except:
								e = sys.exc_info()[0]
									
			if j in range(3,6):
				for k in range(6,9):
					for l in range(3,6):
						if grid[k][l][0] != ".":
							try:
								grid[i][j].pop(grid[i][j].index(grid[k][l][0]))		
							except:
								e = sys.exc_info()[0]
									
			if j in range(6,9):
				for k in range(6,9):
					for l in range(6,9):
						if grid[k][l][0] != ".":
							try:					
								grid[i][j].pop(grid[i][j].index(grid[k][l][0]))
							except:
								e = sys.exc_info()[0]
						
grid = [[[str(i) for i in range(0,10)] for x in range(9)] for x in range(9)]

setup(grid)

loop = True

count = 1
loopcount = 1

while loop:
	loop = False
	count = count + 1
	loopcount = loopcount + 1

	if (count == 199):

		print "*****************BEGIN*********************",loopcount
		print grid
		print "******************END**********************",loopcount
		print "                          "
		print "                          "
	if count > 200:
		count = 0

	for i in range(9):
		for j in range(9):
			checkColumn(grid,i,j)
			length = len(grid[i][j])
			if length == 2:
				grid[i][j][0] = grid[i][j][1]
				grid[i][j].pop(1)
			checkRow(grid,i,j)
			length = len(grid[i][j])
			if length == 2:
				grid[i][j][0] = grid[i][j][1]
				grid[i][j].pop(1)
			checkSquare(grid,i,j)
			length = len(grid[i][j])
			if length == 2:
				grid[i][j][0] = grid[i][j][1]
				grid[i][j].pop(1)
			length = len(grid[i][j])
			if length > 1:
				loop = True
			
print grid
