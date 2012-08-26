import re
def atom(token):
	return bool(re.match(r"^[a-z]\w*$", token))

def variable(token):
	return bool(re.match(r"^[A-Z]\w*$", token))

def term(token):
	return atom(token) or variable(token)

def term_list(tokens):
	a = tokens.split(",", 1)
	return term(tokens) or (len(a) == 2 and term(a[0]) and term_list(a[1]))

def predicate(tokens):
	a = tokens.split("(", 1)
	return atom(a[0]) and len(a) == 2 and len(a[1]) > 1 and a[1][-1] == ")" and term_list(a[1][:-1])

def predicate_list(tokens):
	good = predicate(tokens)
	m = re.match(r"(.*?\(.*?\)),(.*)", tokens)
	if m:
		return predicate(m.group(1)) and predicate_list(m.group(2))
	return good

def rule(tokens):
	a = tokens.split(":-", 1)
	if len(a) == 1:
		return len(a[0]) > 1 and a[0][-1] == "." and predicate(a[0][:-1])
	else:
		return len(a[0]) > 1 and predicate(a[0]) and len(a[1]) > 1 and a[1][-1] == "." and predicate_list(a[1][:-1])

def query(tokens):
	return tokens[:2] == "?-" and tokens[-1] == "." and predicate(tokens[2:-1])

def valid(line):
	return rule(line) or query(line)

f = open("program.plg", "rU")
for i, line in enumerate(f, 1):
	line = ''.join(c for c in line if not c.isspace())
	if line and not valid(line):
		print "Invalid program on line {0}!".format(i)
		break
else:
	print "Valid program!"