def convert_grokcoin(n):
    st = [n]
    s = {0}
    c = {0:0}
    ans = 0
    while st:
        cur = st.pop()
        if cur in s: continue
        s.add(cur)
        st += [cur//i for i in (2,3,4) if cur//i not in s]
    print(len(s))
    for i in sorted(s):
        c[i] = max(i, c[i//2] + c[i//3] + c[i//4])
    return c[n]
