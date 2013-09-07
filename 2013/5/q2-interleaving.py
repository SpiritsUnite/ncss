# interleavings(a, b) = union of interleavings(a[1:], b) and interleavings(a, b[1:])
# basically, to get the interleavings for a pair of strings
# we try find all interleavings that start with the first letter of a
# and union it with all the interleavings that start with the first letter of b
def interleavings(a, b):
    # base cases:
    if a == '' and b == '': return ['']
    elif a == '': return [b]
    elif b == '': return [a]

    # recursion
    l = []
    for s in interleavings(a[1:], b):
        l.append(a[0] + s)
    for s in interleavings(a, b[1:]):
        l.append(b[0] + s)
    l.sort()
    return l
