import math
import copy


def comb(mystring,length,dummy,start,offset):
	global myclist
	end = len(mystring) - length + offset
	for i in xrange(start,end):
		if offset == 1:
			dummy = []
		dummy.append(mystring[i])
		if len(dummy) == length:
			hold = "".join(dummy)
			myclist.append(hold)
			dummy.pop()
		if offset < length:		
			comb(mystring,length,dummy,i+1,offset+1)

wl = open('/usr/share/dict/words', 'r')
wordlist = wl.readlines()
wl.close()

myclist = []

Myword = raw_input("Enter a word : ")
start = 0
offset = 1
masterlist = []
for length in xrange(3,len(Myword)+1):
	Mydummy = []
	comb(Myword,length,Mydummy,start,offset)
	myclist = set(myclist)
	myclist = list(myclist)
	print "length : ",length,myclist
	myclist = []

