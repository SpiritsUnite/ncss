import re

links = []
refs = {}
for line in open("post.md"):
    match = re.match(r"\[([a-zA-Z\d\s]+?)\]: (.*)", line)
    if match:
        refs[match.group(1).strip()] = match.group(2).strip()
    else:
        links += re.findall(r"\[.+?\](\(.+?\)|\[[a-zA-Z\d\s]+?\])", line)

secret = []
for l in links:
    if l[0] == '(':
        link = l[1:-1].strip()
    elif l[0] == '[':
        link = refs.get(l[1:-1].strip(), '').strip()
    if not link or len(link.split('#')) == 1: continue
    word = link.split('#')[-1].strip()
    if word:
        secret.append(word)

if secret:
    print(' '.join(secret))
