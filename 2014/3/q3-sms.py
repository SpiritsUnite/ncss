def tonum(c):
    if c == 's': return '7'
    if c == 'v': return '8'
    if c == 'y' or c == 'z': return '9'
    return str((ord(c) - ord('a')) // 3 + 2)

def tochr(n):
    if n == 8: return 't'
    if n == 9: return 'w'
    return chr(n * 3 - 6 + ord('a'))

freq = {}

for line in open("frequencies.txt"):
    w, f = line.split()
    n = ''.join(tonum(c.lower()) for c in w)
    f = int(f)
    freq[n] = freq.get(n, []) + [(w, f)]

for k in freq:
    freq[k].sort(key=lambda x: -x[1])

out = []

for w in input().split():
    n = str(int(w.replace("*", "")))
    i = w.count('*')
    if n not in freq:
        out.append(''.join(tochr(int(i)) for i in n))
    else:
        out.append(freq[n][i % len(freq[n])][0])

print(' '.join(out))
