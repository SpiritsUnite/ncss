class Particle:
    def __init__(self, a, b, c, d, e):
        self.x = a
        self.y = b
        self.vx = c
        self.vy = d
        self.q = e

    def disp(self):
        print("position = (%d, %d)" % (self.x, self.y))
        print("velocity = (%d, %d)" % (self.vx, self.vy))
        print("charge = %d" % self.q)

    def move(self):
        self.x += self.vx
        self.y += self.vy

    def distance(self, x, y):
        return ((self.x - x)**2 + (self.y - y)**2)**.5
