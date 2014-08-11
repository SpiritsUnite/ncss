d = int(input())
div = [int(input()) for i in range(d)]
n = int(input())

for i in range(1, n+1):
    x = ''.join(' ' if i % div[j-1] else 'X' for j in range(1, d+1)).rstrip()
    print(str(i).rjust(len(str(n))) + ":" + x)
