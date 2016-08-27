from __future__ import division
import math
from random import randint

N = 3
years = 5
Nfact = math.factorial(years)
NpowN = N**(years)
#p = (Nfact/(NpowN))
#p1 = (3**4-(3+18+24))/(3**4)
#p2 = (3**4 - (3*(2**4) - 3))/(3**4)
c = 0
for k in range(0,N+1):
	d = (math.factorial(N)/(math.factorial(k)*math.factorial(N-k)))*(N-k)*(math.factorial(years)/(math.factorial(k)*math.factorial(years - k)))
	c = c + d
p = 1 - (1/(N**years))*c


count = 0
total = 0

def selectSmurf():
	chosenSmurf = randint(1,N)
	return chosenSmurf


for i in range(1,10000):
	smurf = [0]*(N)
	total += 1
	for j in range(0,years):
		index = selectSmurf()-1
		smurf[index] = 1
	if all(item == 1 for item in smurf):
		count += 1

probability = count/total
print smurf
print "theory = ",p
print "practice = ",probability
	
