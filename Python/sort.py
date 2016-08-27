import sys
import time

def simplify(mylist,res):
	minimum = 10000
	for i in range(len(mylist)):
		xi = mylist[i]
		if xi < minimum:
			minimum = xi
			topop = i
	try:
		res.append(mylist[topop])
		mylist.pop(topop)
	except:
		e = sys.exc_info()[0]
	
	if len(mylist) > 0:
		simplify(mylist,res)

	
	
mylist = [2,4,1,5,6.8,4,9,7,5,6.7,3,8,9,1,0.9,6,55,3,9]
res = []
simplify(mylist,res)
print res

