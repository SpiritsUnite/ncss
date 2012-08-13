trans = {}
f = open("bilingual.txt")
for line in f:
	line = line.split()
	trans[line[0]] = line[1]
	trans[line[1]] = line[0]
def tran(word):
	if word in trans:
		return trans[word]
	return word
words = [tran(x) for x in raw_input("Enter English: ").split()]
print "German: {0}".format(" ".join(words))
words = [tran(x) for x in words]
print "English: {0}".format(" ".join(words))