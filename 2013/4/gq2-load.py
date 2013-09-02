from node import *
class Graph:
 __init__=lambda s,l,f:s.load(f)if exec('s.l,s.i,s.n,s.e=l,[],{},{}')or f else f
 size=lambda s:len(s.n)
 def load(s,z):
  f=open(z)
  for l in f:
   if not l.strip():break
   i,l=map(str.strip,l.split(':'))
   if i in s.n:raise ValueError
   s.n[i],s.e[i]=Node(i,l),[]
   s.i.append(i)
  for l in f:
   r,l,o=map(str.strip,l.split(':'))
   if r not in s.n or o not in s.n:raise ValueError
   s.e[r].append((o,l))
   if not l:l=0
   s.n[r].add_neighbour(s.n[o],l)
 output=lambda s:[print(s.n[i],'[%s]'%', '.join(':'.join(x)for x in sorted(s.e[i])))for i in sorted(s.n.keys())]
 def degrees_of_separation(s,x,y):
  if x not in s.n or y not in s.n:raise ValueError
  a=[[1 if s.n[i].has_neighbour(s.n[j],None)else 1<<9 for j in s.i]for i in s.i]
  for k in range(s.size()):
   for i in range(s.size()):
    for j in range(s.size()):a[i][j]=min(a[i][j],a[i][k]+a[k][j])
  b=a[s.i.index(x)][s.i.index(y)]
  if b==1<<9:b=-1
  return 0 if x==y else b
 get_node=lambda s,i:s.n[i]if i in s.n else exec('raise ValueError')
