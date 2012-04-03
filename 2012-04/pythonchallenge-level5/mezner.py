import pickle

f = open('5.p')
p = pickle.load(f)

for arr in p:
    line = ""
    for t in arr:
        line += t[0] * t[1]
    print line

