import csv
from math import *
lat = input().split()
la = float(lat[0]) + float(lat[1])/60 + float(lat[2])/3600
if lat[3] == 'S': la = -la
la = radians(la)

lon = input().split()
lo = float(lon[0]) + float(lon[1])/60 + float(lon[2])/3600
if lon[3] == 'W': lo = -lo
lo = radians(lo)

hr = int(input())

# la, lo
best = -1
bname = ""
for line in csv.DictReader(open("public-toilets.csv")):
    if line["IsOpen"] == "Variable": continue
    if line["IsOpen"] == "DaylightHours" and (hr < 6 or hr >= 20): continue
    la2 = radians(float(line["Latitude"]))
    lo2 = radians(float(line["Longitude"]))
    dist = round(6371 * acos(sin(la)*sin(la2) + cos(la)*cos(la2)*cos(abs(lo - lo2))))
    if best == -1 or dist < best:
        best = dist
        bname = ", ".join([line["Name"], line["Town"], line["State"]])

print("Closest toilet:", bname)
print("Distance: %dkm" % best)
