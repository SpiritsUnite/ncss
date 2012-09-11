import re
rules = {}

def addRule(rule, value):
    try:
        rules[rule].append(value)
    except KeyError:
        rules[rule] = [value]

# Parsing functions

def variable(token):
    if len(token) > 0:
        return token[0].isupper()
    return False

def atom(token):
    if len(token) > 0:
        return token[0].islower()
    return False

def arg(token):
    return bool(re.match(r'\d+$', token))

def parseTermList(token):
    """Separates terms of a term list"""
    return map(str.strip, token.split(','))

def parsePredicate(token):
    """Retruns a predicate as a list with the name and term list"""
    token = token.strip()
    m = re.search(r"(\w*)\s*\((.*?)\)", token)
    if m:
        rule, value = m.group(1), parseTermList(m.group(2))
        return [rule, value]
    return False

def parsePredicateList(token):
    """Separates predicates of a predicate list"""
    token = token.strip()
    m = re.search(r"(\w*\(.*?\))(.*)", token)
    if m:
        return [m.group(1)] + parsePredicateList(m.group(2))
    return []

# Query functions

# Brute force solve

def bfsolve(at, predicates, subs):
    if at >= len(predicates):
        yield subs
        raise StopIteration
    rule, value = predicates[at][:]

    if rule not in rules:
        raise StopIteration

    # Check against each possible rule for predicate
    for match in rules[rule]:
        if not match:
            continue
        s = {}
        for k, v in subs.items():
            s[k] = v
        
        if parsePredicate(match[0]):
            # Then all are predicates
            nPreds = map(parsePredicate, match)
            try:
                for pred in nPreds:
                    for k, v in enumerate(pred[1]):
                        if arg(v):
                            pred[1][k] = value[int(v)]
                            if variable(pred[1][k]) and pred[1][k] in subs:
                                pred[1][k] = subs[pred[1][k]]
                            elif variable(pred[1][k]):
                                pred[1][k] = "ARGZ " + pred[1][k]
                        elif variable(v) and v in subs:
                            pred[1][k] = subs[v]
                        elif variable(pred[1][k]):
                            pred[1][k] = "ARGZ " + pred[1][k]
            except IndexError:
                continue

            for n in bfsolve(0, nPreds, {}):
                for k, v in n.items():
                    # pop an argz off
                    k = k.split(None, 1)
                    if len(k) > 1:
                        s[k[-1]] = v
                for k, v in s.items():
                    s[k] = v
                for i in bfsolve(at + 1, predicates, s):
                    yield i
        else:
            # It is just a fact

            # Make sure both same length
            if len(match) != len(value):
                continue

            # Check if each matches
            for i in xrange(len(value)):
                # Compare if atoms
                if atom(value[i]):
                    if value[i] != match[i]:
                        break
                # Compare substitute if variable
                # If no substitute, add.
                else:
                    if value[i] in s:
                        if match[i] != s[value[i]]:
                            break
                    else:
                        s[value[i]] = match[i]
            else:
                # It matches :O
                for i in bfsolve(at + 1, predicates, s):
                    yield i

# Main program

for line in open("program.plg"):
    # Ignore blank lines
    line = line.strip()
    if not line:
        continue

    # Query
    if line.startswith("?-"):
        line = line[2:].strip()
        predicate = parsePredicate(line)
        try:
            ans = bfsolve(0, [predicate], {}).next()
            printed = False
            for i in sorted(predicate[1]):
                if variable(i):
                    print "{0} = {1}".format(i, ans[i])
                    printed = True
            if not printed:
                print "yes"
        except StopIteration:
            print "no"
    # Rule
    elif len(line.split(":-", 1)) > 1:
        # Get both sides
        rule, predicates = map(str.strip, line.split(":-", 1))
        rule = parsePredicate(rule)
        for i, p in enumerate(rule[1]):
            predicates = predicates.replace(p, str(i))

        addRule(rule[0], parsePredicateList(predicates))
    # Fact
    else:
        rule, value = parsePredicate(line)
        addRule(rule, value)
bfsolve(0, [parsePredicate('female(X)'), parsePredicate('female(Y)')], [])