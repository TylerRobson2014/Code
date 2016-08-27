import math
import copy

def perm(mystring,ref,level):
	global word,wordlist,myplist
	if level == len(mystring):
		word_to_check = "".join([word[i] for i in mystring])
		if word_to_check+"\n" in wordlist:
			myplist.append(word_to_check)

	else: 
		for l in [w for w in ref if not(w in mystring[:level])]:
			mystring[level] = l
			perm(mystring,ref,level+1)


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
	#print myclist

	for word in myclist:
		#print "word",word
		word = list(word)
		dummy = []
		for i in range(len(word)):
			dummy.append(i)
		ref = copy.deepcopy(dummy)
		level = 0
		myplist = []

		perm(dummy,ref,level)
		myset = set(myplist)
		myplist = list(myset)
		if len(myplist)==0:
			pass
			#print "No words of length : ",length
		else:
			for i in myplist:
				masterlist.append(i)

print "Found word(s) !!"
masterlist = set(masterlist)
masterlist = list(masterlist)
print masterlist
