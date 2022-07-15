#!/bin/bash

#*********************************************************
# PREREQUESITES:
#
# Run the 'populate_files.sh' script in the data directory to populate the data for this exercise





#*********************************************************
#  Create a new empty file or overwrite the exsiting file
#
>oldFiles.txt

#*********************************************************
#  Store output contents of the piped command into $files variable
#
      # 1) enclosing the command in '$(<command>)' allows return results into variable
      # 2) use grep to find all occurrences of the pattern " jane " (surrounded by space) in the file list.txt
      # 3) use cut to separate each line by a (' ') delimeter.  -f3 specifies the field or cell to return
files=$( grep " jane " ../data/list.txt | cut -d' ' -f3)


#*********************************************************
#  Preserve the names of the files to be renamed by iterating 
#  through each file. Then test '[ -e <filename> ]' if file exists in the working directory.
#  If it does, append it to the text file created at the beginning of this script.
working_dir=$HOME/Projects/IT-Automation/

for f in $files; do
   echo "loop"
   echo $working_dir$f
   if [ -e $working_dir$f ];then
      echo "working"
      echo $working_dir$f >> oldFiles.txt; 
   fi
done
