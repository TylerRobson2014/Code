from __future__ import division
import math
import random
from copy import deepcopy

def change(h):
	print "before",h
	h.append("c")
	print "after",h
	return h


a = ["a","b"]
b = change(a)
print "a = ",a
print "b = ",b
