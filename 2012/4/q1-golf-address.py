import csv,sys;f=["firstname","lastname","email","street","town","state"];b=list(csv.DictReader(open("addresses.csv"),f));q=raw_input().split(",")
for p in q:k,v=p.split("=",1);b=filter(lambda x:x[k]==v,b)
csv.DictWriter(sys.stdout,f).writerows(b)