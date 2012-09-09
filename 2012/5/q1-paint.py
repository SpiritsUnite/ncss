c, r = map(int, raw_input("Coordinates: ").split())
grid = []
line = raw_input("Enter: ")
while line:
	grid.append(list(line))
	line = raw_input("Enter: ")

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def dfs(rc):
	row = rc[0]
	col = rc[1]
	# Bounds
	if row < 0 or row >= len(grid):
		return
	if col < 0 or col >= len(grid[row]):
		return
	for i in xrange(4):
		nr = row + dr[i]
		nc = col + dc[i]
		if nr < 0 or nr >= len(grid):
			continue
		if nc < 0 or nc >= len(grid[nr]):
			continue
		if grid[nr][nc] == " ":
			grid[nr][nc] = "."
			dfs((nr, nc))

if grid[r][c] == " ":
	grid[r][c] = "."
	dfs((r, c))

for i in grid:
	print "".join(i)
