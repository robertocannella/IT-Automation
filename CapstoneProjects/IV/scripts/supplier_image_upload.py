#!/usr/bin/env python3
import os
import requests

url = "localhost/upload/"

HOME = os.path.expanduser("~")
input_dir = HOME+"/supplier-data/images/"
files = os.listdir(input_dir)


def upload_images(files):
    for file in files:
        with open (file, 'rb') as opened:
            r = requests.post(url, files ={'file': opened})
            if not r.ok:
                print('ERROR: ', r.status_code)

def main():
    upload_images(files)

if __name__ == '__main__':
    main()