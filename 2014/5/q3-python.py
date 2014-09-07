dr, dc = [1, 0, -1, 0], [0, 1, 0, -1]

grid = [list(l.strip()) for l in open("room.txt")]
h, w = len(grid), len(grid[0])
seen = [[0]*w for i in range(h)]
area = 1

stack = []

for r in range(h):
    for c in range(w):
        if grid[r][c] == '<':
            stack += [(r, c+1)]
        elif grid[r][c] == '>':
            stack += [(r, c-1)]
        elif grid[r][c] == '^':
            stack += [(r+1, c)]
        elif grid[r][c] == 'v':
            stack += [(r-1, c)]

while stack:
    area += 1
    r, c = stack.pop()
    seen[r][c] = 1
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if nr < 0 or nr >= h or nc < 0 or nc >= w: continue
        if grid[nr][nc] != 'X': continue
        if seen[nr][nc]: continue
        seen[nr][nc] = 1
        stack += [(nr, nc)]

print(area)
