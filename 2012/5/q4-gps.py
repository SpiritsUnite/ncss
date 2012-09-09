import math

class Point(object):
	EARTH_RADIUS = 6353000
	def __init__(self, theta, radius):
		self.theta = theta
		self.radius = radius

		self.calc()

	def calc(self):
		self.x = math.sin(self.theta) * self.radius
		self.y = -math.cos(self.theta) * self.radius

	def distSq(self, p):
		"""Returns square of the distance"""
		return (self.x - p.x) ** 2 + (self.y - p.y) ** 2

class City(Point):
	def __init__(self, name, theta):
		super(City, self).__init__(theta, Point.EARTH_RADIUS)
		self.name = name
		self.blackout = 0

class Satellite(Point):
	def __init__(self, height, velocity, theta):
		super(Satellite, self).__init__(theta, Point.EARTH_RADIUS + height)
		self.velocity = velocity

	def move(self):
		self.theta += self.velocity / self.radius * 60
		self.theta %= math.pi * 2

		# Recalculate x, y value
		self.calc()

	def canSee(self, city):
		"""Can this satellite see city?"""
		a = city.radius
		b = self.distSq(city)      # Note that b is dist squared, others are not
		c = self.radius
		# Cosine Rule!
		g = (a ** 2 + b - c ** 2) / (2 * a * math.sqrt(b))
		# Screw precision, that's why! >:C >:C >:C
		if g > 1 - 1e-8:
			g = 1
		elif g < -1 + 1e-8:
			g = -1
		angle = math.acos(g)
		return angle > math.pi/2 - 1e-8

satellites = []
cities = []

line = raw_input("Enter: ")
while line:
	line = line.split()
	if line[0] == "city":
		cities.append(City(line[1], float(line[2])))
	elif line[0] == "satellite":
		satellites.append(Satellite(float(line[1]), float(line[2]), float(line[3])))
	line = raw_input("Enter: ")

# dump = open("dump.txt", "w")

for t in xrange(1440):
	for s in satellites: s.move()

	# Dumping
	# for s in satellites:
	# 	dump.write("satellite {} {}\n".format(s.x, s.y))
	# for c in cities:
	# 	dump.write("city {} {} {}\n".format(c.name, c.x, c.y))

	for c in cities:
		# good = False
		for s in satellites:
			if s.canSee(c):
				# good = True
				# dump.write("line yellow {} {} {} {}\n".format(c.x, c.y, s.x, s.y))
				break
		else:
			c.blackout += 1
		# if not good:
		# 	c.blackout += 1
	# dump.write("\n")

for c in cities:
	print "%s %s" % (c.name, c.blackout)
