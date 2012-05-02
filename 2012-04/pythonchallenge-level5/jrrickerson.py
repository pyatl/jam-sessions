import pickle

with open('banner.p') as file:
    obj = pickle.load(file)

for line in obj:
    output = ''
    for tup in line:
        output += tup[0] * tup[1]
    print output
