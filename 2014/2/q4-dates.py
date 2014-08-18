import re

form = 0
DMY = 1
MDY = 2
YMD = 3

dates = []

def fmt(date):
    if form == DMY:
        date.reverse()
    elif form == MDY:
        date[0], date[1] = date[1], date[0]
        date.reverse()
    return "%04d-%02d-%02d" % tuple(date)

def check(date):
    if date[1] in (1, 3, 5, 7, 8, 10, 12) and 0 < date[2] <= 31:
        return True
    elif date[1] in (4, 6, 9, 11) and 0 < date[2] <= 30:
        return True
    elif date[1] == 2 and 0 < date[2] <= 28:
        return True
    return False

def unambiguate(date):
    global form
    if form: return
    if check(list(reversed(date))): form = DMY
    if check([date[2], date[0], date[1]]):
        if form:
            form = 0
            return
        form = MDY
    if check(date):
        if form:
            form = 0
            return
        form = YMD

for line in open("ambiguous-dates.txt"):
    dates += re.findall(r"([0-9]+)[^a-zA-Z0-9]([0-9]+)[^a-zA-Z0-9]([0-9]+)", line)

dates = [list(map(int, date)) for date in dates]
for d in dates:
    unambiguate(d)
    if form: break

if form:
    for d in dates: print(fmt(d))
else:
    print("No unambiguous dates found")
