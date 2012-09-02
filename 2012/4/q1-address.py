import csv, sys
fields = ["firstname", "lastname", "email", "street", "town", "state"]
book = [line for line in csv.DictReader(open("addresses.csv"), fields)]

query = raw_input("Query: ").split(",")
for pair in query:
    field, value = pair.split("=", 1)
    book = filter(lambda x: x[field] == value, book)

csv.DictWriter(sys.stdout, fields).writerows(book)
