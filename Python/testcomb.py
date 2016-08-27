import re
import math

word = raw_input("Enter word: ")

index = 0
number = math.factorial(len(word))
wordlist = ["" for x in range(number+1)]

def foo(word,num):
	global index
	global wordlist
	if not(len(num) == len(word)):
		for i in range(len(word)):
			if i not in num:
				num.append(i)
				foo(word,num)
				num.pop()

	else:
		for j in range(len(num)):
			if not(re.search(r'[^\.a-z]',word[num[j]])):
				wordlist[index] = wordlist[index] + word[num[j]]

		index = index + 1
		
def check_string(myword):

    #open the file using `with` context manager, it'll automatically close the file for you
    with open('/usr/share/dict/words') as f:
        found = False
        for line in f:
            if re.match(myword,line.rstrip()):
				if len(myword) == len(line.rstrip()):
					print "found",myword
					found = True


count = []

foo(word,count)

wordlist.pop()

print wordlist

for k in range(number):
	check_string(wordlist[k])




