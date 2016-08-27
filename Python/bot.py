#!/usr/bin/python
def still_to_clean(board,dimh,dimw):
	result = False
	for y in xrange(dimh):
		for x in xrange(dimw):
			if board[x][y] == 'd':
				result = True
	return result
	
def next_move(posr, posc, dimh, dimw, board):
	move = checkNeighbors(posr,posc,board,dimh,dimw)
	print move
	return move	
	
	
def checkNeighbors(r,c,board,dimh,dimw):
	m = 'NONE'
	old_d2 = 9999
	(nr,nc) = (r,c)
	for i in xrange(0,dimh):
		for j in xrange(0,dimw):
			if board[i][j] == 'd':
				d2 = (i-r)**2 + (j-c)**2
				if d2 < old_d2:
					old_d2 = d2
					(nr,nc) = (i,j)
	
	if (nr,nc) == (r,c):
		m = "CLEAN"
		
	if nr > r and nc == c:
		m = "DOWN"
	if nr < r and nc == c:
		m = "UP"
		
	if nr < r and not nc == c:
		m = "UP"
	if nr > r and not nc == c:
		m = "DOWN"
		
	if nc > c and nr == r:
		m = "RIGHT"
	if nc < c and nr == r:
		m = "LEFT"

	if nc > c and not nr == r:
		m = "RIGHT"
	if nc < c and not nr == r:
		m = "LEFT"

	return m
		       
if __name__ == "__main__":
	import random
	dim = [50,50]
	board = [['-' for j in xrange(dim[0])] for k in xrange(dim[1])]
	pos = [random.randint(0,dim[0]-1),random.randint(0,dim[1]-1)]
	board[pos[0]][pos[1]] = 'b'
	for y in xrange(dim[1]):
		for x in xrange(dim[0]):
			toss = random.randint(0,3)
			if toss == 1:
				fill = 'd'
				board[x][y] = fill
	count = 0
	while still_to_clean(board,dim[0],dim[1]):
		count = count + 1
		#print count
		for x in xrange(dim[0]):
			for y in xrange(dim[1]):
				print board[x][y],
			print ''
#		raw_input()
		move = next_move(pos[0], pos[1], dim[0], dim[1], board)
		#print "position ", pos
		#print "move ",move
		if move == 'CLEAN':
			#print "cleaning"
			(pos[0],pos[1]) = (pos[0],pos[1])
			board[pos[0]][pos[1]] = 'b'
		if move == 'LEFT':
			board[pos[0]][pos[1]] = '-'
			(pos[0],pos[1]) = (pos[0],pos[1]-1)
			if board[pos[0]][pos[1]] == '-':
				board[pos[0]][pos[1]] = 'b'
		if move == 'RIGHT':
			board[pos[0]][pos[1]] = '-'
			(pos[0],pos[1]) = (pos[0],pos[1]+1)
			if board[pos[0]][pos[1]] == '-':
				board[pos[0]][pos[1]] = 'b'
		if move == 'UP':
			board[pos[0]][pos[1]] = '-'
			(pos[0],pos[1]) = (pos[0]-1,pos[1])
			if board[pos[0]][pos[1]] == '-':
				board[pos[0]][pos[1]] = 'b'
		if move == 'DOWN':
			board[pos[0]][pos[1]] = '-'
			(pos[0],pos[1]) = (pos[0]+1,pos[1])
			if board[pos[0]][pos[1]] == '-':
				board[pos[0]][pos[1]] = 'b'
	#	raw_input()
