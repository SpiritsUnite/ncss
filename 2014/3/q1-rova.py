import re
def encode(s):
    title = s.istitle()
    s = re.sub(r"([bcdfghjklmnpqrstvwxyz])", r"\1o\1", s)
    s = re.sub(r"([BCDFGHJKLMNPQRSTVWXYZ])", r"\1O\1", s)
    if title: s = s.title()
    return s

def decode(s):
    title = s.istitle()
    if title: s = s.lower()
    s = re.sub(r"([bcdfghjklmnpqrstvwxyz])o\1", r"\1", s)
    s = re.sub(r"([BCDFGHJKLMNPQRSTVWXYZ])O\1", r"\1", s)
    if title: s = s.title()
    return s
