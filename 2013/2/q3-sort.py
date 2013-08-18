def novowelsort(l):
    return sorted(l, key=lambda s: ''.join(c for c in s.lower() if c not in 'aoeui'))
