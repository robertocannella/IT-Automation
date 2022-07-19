#!/usr/bin/env python3

import sys
args_len  = len(sys.argv)

def linear_search(list, key):
    """If key is in the list returns its position in the list, otherwise returns -1."""
    for i, item in enumerate(list):
        if item == key:
            return i
    return -1

def main():
    if args_len > 1:
        list = []
        for thing in sys.argv:
            list.append(thing)
        key = list.pop()
        print("Key of {} is {}".format(key,linear_search(list, key)))
    else:
        print("enter a list of numbers,  followed by a key")
        sys.exit(1)

main()
