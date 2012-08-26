import re
text = open("input.txt", "rU").read()
matches = re.findall(r"(\S*?\|[^\|]*\|[IB]-(\S*)( \S*?\|[^\|]*\|I-\2)*)", text)
if matches:
    print "\n".join(x[0].strip() for x in matches)