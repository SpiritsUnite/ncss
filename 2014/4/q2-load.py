from particle import Particle

def load_particles(f):
    p, pos = [], []
    for no, line in enumerate(open(f)):
        if line.isspace(): continue
        nums = line.split()
        if len(nums) > 5:
            raise RuntimeError("Line %d contains too many items" % (no+1))
        if len(nums) < 5:
            raise RuntimeError("Line %d contains too few items" % (no+1))
        try:
            nums = [float(x) for x in nums]
        except ValueError:
            pass
            raise TypeError("Line %d has a non-number" % (no+1))
        if nums[-1] not in (-1, 0, 1):
            raise ValueError("Line %d has an invalid charge" % (no+1))
        if (nums[0], nums[1]) in pos:
            raise ValueError("Line %d uses the same position as a previous particle" % (no+1))
        p.append(Particle(*nums))
        pos.append((nums[0], nums[1]))
    return p
