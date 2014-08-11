n, s = int(input()), input()
for i in range(n):
    print(s)
    s = ''.join('*' if (s[(j-1) % len(s)] == '*') ^ (s[(j+1) % len(s)] == '*') else '.' for j in range(len(s)))
