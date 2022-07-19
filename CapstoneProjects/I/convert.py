#!/usr/bin/env python3

import os
import sys
from PIL import Image

HOME = os.path.expanduser("~")
input_dir = HOME+"/images/"
output_dir  = "/opt/icons/"

def check_dirs():
    if not os.path.isdir(input_dir) or not os.path.isdir(output_dir):
        print("Not all paths returned a value. Check paths.")
        sys.exit(1)
    return True

    
    

def get_images_as_list():
    images = []
    try:
        list = os.listdir(input_dir)
    except FileNotFoundError as e:
        raise FileNotFoundError

    for item in list:
        if os.path.isfile(os.path.join(input_dir, item)):
            if not item.startswith('.'):
                images.append(item)
    return images

def rotate_scale(images):
    for image in images:
        im = Image.open(os.path.join(input_dir, image))
        im.rotate(90).convert('RGB').resize((128,128)).save(os.path.join(output_dir,"{}fixed.jpg".format(image)))
        print(image)

def main():
    check_dirs()
    images = get_images_as_list()
    rotate_scale(images)

if __name__ == "__main__":
	main()
