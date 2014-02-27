import os, sys
from datetime import datetime

from PIL import Image
from PIL.ExifTags import TAGS


'''
im = Image.open("test.jpg")
for k in im.info:
	v = im.info[k]
	print k + ": ", v.__class__

	if isinstance(v, basestring):
		print len(v)

	if k != "exif":
		print v

exif = im.info["exif"]
'''



#print exif


def get_exif(fn):
    ret = {}
    i = Image.open(fn)
    info = i._getexif()
    for tag, value in info.items():
        decoded = TAGS.get(tag, tag)
        ret[decoded] = value
    return ret


exif = get_exif("test.jpg")
"""
for k, v in exif.items():
	print k, ": "#, v.__class__

	if isinstance(v, basestring):
		#print len(v)
		pass
		

	if isinstance(v, basestring) and len(v) > 500:
		print "Too long value: " + str(len(v))
	else:
		print v
"""

print exif["DateTime"]
print exif["DateTimeOriginal"]
print exif["DateTimeDigitized"]






im = Image.open("test.jpg")
info = im._getexif()
date_time = info[306]

for tag, value in info.items():
    decoded = TAGS.get(tag, tag)
    print tag, " => ", decoded


"""
36867  =>  DateTimeOriginal
36868  =>  DateTimeDigitized
306  =>  DateTime
"""


"2011:03:29 04:06:40"

format = "%Y:%m:%d %H:%M:%S"

print date_time
#arr = date_time.replace(" ", ":").split(":")
#print arr
#dt = datetime.datetime(arr)
dt = datetime.strptime(date_time, format)

print dt
































