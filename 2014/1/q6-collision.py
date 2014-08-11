count_collisions=lambda t,k:(lambda z:sum(i if i>1 else 0 for i in[z.count(n)for n in set(z)]))([''.join(str(k[c])for c in w.lower())for w in t.split()])
