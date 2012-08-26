import re
for i in re.findall(r"(\S*[IB]-(\S*)( \S*I-\2)*)",open("input.txt").read()):print i[0]