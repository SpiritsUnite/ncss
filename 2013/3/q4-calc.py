n = input("Number: ")
w = int(input("Width: "))

# Top bars
print(' '.join(' ' + '-' * w + ' ' if x not in '14' else ' ' * (w + 2) for x in n))

# Side top
for i in range(w):
    print(' '.join('|' + ' ' * w + '|' if x in '4890'
        else ' ' * (w + 1) + '|' if x in '1237'
        else '|' + ' ' * (w + 1) for x in n))

# Mid bars
print(' '.join(' ' + '-' * w + ' ' if x not in '170' else ' ' * (w + 2) for x in n))

# Side bottom
for i in range(w):
    print(' '.join('|' + ' ' * w + '|' if x in '680'
        else ' ' * (w + 1) + '|' if x in '134579'
        else '|' + ' ' * (w + 1) for x in n))

# Bottom
print(' '.join(' ' + '-' * w + ' ' if x not in '147' else ' ' * (w + 2) for x in n))

