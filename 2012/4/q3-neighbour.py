import csv
import sys
reader = csv.DictReader(open("data.csv"))
data = [line for line in reader]
unkReader = csv.DictReader(open("unknown.csv"))
writer = csv.DictWriter(sys.stdout, reader.fieldnames)
for unknown in unkReader:
	unknown[reader.fieldnames[0]] = None
	bestDiff = len(reader.fieldnames) + 2
	for d in data:
		inc = 0
		for k, v in unknown.items():
			if d[k] != v:
				inc += 1
		if inc < bestDiff:
			bestDiff = inc
			unknown[reader.fieldnames[0]] = d[reader.fieldnames[0]]
	if unknown[reader.fieldnames[0]] != None:
		writer.writerow(unknown)
	