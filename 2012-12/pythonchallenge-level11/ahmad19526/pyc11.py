from PIL import Image
from pprint import pprint

im = Image.open("w.jpg")

im.save("a.jpg")
im.show()

pprint(dir(im))

x =  list(im.getdata())

odd = [x[i] for i in range(len(x)) if i%2 != 0]
even = [x[i] for i in range(len(x)) if i%2 == 0]

op = im.putdata(odd)

#evp = Image.new("RGB",(320,240))
ev = evp.putdata(even)

im.save("odd.jpg")
#ev.save("even.jpg")


print "odd pixels %s" % len(odd)
print len(x)
