
#! /usr/bin/env python3

import os
import requests
import json
import re

keys = ['title', 'name', 'date', 'feedback']
reviews = {}

data_dir = '/data/feedback/'
files = os.listdir(data_dir)

for file in files:
    with open(os.path.join(data_dir, file), 'r') as fh:
        for index,line in enumerate(fh):
            reviews[keys[index]] = line.strip('\n')
        response = requests.post("http://34.70.115.233/feedback/", json=reviews)
        result = response == 201
        if not response.ok:
            print(response.status_code)