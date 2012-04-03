import urllib
import re

nothing = "44827"
def find_last_nothing(nothing):
    prefix = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
    exp = r"[0-9]+"
    for i in range(1, 400):
        url = prefix + nothing
        c = urllib.urlopen(url).read()
        match = re.search(exp, c)
        if match == None:
            print "finalized @ " + nothing
            return nothing
        nothing = match.group(0)
        print "following nothing " + nothing

s = find_last_nothing("44827")
print find_last_nothing(str(int(s) / 2))

print "content tells you to next use 63579"
print find_last_nothing("63579")
