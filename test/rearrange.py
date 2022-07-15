#!/usr/bin/env python3

import re


def rearrange_name(name):
    if type(name) is not str:
        raise ValueError('Input must be a string')


    result = re.search('^([\w .]*), ([\w .]*)$', name)
    print(result)
    if result is None:
            return name
    return "{} {}".format(result[2],result[1])


name = "Lovelace, Ada"

print(rearrange_name(name))