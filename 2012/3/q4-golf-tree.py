def p(t):
 l,h=t;
 if not h:return['['+l+']']
 u=['']
 for c in h:
  s=p(c)
  while len(u)<len(s):u+=['.'*len(u[0])]
  while len(s)<len(u):s+=['.'*len(s[0])]
  for i in xrange(len(u)):u[i]+=s[i]
 u=map(lambda x:x+"."*max(0,len(l)-len(u[0])+2),u)
 return['['+l+"_"*max(0,len(u[0])-len(l)-2)+']']+u
print"\n".join(p(input()))