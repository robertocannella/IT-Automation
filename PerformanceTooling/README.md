# IT-Automation

Google IT Automation Course

# Performance Tooling with Python

## Introduction

You're an IT administrator for a media production company that uses Network-Attached Storage (NAS) to store all data generated daily (e.g., videos, photos). One of your daily tasks is to back up the data in the production NAS (mounted at /data/prod on the server) to the backup NAS (mounted at /data/prod_backup on the server). A former member of the team developed a Python script (full path /scripts/dailysync.py) that backs up data daily. But recently, there's been a lot of data generated and the script isn't catching up to the speed. As a result, the backup process now takes more than 20 hours to finish, which isn't efficient at all for a daily backup.

What you'll do
* Identify what limits the system performance: I/O, Network, CPU, or Memory
* Use rsync command instead of cp to transfer data
* Get system standard output and manipulate the output
* Find differences between threading and multiprocessing

## Utilities 

* `rsync` [bash] (remote sync): a utility for efficiently transferring and synchronizing files between a computer and an external hard drive and across networked computers by comparing the modification time and size of files. [more1...](https://linux.die.net/man/1/rsync) [2...](linuxtechi.com/rsync-command-examples-linux/)
    ```
        rsync -zvh [Source-Files-Dir] [Destination] # copy/sync files locally
        rsync -zavh [Source-Files-Dir] [Destination] # copy/sync directories locally
        rsync -zrvh [Source-Files-Dir] [Destination] # copy files and directories recursively
    ```
    <table>
        <th>Options</th><th>Uses</th>
        <tr><td>-v</td><td>Verbose output</td></tr>
        <tr><td>-q</td><td>Suppress message output</td></tr>
        <tr><td>-a</td><td>Archive files and directory while synchronizing</td></tr>
        <tr><td>-r</td><td>Sync files and directories recursively</td></tr>
        <tr><td>-b</td><td>Take the backup during synchronization</td></tr>
        <tr><td>-z</td><td>Compress file data during the transfer</td></tr>
    <table>

    Calling from python script

    ```
    import subprocess

    src = "<source-path>"
    dest = "<destination-path>"

    subprocess.call(["rsync", "-arq", src, dest]) # copy/sync locally

    ```

* `os.walk()`: Python method walk() generates the file names in a directory tree by walking the tree either top-down or bottom-up.

    A script to generate dummy data using `os.walk()` is included in the python script for this project.  The script also uses `os.walk()` to
    traverse the directories for the `rsync` utility.

<hr>


## Multiprocessing

Now, when you go through the hierarchy of the subfolders of /data/prod, data is from different projects (e.g., , beta, gamma, kappa) and they're independent of each other. So, in order to efficiently back up parallelly, use multiprocessing to take advantage of the idle CPU cores. Initially, because of CPU bound, the backup process takes more than 20 hours to finish, which isn't efficient for a daily backup. Now, by using multiprocessing, you can back up your data from the source to the destination parallelly by utilizing the multiple cores of the CPU.

