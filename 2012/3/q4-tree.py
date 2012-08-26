def proc(tree):
    # Base case
    if not tree[1]:
        return ['[' + tree[0] + ']']

    under = ['']
    for child in tree[1]:
        subtree = proc(child)
        # Extend under / subtree so they are equal
        while len(under) < len(subtree): under += ['.' * len(under[0])]
        while len(subtree) < len(under): subtree += ['.' * len(subtree[0])]
        for i in xrange(len(under)): under[i] += subtree[i]

    under = map(lambda x: x + "." * max(0, len(tree[0]) - len(under[0]) + 2), under)
    return ['[' + tree[0] + "_" * max(0, len(under[0]) - len(tree[0]) - 2) + ']'] + under

print "\n".join(proc(input("Enter tree: ")))