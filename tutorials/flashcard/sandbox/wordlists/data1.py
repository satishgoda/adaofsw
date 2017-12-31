
# http://www.k12reader.com/dolch-word-list-sorted-alphabetically-by-grade-with-nouns/

f = open("data1.txt")

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
        
        # Since there are two colums for nouns
        # And we collapsed into one
        if index > 5:
            index = 5
        
        category = database.keys()[index]
        database[category].append(item)


