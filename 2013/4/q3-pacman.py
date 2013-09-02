dr, dc = [-1, 0, 1, 0], [0, -1, 0, 1]
maze = [list(line.strip()) for line in open("maze.txt")]
move = []
for r in range(len(maze)):
    for c in range(len(maze[0])):
        if maze[r][c] == 'G':
            found = False
            q = [(r, c, (0, 0))]
            seen = []
            while q:
                node = q[0]
                q = q[1:]
                seen.append(node)
                for xr, xc in zip(dr, dc):
                    nr, nc = node[0] + xr, node[1] + xc
                    try:
                        if maze[nr][nc] == '#': continue
                        if node[2] == (0, 0):
                            nex = (nr, nc, (xr, xc))
                        else:
                            nex = (nr, nc, node[2])
                        if maze[nr][nc] == 'P':
                            found = True
                            break
                        if nex in seen: continue
                        q.append(nex)
                    except:
                        continue
                if found:
                    break
            move.append(((r, c), (r + nex[2][0], c + nex[2][1])))

for i in move:
    maze[i[0][0]][i[0][1]] = ' '
for i in move:
    maze[i[1][0]][i[1][1]] = 'G'

print('\n'.join(''.join(n) for n in maze))

