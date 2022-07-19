#!/usr/bin/env python3

# APPROACH
# Original implementation used single process to backup a directory.  
# The directory is structured as follows

# prod -
#       | alpha -
#                |- video
#                |- audio
#       | beta -
#                |- video
#                |- audio
#       | delta -
#                |- video
#                |- audio ....etc

# Backing up each sub directory of the parent into a separate process allows for speedier results.

# TODO: refactor the code to minimize the imports.  Looks like some utils are available from multiple imports
import multiprocessing              # used for multiprocessing
from multiprocessing import Pool    #
import os                           # for making/creating directories and files
import subprocess                   # used to call our main backup function
from pathlib import Path            # for path existence
import shutil                       # for removing directory tree recursively

# Set the paths
HOME = os.path.expanduser('~')
src = HOME+'/Projects/IT-Automation/PerformanceTooling/data/prod/'
dest = HOME+'/Projects/IT-Automation/PerformanceTooling/data/prod_backup/'


# This method only used for populating dummy data.  Not part of the core functionality of the script
def make_fake_directories(src):
    """Populates data directory with dummy data"""
    # Delete existing data if it exists
    exists = os.path.isdir(src)
    if exists:
        shutil.rmtree(src)

    # Create root directories
    os.mkdir(src)
    for folder in ['alpha','beta','gamma','delta','epsilon','zeta']:
        os.mkdir(src+ folder)
   
    # Create dummy data here
    for root, dirs, files in os.walk(src,topdown=False):
        print('making {}'.format(root))
        for name in dirs:
            if len(dirs) > 0:
                path = os.path.join(root, name)
                os.mkdir(path + '/video', mode=0o777 )
                for i in range(30):
                    Path(path + '/video/movie{}.mp4'.format(i)).touch()
                os.mkdir(path + '/audio', mode=0o777 )
                for i in range(30):
                    Path(path + '/audio/music{}.mp3'.format(i)).touch()


# This backup task is the one we will run with multiprocessing
def run(path):
    print("Running: {} : {} ".format(multiprocessing.current_process(), path))
    subprocess.call(["rsync", "-arq", path, dest])
    

if __name__ == '__main__':
    # Comment/Uncomment this to reset directory structure
    make_fake_directories(src)
    

    # Store our paths here
    paths = []
    for root, dirs, files in os.walk(src):
        # ignore the top level directory
        if root == src:
            continue
        if len(dirs) > 0:
            paths.append(root)

    # create the appropriate pool size 
    p = Pool(len(paths))

    # map our list of paths to the run function, subsequently to the process pool.  
    p.map(run,paths)
