import re
typo = {}
line = input()
while line:
    for word in re.split(r"[\s.,;-]+", line):
        if len(word) < 4: continue
        word = word.lower()
        wordc = re.sub("[aeiou]", "", word)
        typo[wordc] = typo.get(wordc, set()) | set([word])
    line = input()

for k in typo:
    if len(typo[k]) > 1:
        print(" ".join(sorted(typo[k])))
