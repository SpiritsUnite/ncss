import re
tags = {}
for m in re.finditer("<([a-zA-Z0-9]+)(\s[^>]*|/\s*)?>", open("input.html").read()):
    tags[m.group(1).lower()] = tags.get(m.group(1).lower(), 0) + 1

tags = sorted(tags.items(), key=lambda x: (-x[1], -len(x[0])))
if len(tags):
    longest = (len(tags[0][0]), tags[0][1])
    print('\n'.join("%s %d" % t for t in tags if (len(t[0]), t[1]) == longest))

