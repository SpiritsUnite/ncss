pref = {}
for line in open("preferences.txt"):
    line = line.strip().split(',')
    pref[line[0]] = int(line[1])

sands = [l.strip() for l in open("sandwiches.txt")]
sands.sort(key=lambda x: (-sum(pref.get(i, 0) for i in x.split(',')), -len(x.split(',')),x))
if sands: print('\n'.join(sands))
else: print("devo :(")
