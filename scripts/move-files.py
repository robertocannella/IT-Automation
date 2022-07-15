#!/usr/bin/env python3
import sys
import subprocess


#*********************************************************
# PREREQUESITES:
#
# The 'find_files.sh' script in this directory is the argument passed to
# this python script


#*********************************************************
# Open the file passed as an argument store into f variable
#
f = open(sys.argv[1], "r")


#*********************************************************
# Iterate throught the files, renamimg them.
#
for line in f.readlines():
 old_name = line.strip()                        # strip leading or trailing white spaces
 new_name = old_name.replace("jane", "jdoe")    # store new_name with replaced portion of string
 subprocess.run(["mv", old_name, new_name])     # call system to run 'mv' to rename file
f.close()                                       # close the file
