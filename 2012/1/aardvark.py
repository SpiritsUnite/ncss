f = open("input.txt", "rU")
for i, line in enumerate(f, 1):
    line = line.lower()
    good = True
    for c in "ardvk":
        if line.count(c) < "aardvark".count(c):
            good = False
            break
    if good:
        print "Aardvark on line", i
