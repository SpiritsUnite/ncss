n = input('Number: ')
a = ''
if len(n) > 10:
    a = 'not '
for i in range(len(n)):
    if n.count(str(i)) != int(n[i]):
        a = 'not '
print(n, "is %sautobiographical" % a)
