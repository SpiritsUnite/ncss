def check(tree):
    children = tree[1]
    if len(children) not in (0, 3):
        return False
    for child in children:
        if not check(child):
            return False
    return True

tree = input('Enter tree: ')
if check(tree):
    print "Strict"
else:
    print "Non-strict"