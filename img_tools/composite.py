import os, sys
from PIL import Image
from PIL import ImageChops
import StringIO




im = Image.open("thumb.jpg")
print im.format, im.size, im.mode


im2 = Image.open("blank.jpg")
print im2.format, im2.size, im2.mode


mask = Image.open("mask.png")
print mask.format, mask.size, mask.mode


#out = Image.alpha_composite(im, mask)    #Pillow
out = Image.composite(im, im2, mask)
print out.format, im.size, out.mode

out.save("out_with_mask.jpg", "JPEG")