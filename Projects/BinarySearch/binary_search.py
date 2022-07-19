#!/usr/bin/env python3

import sys
args_len = len(sys.argv)

def binary_search(list, key):
    """Returns the position of key in the list if found, -1 otherwise.

    List must be sorted.
    """
    print(list,int(key))
    left = 0
    right = len(list) - 1

    while left <= right:
        middle = (left + right) // 2
        print('middle: ',middle)
        print('right:', right)
        print('left', left)
        if int(list[middle]) == key:
            return middle
        if int(list[middle]) > key:
            right = middle - 1
        if int(list[middle]) < key:
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
        print("Key of {} is {}".format(key,binary_search(args,int(key))))
    else:
        print("enter a list of numbers,  followed by a key")
        sys.exit(1)

main()
