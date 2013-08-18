a,b,c,d=map(float,map(input,['']*4))
e,f=b/a/a,d/c/c
s='cake %s'%((e>f)+1)
if e==f:s='either'
print('Cake 1 costs $%.2f per cm2 for %d cm2\nCake 2 costs $%.2f per cm2 for %d cm2\nGet %s!'%(e,a*a,f,c*c,s))
