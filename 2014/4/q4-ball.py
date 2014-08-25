class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def m(self):
        return (self.y.y - self.x.y) / (self.y.x - self.x.x)

    def __str__(self):
        return str(self.x) + ", " + str(self.y)

lines = {}
for line in open("marble-run.txt"):
    line = line.split()
    if len(line) == 2:
        st = Point(*[float(i) for i in line])
    else:
        pts = [float(i) for i in line[1:]]
        a = min((pts[0], pts[1]), (pts[2], pts[3]))
        b = max((pts[0], pts[1]), (pts[2], pts[3]))
        lines[line[0]] = Point(Point(*a), Point(*b))

hit = [""]
def nxt(p):
    global hit
    best = 0
    pt = Point(0, 0)
    bname = "GROUND"
    for k,l in lines.items():
        if hit[-1] == k: continue
        if p.x < l.x.x or p.x > l.y.x: continue
        y = l.m() * (p.x - l.x.x) + l.x.y
        if y > p.y: continue
        if y > best:
            best = y
            if l.x.y > l.y.y:
                pt = l.y
            else:
                pt = l.x
            bname = k
    hit.append(bname)
    return pt

while hit[-1] != "GROUND":
    st = nxt(st)
print(" ".join(hit[1:]))
