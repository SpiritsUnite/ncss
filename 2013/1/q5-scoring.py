f = open('commentary.txt')
a, b = f.readline().split()[::2]
s = list(f)
c, d = len([x for x in s if x[:len(a)] == a]), len([x for x in s if x[:len(b)] == b])
if c > d:
    print(a, c)
    print(b, d)
else:
    print(b, d)
    print(a, c)

