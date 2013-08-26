import re, string
words = []
for line in open("words.txt"):
    sets = 0
    for c in string.ascii_lowercase:
        if re.search(c*2, line):
            sets += 1
    if sets > 2:
        words.append(line.strip())
words.sort()
print('\n'.join(words))
