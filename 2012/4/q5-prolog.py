rules = {}
for line in open("program.plg"):
    line = line.strip()
    if not line:
        continue

    # QUERY!
    if line.startswith("?-"):
        line = line[2:].strip()
        rule = line[:line.index('(')]
        value = map(str.strip, line[line.index('(') + 1:line.index(')')].split(","))
        if rule in rules:
            for match in rules[rule]:
                variables = {}
                if len(match) != len(value):
                    continue
                for i in xrange(len(value)):
                    # If atom
                    if value[i][0].islower():
                        if value[i] != match[i]:
                            break
                    # If variable
                    else:
                        if value[i] in variables:
                            if match[i] != variables[value[i]]:
                                break
                        else:
                            variables[value[i]] = match[i]
                else:
                    if len(variables) == 0:
                        print "yes"
                    else:
                        for var, val in sorted(variables.items()):
                            print "{0} = {1}".format(var, val)
                    break
            else:
                print "no"
        else:
            print "no"
    else:
        rule, value = line.split('(', 1)
        value = map(str.strip, value[:value.index(')')].split(','))
        try:
            rules[rule].append(value)
        except KeyError:
            rules[rule] = [value]