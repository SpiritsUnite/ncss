def caesar_shift(s, n):
    res = ''
    for c in s:
        if c.isupper():
            res += chr((ord(c) - ord('A') + n) % 26 + ord('A'))
        elif c.islower():
            res += chr((ord(c) - ord('a') + n) % 26 + ord('a'))
        else:
            res += c
    return res
