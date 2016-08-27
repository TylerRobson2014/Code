

word = raw_input("Enter word: ")

for i in range(0,len(word)):
	for j in range(0,len(word)):
		if not(j == i):
			for k in range(0,len(word)):
				if not(k == i) and not(k == j):
					for l in range(0,len(word)):
						if not(l == i) and not(l == j) and not(l == k):
							print word[i],word[j],word[k],word[l]


