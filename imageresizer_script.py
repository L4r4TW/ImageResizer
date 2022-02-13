# from PIL import Image
# import glob
# import os

# import sys
# print(sys.executable)

# image_list = []
# resized_images = []
# image_name_list = []

# for filename in glob.glob('/Volumes/TOSHIBA EXT/RV_leltár_HSSC Kft/Képek/*.*'): #set import path
#     # print(filename)
#     img = Image.open(filename)
#     image_list.append(img)
#     image_name_list.append(os.path.split(filename)[1])

# for image in image_list:
# #     image.show()
#     image = image.resize((600,400)) #set desired size in pixels (width, length)
#     resized_images.append(image)

# for (i, new) in enumerate(resized_images):
#     new.save('{}{}'.format('//Users/bruno/Pictures/MVH_fotok_teszt/Atmeretezett/',image_name_list[i])) #set output path
#     print(i+1)

# image_list.clear()
# resized_images.clear()
# /Users/bruno/Pictures/MVH_fotok_teszt/Eredeti
# Volumes/TOSHIBA EXT/RV_leltár_HSSC Kft/Képek/*.*

from PIL import Image
import glob
import os
i=0

for (filename) in glob.glob('/Volumes/TOSHIBA EXT/RV_leltár_HSSC Kft/Képek/*.*'): #set import path
    i = i + 1
    print(filename + str(i))    
    img = Image.open(filename)
    image_name = os.path.split(filename)[1]
    image = img.resize((200,200)) #set desired size in pixels (width, length)
    image.save('{}{}'.format('//Users/bruno/Pictures/MVH_fotok_teszt/Atmeretezett/',image_name)) #set output path