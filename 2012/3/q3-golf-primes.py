h=1000000
P=range(h)
P[1]=0
for i in range(h):
 if P[i]:
  for j in range(i+i,h,i):P[j]=0
p=filter(None,P)
d=[p[i+1]-p[i]for i in range(len(p)-1)]
i=d.index(max(d))
print p[i],p[i+1]