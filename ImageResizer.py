from PIL import Image
import glob
import os

i=0

for (filename) in glob.glob('/[set_path_here]/*.*'): #set import path
    i = i + 1
    print(filename + str(i))    
    img = Image.open(filename)
    image_name = os.path.split(filename)[1]
    image = img.resize((200,200)) #set desired size in pixels (width, length)
    image.save('{}{}'.format('/[set_path_here]/',image_name)) #set output path
