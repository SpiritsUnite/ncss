import re
s = open('site.html').read()
print('\n'.join(i[1] for i in re.findall(r'<img\s+([^>]+\s|\s*)src="([^"]*)"[^>]*>', s)))
