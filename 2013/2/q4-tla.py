import re

num = 0
tla = 0
for line in open('sentences.txt'):
    num += 1
    if re.search(r'(^|[^A-Z])[A-Z]{3}([^A-Z]|$)', line): tla += 1

print("%.1f%% of sentences contain a TLA" % (tla * 100 / num))
