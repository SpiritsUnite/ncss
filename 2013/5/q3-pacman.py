import copy
from collections import deque

# make a class to define a grid square
# i could use a tuple, but grid.row is better than grid[0]
class Node():
    def __init__(self, row, col):
        self.row, self.col = row, col

    def __add__(self, rhs):
        return Node(self.row + rhs.row, self.col + rhs.col)

    def __sub__(self, rhs):
        return Node(self.row - rhs.row, self.col - rhs.col)

    def __eq__(self, rhs):
        return self.row == rhs.row and self.col == rhs.col

delta = [Node(1, 0), Node(0, 1), Node(-1, 0), Node(0, -1)]
pacmove = {'D': 0, 'R': 1, 'U': 2, 'L': 3}

# I store the maze, the ghosts and pacman separately which helps with dealing
# with the dots
maze = [list(line.strip()) for line in open('maze.txt')]
ghosts = []

for row in range(len(maze)):
    for col in range(len(maze[row])):
        if maze[row][col] == 'G':
            maze[row][col] = ' '
            ghosts.append(Node(row, col))
        elif maze[row][col] == 'P':
            maze[row][col] = ' '
            pacman = Node(row, col)

total = sum(line.count('.') for line in maze)

dead = False
points = 0

def output():
    # to output, i make a copy of the maze, put pacman and ghosts in
    # and output
    out = copy.deepcopy(maze)
    for ghost in ghosts:
        out[ghost.row][ghost.col] = 'G'
    if not dead:
        out[pacman.row][pacman.col] = 'P'
    print("Points:", points)
    print("\n".join("".join(line) for line in out))

commands = input('Commands: ').split()
for command in commands:
    if points == total: break
    if command == 'O':
        output()
        continue

    # to make a move, I bfs from the pacman to everywhere, while
    # storing the best move for a ghost at any square in move
    dist = [[0] * len(line) for line in maze]
    move = [[4] * len(line) for line in maze]
    queue = deque([pacman])
    while queue:
        node = queue.popleft()
        for i, v in enumerate(delta):
            new = node + v
            newdist = dist[node.row][node.col] + 1
            if maze[new.row][new.col] == '#': continue
            if new == pacman: continue
            if dist[new.row][new.col] == newdist:
                move[new.row][new.col] = min(move[new.row][new.col], i)
            if dist[new.row][new.col]: continue

            dist[new.row][new.col] = newdist
            move[new.row][new.col] = i
            queue.append(new)

    newpac = pacman + delta[pacmove[command]]
    if maze[newpac.row][newpac.col] == '#':
        newpac = pacman

    for ghost in ghosts:
        dead = dead or (newpac == ghost) or \
            (newpac == ghost - delta[move[ghost.row][ghost.col]])

    for i in range(len(ghosts)):
        ghosts[i] -= delta[move[ghosts[i].row][ghosts[i].col]]

    pacman = newpac
    if dead: break
    elif maze[pacman.row][pacman.col] == '.':
        points += 1
        maze[pacman.row][pacman.col] = ' '
if dead:
    print("You died!")
elif points == total:
    print("You won!")
output()
