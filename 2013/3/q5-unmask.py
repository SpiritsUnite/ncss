import string

wdlen = {}
for line in open("texts.txt"):
    line = line.strip()
    l = []
    words = [w.strip(string.punctuation) for w in open(line).read().split()]
    for word in sorted(words, key=len, reverse=True):
        if not word: continue
        try:
            l[len(word) - 1] += 1
        except:
            l = [0] * len(word)
            l[len(word) - 1] += 1
    wdlen[line] = l

l = []
words = [w.strip(string.punctuation) for w in open("unknown.txt").read().split()]
for word in sorted(words, key=len, reverse=True):
    if not word: continue
    try:
        l[len(word) - 1] += 1
    except:
        l = [0] * len(word)
        l[len(word) - 1] += 1

final = []
for k, v in wdlen.items():
    try:
        final.append((sum(a * b for a, b in zip(v, l)) /
                (sum(i*i for i in v)**.5 * sum(i*i for i in l)**.5), k))
    except:
        final.append((0, k))
final.sort(key=lambda x: (-x[0], x[1]))
for s, k in final:
    print("%.3f %s" % (s, k))
