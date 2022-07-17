#!/usr/bin/env python3

import sys
args_len = len(sys.argv)

def find_item(list, item):
  #Returns True if the item is in the list, False if not.
  print(list)
  if len(list) == 0:
    return False

  #Is the item in the center of the list?
  middle = len(list)//2
  if list[middle] == item:
    return True

  #Is the item in the first half of the list?
  if int(item) < int(list[middle]):
    #Call the function with the first half of the list
    return find_item(list[:middle], item)
  else:
    #Call the function with the second half of the list
    return find_item(list[middle+1:], item)

  return False

def main():
    if args_len > 1:
        args = []
        for index,thing in enumerate(sys.argv):
            if index == 0:
                continue
            args.append(thing)
        key = args.pop(-1)
        print("Key of {} is {}".format(key,find_item(args,key)))
    else:
        print("enter a list of numbers,  followed by a key")
        sys.exit(1)

main()
