n = int(raw_input("Enter size: "))
grid = [['-' for i in xrange(n)] for i in xrange(n)]
# generate column by column
for c in xrange(n):
	# in first half?
	if c < n / 2:
		for r in xrange(n):
			if r == c + 1:
				grid[r][c] = '/'
			if r == n - c - 1:
				grid[r][c] = '\\'
			if r > c + 1 and r < n - c - 1:
				grid[r][c] = '|'
	else:
		for r in xrange(n):
			if r == c:
				grid[r][c] = '/'
			if r == n - c - 1:
				grid[r][c] = '\\'
			if r > n - c - 1 and r < c:
				grid[r][c] = '|'
for r in xrange(n):
	print ' '.join(grid[r])