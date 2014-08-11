is_kaprekar=lambda x:(lambda y:any(int(y[:i])+int(y[i:])==x and int(y[:i])and int(y[i:])for i in range(1,len(y))))(str(x**2))
