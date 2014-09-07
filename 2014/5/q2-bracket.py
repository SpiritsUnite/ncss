inp = input()
mtn = [[]]
stack = []
good = True
for i, c in enumerate(inp):
    while len(mtn) <= len(stack): mtn += [[]]
    if c in '({':
        mtn[len(stack)] += [(c,i)]
        stack += [c]
    if c == ')':
        if len(stack) > 0 and stack[-1] != '(':
            good = False
            break
        stack.pop()
        mtn[len(stack)] += [(c,i)]
    if c == '}':
        if len(stack) > 0 and stack[-1] != '{':
            good = False
            break
        stack.pop()
        mtn[len(stack)] += [(c,i)]

if good:
    for l in reversed(mtn):
        if not l: continue
        last = 0
        for c, i in l:
            print(' '*(i-last) + c, end='')
            last = i+1
        print()
else:
    print("Invalid input!")
