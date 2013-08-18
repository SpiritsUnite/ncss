f=open('commentary.txt')
a,b=f.readline().split()[::2]
s=list(f)
c=len([x for x in s if x[:len(a)]==a])
d=len(s)-c
if c<d:a,b,c,d=b,a,d,c
print("%s %d\n%s %d"%(a,c,b,d))
