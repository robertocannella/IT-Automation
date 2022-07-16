#!/usr/bin/env python3

import sys
args_len = len(sys.argv)

def binary_search(list, key):
    """Returns the position of key in the list if found, -1 otherwise.

    List must be sorted.
    """
    left = 0
    right = len(list) - 1
    while left <= right:
        middle = (left + right) // 2

        if list[middle] == key:
            return middle
        if list[middle] > key:
            right = middle - 1
        if list[middle] < key:
            left = middle + 1
    return -1


def main():
    if args_len > 1:
        args = []
        for index,thing in enumerate(sys.argv):
            if index == 0:
                continue
            args.append(thing)
        key = args.pop(-1)
        print("Key of {} is {}".format(key,binary_search(args,key)))
    else:
        print("enter a list of numbers,  followed by a key")
        sys.exit(1)

main()
