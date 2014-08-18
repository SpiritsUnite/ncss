import re

if re.search("a.*a.*r.*d.*v.*a.*r.*k", input("Enter text: "), re.I):
    print("Aardvark!")
else:
    print("No aardvarks here :(")
