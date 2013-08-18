n,a=input(),''
if len(n)>10:a='not '
for k,v in enumerate(n):if n.count(str(k+1))-int(v):a='not '
print(n,"is %sautobiographical"%a)
