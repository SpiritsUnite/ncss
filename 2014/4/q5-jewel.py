import re
board = []
s = open("jewels.txt").read().strip()
for x in range(8):
    board.append(list(s[x*8:x*8+8]))

score = 0
reg = re.compile(r"([^?])\1{2,}")

def pboard():
    for i in range(7, -1, -1):
        print(' '.join(board[i]))

def rem():
    tod = []
    global score
    for k, line in enumerate(board):
        for m in reg.finditer(''.join(line)):
            score += 10 + 10*(len(m.group(0))-3)
            for i in range(m.start(), m.end()):
                tod.append((k, i))

    for k in range(8):
        for m in reg.finditer(''.join(line[k] for line in board)):
            score += 10 + 10*(len(m.group(0))-3)
            for i in range(m.start(), m.end()):
                tod.append((i, k))
    return tod

pboard()
print("Score =", score)
while True:
    tod = rem()
    if len(tod) == 0: break
    for p in tod:
        board[p[0]][p[1]] = '?'

    board = [list(i) for i in zip(*[''.join(l).replace('?','').ljust(8,'?') for l in zip(*board)])]
pboard()
print("Score =", score)
