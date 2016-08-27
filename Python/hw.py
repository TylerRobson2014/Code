from __future__ import division
import random
import numpy as np
import math
import csv
import matplotlib.pyplot as plt

num_lines = sum(1 for line in open('/home/steve/Downloads/results1.csv'))

with open('/home/steve/Downloads/results1.csv', 'rb') as f:
    reader = csv.reader(f)
    data = list(reader)
print num_lines
x = []
y = []
diff = []
start = 4
window = 1
for i in xrange(start+window,num_lines-start):
	if not data[i][1] == "Bank holiday":
		x.append(float(data[i][1]))
		diff.append(float(data[i][1]) - float(data[i-window][1]))
	y.append(i)
#plt.plot(x)
#plt.show()
plt.plot(diff)
plt.show()




		

