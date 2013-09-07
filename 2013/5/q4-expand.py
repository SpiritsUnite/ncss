import re
s = []
line = input('RPN: ').split()
for c in line:
    if c in '+-*^':
        b = s.pop()
        a = s.pop()
        if c == '+':
            s.append([])
            for i in range(max(len(a), len(b))):
                s[-1].append(0)
                try:
                    s[-1][-1] += a[i]
                except IndexError:
                    pass
                try:
                    s[-1][-1] += b[i]
                except IndexError:
                    pass
        elif c == '-':
            s.append([])
            for i in range(max(len(a), len(b))):
                s[-1].append(0)
                try:
                    s[-1][-1] += a[i]
                except IndexError:
                    pass
                try:
                    s[-1][-1] -= b[i]
                except IndexError:
                    pass
        elif c == '*':
            s.append([0] * (len(a) + len(b)))
            for i in range(len(a)):
                for j in range(len(b)):
                    s[-1][i + j] += a[i] * b[j]
        else:
            e = a
            if b[0] > 1:
                for k in range(b[0] - 1):
                    res = [0] * (len(a) + len(e))
                    for i in range(len(a)):
                        for j in range(len(e)):
                            res[i + j] += a[i] * e[j]
                    a = res
                s.append(res)
            elif b[0] == 1:
                s.append(a)
            else:
                s.append([1])
    elif c == 'x':
        s.append([0, 1])
    else:
        s.append([int(c)])
while s[-1]:
    if s[-1][-1]:
        break
    s[-1].pop()
if s[-1]:
    ans = '-' if s[-1][-1] < 0 else ''
    ans += '%dx^%d' % (abs(s[-1][-1]), len(s[-1]) - 1)
    for i in range(len(s[-1]) - 2, -1, -1):
        if not s[-1][i]: continue
        ans += ' + ' if s[-1][i] > 0 else ' - '
        ans += '%dx^%d' % (abs(s[-1][i]), i)
    ans = re.sub(r'\^1\b', '', ans)
    ans = re.sub(r'x\^0\b', '', ans)
    ans = re.sub(r'\b1x', 'x', ans)
    ans = re.sub(r'-1x', 'x', ans)
    print(ans)
else:
    print('0')
