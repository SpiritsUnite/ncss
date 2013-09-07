def interleavings(a, b):
    if a == '' and b == '': return ['']
    elif a == '': return [b]
    elif b == '': return [a]
    l = []
    for s in interleavings(a[1:], b):
        l.append(a[0] + s)
    for s in interleavings(a, b[1:]):
        l.append(b[0] + s)
    l.sort()
    return l
