from PIL import Image
from __init__ import *

im = Image.open("test.jpg")




avatar = ImgTools().make_avatar(im)


avatar.save("avatar_test.jpg")
