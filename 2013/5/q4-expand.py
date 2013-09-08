# Basic gist of this algorithm is to represent everything as a list
# where list[i] represents the coefficient of the term with degree i
#   e.g. [3, 0, 4, 2] => 2x^3 + 4x^2 + 0x + 3

# Adding is done just by adding respective values in list
# Subtracting is done similarly
# Multiplying is going through each pair of elements in both lists
#   multiplying them together, and adding it to the appropriate place
#   in the resultant list
# Exponentiation is multiplying by itself that many times
#   you could also use pascal's triangle

import re

def add(a, b):
    # create a 'zero polynomial' with enough space to add the two
    result = [0] * max(len(a), len(b))
    # add both onto the polynomial
    for i in range(len(a)):
        result[i] += a[i]
    for i in range(len(b)):
        result[i] += b[i]
    return result

def subtract(a, b):
    result = [0] * max(len(a), len(b))
    for i in range(len(a)):
        result[i] += a[i]
    for i in range(len(b)):
        result[i] -= b[i]
    return result

def multiply(a, b):
    result = [0] * (len(a) + len(b))
    # for every possible pair, multiply and add onto result
    for i in range(len(a)):
        for j in range(len(b)):
            result[i + j] += a[i] * b[j]
    return result

def exponentiate(a, b):
    result = [1]
    for i in range(b[0]):
        result = multiply(result, a)
    return result

stack = []
tokens = input('RPN: ').split()

for token in tokens:
    if token in '+-*^':
        b = stack.pop()
        a = stack.pop()

        if token == '+':
            stack.append(add(a, b))
        elif token == '-':
            stack.append(subtract(a, b))
        elif token == '*':
            stack.append(multiply(a, b))
        elif token == '^':
            stack.append(exponentiate(a, b))
    elif token == 'x':
        stack.append([0, 1])
    else:
        stack.append([int(token)])

# remove leading 0s in the answer
result = stack.pop()
while result:
    if result[-1]:
        break
    result.pop()

if result:
    ans = ''
    for k, v in reversed([i for i in enumerate(result)]):
        if v:
            ans += ' + %dx^%d' % (v, k)

    # first term shouldn't have a '+ ' at the front
    ans = ans[3:]

    # answer isn't formatted properly, so we use regex to fix it
    # turn '+ -' -> '- '
    ans = re.sub(r'\+ -', '- ', ans)
    # if the first term is -1x, turn it to -x
    ans = re.sub(r'^-1x', '-x', ans)
    # turn x^1 -> x
    ans = re.sub(r'\^1\b', '', ans)
    # remove x^0
    ans = re.sub(r'x\^0\b', '', ans)
    # turn 1x -> x
    ans = re.sub(r'\b1x', 'x', ans)
    print(ans)
else:
    print('0')
