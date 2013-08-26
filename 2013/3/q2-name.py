import re
# parse all scores, put into a list of tuples
lead = [x.strip().split(',')[::-1] for x in open("leaderboard.txt")]
# make all scores integers not strings
lead = [[-int(x[0]), x[1]] for x in lead]
for i in range(len(lead)):
    lead[i][1] = re.sub(r'^[0-9]*', '', lead[i][1])
    lead[i][1] = re.sub(r'^[A-Z]*(?![a-z])', '', lead[i][1])
    lead[i][1] = re.sub(r'(^|\s+)\b[A-Z]+\b', '', lead[i][1])
    lead[i][1] = re.sub(r'(^|\s+)\b[^A-Z]\S*\b', '', lead[i][1])
    lead[i][1] = lead[i][1].strip()
    if not re.search(r'[A-Za-z]', lead[i][1]): lead[i][1] = "Invalid Name"
lead.sort()
for s, n in lead:
    print('%s,%d' % (n, -s))
