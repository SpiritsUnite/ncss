def to_camel(s):
    s = s.split('_')
    return ''.join([s[0]] + list(map(lambda x: x[0].upper() + x[1:], s[1:])))
