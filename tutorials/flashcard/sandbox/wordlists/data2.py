
# http://www.k12reader.com/dolch-word-list-sorted-by-frequency-by-grade/

f = open("data2.txt")

header = f.readline()

from collections import OrderedDict


database = OrderedDict()

for item in header.split():
    database[item] = []

for line in f.readlines():
    items = line.rstrip().split('\t')
    
    for index, item in enumerate(items):
        if not item:
            continue
        category = database.keys()[index]
        database[category].append(item)


