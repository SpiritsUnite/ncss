k=raw_input("Enter key: ")
r=[i for i in raw_input("Enter text: ") if i.isalpha()]
r.extend(chr(i%26+97)for i in range((len(k)-len(r)%len(k))%len(k)))
print''.join(''.join(r[i[0]::len(k)])for i in sorted(enumerate(k),key=lambda x:x[1]))