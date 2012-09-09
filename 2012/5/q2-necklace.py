necklaces = []
lace = raw_input("Enter necklace: ")
while lace:
	necklaces.append(lace)
	lace = raw_input("Enter necklace: ")

groups = []

for lace in necklaces:
	added = False
	for g in groups:
		# check if g[0] = lace
		for i in xrange(len(lace)):
			if lace[i:] + lace[:i] == g[0]:
				g.append(lace)
				added = True
				break
			elif (lace[i:] + lace[:i])[::-1] == g[0]:
				g.append(lace)
				added = True
				break
		if added:
			break
	if not added:
		groups.append([lace])

for g in sorted(groups, key=lambda x: len(x), reverse=True):
	print " ".join(sorted(g))
