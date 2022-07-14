#!/usr/bin/env python3

import re

def rearrange_name(name):
    result = re.search('^([\w .]*), ([\w .]*)$', name)
    if result is None:
            return ''
    return "{} {}".format(result[2],result[1])


name = "Lovelace, Ada"

print(rearrange_name(name))