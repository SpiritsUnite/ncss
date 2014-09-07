convert_grokcoin=a=lambda n,c={0:0}:c.setdefault(n,n in c or max(n,a(n//2)+a(n//3)+a(n//4)))
