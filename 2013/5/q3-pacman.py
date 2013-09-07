# uhh, later

import copy
dr, dc = [-1, 0, 1, 0], [0, -1, 0, 1]
pr, pc = {'U': -1, 'R': 0, 'D': 1, 'L': 0}, {'U': 0, 'R': 1, 'D': 0, 'L': -1}
maze = [list(line.strip()) for line in open('maze.txt')]
tot = sum(line.count('.') for line in maze)
gs = []
for r in range(len(maze)):
    for c in range(len(maze[r])):
        if maze[r][c] == 'G':
            maze[r][c] = ' '
            gs.append((r, c))
        elif maze[r][c] == 'P':
            maze[r][c] = ' '
            p = (r, c)

die = False
pts = 0
def output():
    out = copy.deepcopy(maze)
    for g in gs:
        out[g[0]][g[1]] = 'G'
    if not die:
        out[p[0]][p[1]] = 'P'
    print("Points:", pts)
    print("\n".join("".join(line) for line in out))

com = input('Commands: ').split()
for co in com:
    if pts == tot: break
    if co == 'O':
        output()
        continue
    moves = []
    for g in gs:
        unseen = copy.deepcopy(maze)
        q = [(g[0], g[1], (0, 0))]
        while q:
            r, c, m = q[0]
            if (r, c) == p:
                break
            q = q[1:]
            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                if not unseen[nr][nc] or maze[nr][nc] == '#': continue
                unseen[nr][nc] = 0
                if m == (0, 0):
                    q.append((nr, nc, (dr[i], dc[i])))
                else:
                    q.append((nr, nc, m))
        moves.append((g[0] + q[0][2][0], g[1] + q[0][2][1]))

    np = (p[0] + pr[co], p[1] + pc[co])
    if maze[np[0]][np[1]] == '#':
        np = p # SOLVED P == NP!

    die = False
    for i in gs:
        if np == i: die = True
    for i in moves:
        if np == i: die = True

    gs = moves
    p = np # SOLVED P == NP AGAIN!
    if die: break
    elif maze[p[0]][p[1]] == '.':
        pts += 1
        maze[p[0]][p[1]] = ' '
        if pts == tot: break
if die:
    print("You died!")
elif pts == tot:
    print("You won!")
output()
