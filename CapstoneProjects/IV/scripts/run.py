#! /usr/bin/env python3

import os
import requests


url = "http://[CHANGE_THIS]/fruits"

HOME = os.path.expanduser("~")
input_dir = HOME+"/supplier-data/images/"
files = os.listdir(input_dir)

keys = ['name', 'weight', 'description', 'image_name']
items = {}

def post_descriptions():
    for file in files:
        with open(os.path.join(input_dir, file), 'r') as fh:
            for index,line in enumerate(fh):
                items[keys[index]] = line.strip('\n')
            items['weight'] = items['weight'].replace(' lbs', '')
            response = requests.post(url, json=items)
            if not response.ok:
                print("ERROR: ", response.status_code)

def main():
    post_descriptions()

if __name__ == "__main__":
    main()