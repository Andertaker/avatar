import os, sys
from PIL import Image
from StringIO import StringIO

size = (200, 200)

#im = Image.open("test.jpg")
#print im.format, im.size, im.mode


f = open("test", "wb+")
s = f.read()
print len(s)


'''
io = StringIO(s)
print dir(io)
im = Image.open(io)
'''
im = Image.new("RGB", (200, 200), "white")
#Image.fromstring("RGBA", size, s)    #get image from pixel data, not file
print im.format, im.size, im.mode


b = im.tobytes()
print len(b)

s = im.tostring()


str_object = StringIO()
im.save(str_object, 'JPEG')

content = str_object.getvalue()


f.write(content)














