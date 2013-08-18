import re
to_camel=lambda s:re.sub('_.',lambda x:x.group()[1].upper(),s)
