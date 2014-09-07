import re
board = []
s = open("jewels.txt").read().strip()
for x in range(8):
    board.append(list(s[x*8:x*8+8]))
at = 64

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

def ext(l):
    global at
    d = 8 - len(l)
    at += d
    return l + s[at-d:at]

def cascade():
    global board
    global score
    mul = 0
    fscore = score
    pscore = score
    while True:
        tod = rem()
        score += (score - pscore) * mul
        pscore = score
        mul += 1
        if len(tod) == 0: break
        for p in tod:
            board[p[0]][p[1]] = ''
        board = [list(i) for i in zip(*[ext(''.join(l)) for l in zip(*board)])]
    return fscore != score

pboard()
print("Score =", score)
mov = input()
while mov:
    mov = [int(x) for x in mov.split()]
    c1, r1, c2, r2 = mov
    if abs(c2-c1) + abs(r2-r1) != 1:
        print("Invalid move")
    elif max(mov) > 7 or min(mov) < 0:
        print("Invalid move")
    else:
        board[r1][c1], board[r2][c2] = board[r2][c2], board[r1][c1]
        if cascade():
            pboard()
            print("Score =", score)
        else:
            board[r1][c1], board[r2][c2] = board[r2][c2], board[r1][c1]
            print("Invalid move")
    mov = input()
