cache = {}
cache2 = {}

def convert_grokcoin(n):
    global cache
    if n not in cache:
        if n <= 1: cache[n] = n
        else: cache[n] = max(n, convert_grokcoin(n//2) + convert_grokcoin(n//3) + convert_grokcoin(n//4))
    return cache[n]

def gr_convert_grokcoin(n):
    global cache2
    if n not in cache2:
        if n <= 1: cache2[n] = n
        else:
            if n//2 + n//3 + n//4 > n:
                cache2[n] = convert_grokcoin(n//2) + convert_grokcoin(n//3) + convert_grokcoin(n//4)
            else:
                cache2[n] = n
    return cache2[n]
