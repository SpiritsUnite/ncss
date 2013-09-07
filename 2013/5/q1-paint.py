grid = open("patches.txt").read().split()
seen = [[0]*len(line) for line in grid]

dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

def dfs(r, c):
    stack = []
    stack.append((r, c))
    while stack:
        r, c = stack.pop()
        seen[r][c] = 1
        for i in range(8):
            nr = r + dr[i]
            nc = c + dc[i]
            try:
                if nr < 0 or nc < 0: continue
                if seen[nr][nc]: continue
                if grid[nr][nc] == '.': continue
                stack.append((nr, nc))
            except IndexError:
                continue

ans = 0
for r in range(len(grid)):
    for c in range(len(grid[r])):
        if seen[r][c] or grid[r][c] == '.': continue
        ans += 1
        dfs(r, c)

if ans == 1:
    print("1 patch")
else:
    print("%d patches" % ans)
