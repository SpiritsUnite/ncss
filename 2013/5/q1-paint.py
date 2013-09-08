grid = open("patches.txt").read().split()

# this list ensures i only expand on each grid square at most once
# this is basically the only thing i needed in terms of speed
seen = [[False]*len(line) for line in grid]

# useful when doing graph search algorithms on a grid
# i can just loop over this
deltar = [-1, -1, 0, 1, 1, 1, 0, -1]
deltac = [0, 1, 1, 1, 0, -1, -1, -1]

# This had originally been recursive, but that blows stack memory
# so I had to slightly alter it to be iterative...
def dfs(r, c):
    # Stack maintains a list of nodes i want to expand on
    stack = []
    stack.append((r, c))
    while stack:
        curr, curc = stack.pop()
        seen[curr][curc] = True
        # using the delta lists, i can easily go in the 8 directions
        for i in range(8):
            nextr = curr + deltar[i]
            nextc = curc + deltac[i]
            # using exceptions to keep myself in bounds
            try:
                # negative indices are valid, but we don't want to wrap
                if nextr < 0 or nextc < 0: continue
                # make sure we only expand each square once
                if seen[nextr][nextc]: continue
                if grid[nextr][nextc] == '.': continue
                stack.append((nextr, nextc))
            except IndexError:
                continue

# count the patches by making sure we go through each patch once
# using the seen array and dfsing
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
