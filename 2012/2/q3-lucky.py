n = int(raw_input("Enter number: "))
n += 1
l = [i for i in xrange(1, n)]
for i in xrange(2, n):
	if i in l:
		l = [l[j] for j in xrange(len(l)) if (j + 1) % i != 0]
print l[-1]