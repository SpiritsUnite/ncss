def carries(a, b):
    a,b = str(a),str(b)
    n = 0
    carry = 0
    for i in range(1, max(len(a),len(b)) + 1):
        res = 0
        try:
            res += int(a[-i])
        except:
            pass
        res += carry
        try:
            res += int(b[-i])
        except:
            pass
        if res > 9:
            n += 1
            carry = 1
        else:
            carry = 0
    return n
