import string
lengths = {}
for word in open("words.txt"):
	word = word.strip()
	try:
		lengths[len(word)].append(word)
	except KeyError:
		lengths[len(word)] = [word]

crypt = raw_input("encrypted: ")
eWords = filter(None, sorted([word.strip(string.punctuation) for word in crypt.split()], key=lambda word: len(set(word)), reverse=True))
subs = {}
backs = {}

def crack(at):
	if at >= len(eWords):
		return True
	# Try all possible words
	for word in lengths[len(eWords[at])]:
		added = []
		badded = []
		# Check corresponding letters
		for i in xrange(len(eWords[at])):
			# Check punctuation directly
			if eWords[at][i] == "'" or word[i] == "'":
				if eWords[at][i] != word[i]:
					break
			elif eWords[at][i] in subs:
				if subs[eWords[at][i]] != word[i]:
					break
			elif word[i] in backs:
				break
			else:
				subs[eWords[at][i]] = word[i]
				backs[word[i]] = eWords[at][i]
				added.append(eWords[at][i])
				badded.append(word[i])
		else:
			# all matched
			if crack(at + 1):
				return True
		for a in added: del subs[a]
		for b in badded: del backs[b]
	return False

crack(0)
for e, d in subs.items():
	crypt = crypt.replace(e, d)

print "decrypted: " + crypt
