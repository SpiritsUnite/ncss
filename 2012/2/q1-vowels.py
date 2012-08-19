_=''.join(_ for _ in open('words.txt')if __import__('re').match('(?i)^[tm][^aeiou]*[aeiou]?(?:[^aeiou]+[aeiou]?)*y$', _))
if _: print _,