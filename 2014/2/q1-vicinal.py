VICINAL = 0
NONVICINAL = 1
NEITHER = 2

prv = lambda c: chr((ord(c)-ord('a')-1)%26 + ord('a'))
nxt = lambda c: chr((ord(c)-ord('a')+1)%26 + ord('a'))

def vicinal(w):
    w = w.lower()
    l = [nxt(c) in w or prv(c) in w for c in w]
    if all(l): return VICINAL
    elif any(l): return NEITHER
    else: return NONVICINAL

inp = input("Line: ")
while inp:
    vic = [w for w in inp.split() if vicinal(w) == VICINAL]
    nonvic = [w for w in inp.split() if vicinal(w) == NONVICINAL]
    if vic:
        print("Vicinals:", *vic)
    if nonvic:
        print("Non-vicinals:", *nonvic)
    inp = input("Line: ")
