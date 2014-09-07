import csv

class Particle:
    def __init__(self, x, y, vx, vy, q, ax, ay):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.q = q
        self.ax = ax
        self.ay = ay

    def disp(self):
        print("position = ({}, {})".format(self.x, self.y))
        print("velocity = ({}, {})".format(self.vx, self.vy))
        print("acc = ({}, {})".format(self.ax, self.ay))

    def move(self):
        self.vx += self.ax
        self.vy += self.ay
        self.x += self.vx
        self.y += self.vy
        if self.x <= -300 or self.x >= 300:
            self.x = min(max(self.x, -300), 300)
            self.vx = -self.vx
        if self.y <= -200 or self.y >= 200:
            self.y = min(max(self.y, -200), 200)
            self.vy = -self.vy

    def distance(self, x, y):
        xoff = self.x - x
        yoff = self.y - y
        return (xoff*xoff + yoff*yoff) ** 0.5
    
    def __str__(self):
        return "%.1f,%.1f" % (self.x, self.y)

f = open("particles.txt")
n = int(f.readline())
ps = []
for l in f:
    if l: ps += [Particle(*[float(i) for i in l.split()])]

for i in range(n):
    for p in ps:
        x, y = 0, 0
        for q in ps:
            if q.x < p.x:
                x -= (-1)**((p.q > 0) == (q.q > 0))
            if q.x > p.x:
                x += (-1)**((p.q > 0) == (q.q > 0))
            if q.y < p.y:
                y -= (-1)**((p.q > 0) == (q.q > 0))
            if q.y > p.y:
                y += (-1)**((p.q > 0) == (q.q > 0))
        p.ax = x/10
        p.ay = y/10
    for p in ps:
        p.move()
    print(",".join(str(p) for p in ps))
