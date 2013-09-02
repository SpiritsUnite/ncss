import csv, sys

degrees = list(csv.DictReader(open("degrees.csv")))
students = list(csv.DictReader(open("students.csv")))
qs = list(csv.DictReader(open("students.csv")))
qs.sort(key=lambda x: (-float(x['score']), x['name']))
qs.reverse()

accept = {}
for d in degrees: accept[d['code']] = []

while qs:
    s = qs.pop()
    ps = s['preferences'].split(';')
    score = float(s['score'])
    for p in ps:
        good = False
        sc = score
        if len(p.split('+')) > 1:
            sc = min(99.95, sc + float(p.split('+')[1]))
            p = p.split('+')[0]
        if len(accept[p]) < int([d for d in degrees if d['code'] == p][0]['places']):
            good = True
            accept[p].append((s['name'], sc))
        else:
            try:
                if sc > accept[p][-1][1]:
                    qs.append([st for st in students if st['name'] == accept[p][-1][0]][0])
                    accept[p][-1] = (s['name'], sc)
                    good = True
            except IndexError:
                pass
        if good:
            accept[p].sort(key=lambda x: -float(x[1]))
            break

degout = csv.DictWriter(sys.stdout, ['code', 'name', 'institution', 'cutoff', 'vacancies'],
        lineterminator='\n')
degout.writeheader()
degrees.sort(key=lambda x: int(x['code']))
for d in degrees:
    try:
        d['cutoff'] = '%.2f' % accept[d['code']][-1][1]
    except IndexError:
        d['cutoff'] = '-'
    d['vacancies'] = 'Y' if len(accept[d['code']]) < int(d['places']) else 'N'
    d.pop('places')
    degout.writerow(d)

print()

stuout = csv.DictWriter(sys.stdout, ['name', 'score', 'offer'], lineterminator = '\n')
stuout.writeheader()
students.sort(key=lambda x: (-float(x['score']), x['name']))
for s in students:
    try:
        s['offer'] = [c for c in accept if s['name'] in [x[0] for x in accept[c]]][0]
    except IndexError:
        s['offer'] = '-'
    s['score'] = '%.2f' % float(s['score'])
    s.pop('preferences')
    stuout.writerow(s)
