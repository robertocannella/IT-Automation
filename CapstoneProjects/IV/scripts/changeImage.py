#!/usr/bin/env python3

import os
import sys
from PIL import Image

HOME = os.path.expanduser("~")
input_dir = HOME+"/supplier-data/images/"
output_dir  = input_dir

def check_dirs():
    if not os.path.isdir(input_dir) or not os.path.isdir(output_dir):
        print("Not all paths returned a value. Check paths.")
        sys.exit(1)
    return True

def get_images_as_list(input_dir):
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

def resize_and_format(images):
    for image in images:
        im = Image.open(os.path.join(input_dir, image))
        im.convert('RGB').resize((600,400)).save(os.path.join(output_dir,"{}.jpeg".format(image.replace('.tiff',''))))
        print('converted: ', image)

def main():
    check_dirs()
    images = get_images_as_list()
    resize_and_format(images)

if __name__ == "__main__":
	main()