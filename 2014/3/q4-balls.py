holes = [[int(i) for i in line.split()] for line in open("holes.txt")]
bucket = []

for line in open("balls.txt"):
    d, l = line.split()
    d = int(d)
    for i in range(len(holes)):
        if holes[i][1] and holes[i][0] >= d:
            holes[i][1] -= 1
            break
    else:
        bucket.append(l)

if bucket:
    print("The bucket contains:", ", ".join(bucket) + ".")
else:
    print("The bucket contains no balls.")
