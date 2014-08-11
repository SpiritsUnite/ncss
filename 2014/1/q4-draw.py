l, p, r = [], {}, {}
for line in open("draw.txt"):
    a, b = line.split(',')
    p[a], r[a] = {}, int(b)
    l.append(a)

for i in range(1, len(bin(len(l))) - 2):
    for j in range(len(r) >> i):
        p[l[j*2]][l[j*2 + 1]] = p[l[j*2 + 1]][l[j*2]] = i
        l[j] = min(l[j*2], l[j*2 + 1], key=lambda s: r[s])

try:
    print("Round %d" % p[input()][input()])
except:
    print("Did not play")
