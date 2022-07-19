# IT-Automation

Google IT Automation Course

# Performance Tooling with Python

## Project 1 - Daily Backup

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

<hr>

## Project 2 - Employee Start Date Report
This lab builds on concepts covered to this point in the course.  Our primary focus is to improve the code run time.Throughout this project, we will touch on type casting, reading CSV into Python dictionaries, sorting dictionaries and iterating through tuples with lists.  

*Project Details*: You're a member of your company's IT department. A colleague that recently left the company wrote a program that's 90% complete; it's designed to read some data files with information on employees and then generate a report. It's up to you to finish the code -- this includes fixing any errors, bugs, and slowness that might be in the unfinished code.

*Prerequisites*: You should have a sound knowledge of the following things prior to performing the lab:

* Debugging (gathering information, root cause analysis, and remediation)
* Identifying and understanding system performance (I/O, Network, CPU, Memory)
* Understanding and troubleshooting the environment around the program (file system, OS, etc.)

**Task 1**:   Our first task is to fix a minor casting bug.  The script begins by requesting user input to specify a date to query from. The fix requires casting each of the inputs from a string to integer:

```
    year = int(input('Enter a value for the year: '))
    month = int(input('Enter a value for the month: '))
    day = int(input('Enter a value for the day: '))
```

**Task 2**: Our second task it to improve how the application retrieves it file through the `request` module.  The implementation given seems a bit far fetched for a real life scenario.  While iterating through each day from the user's input date to present, a separate http request is made for each day.  As I said, highly unlikely.  
Moving this call to get data to a separate function that gets called once resolves this issue.  

**Task 3**: This task is a bit more challenging as it requires the student to utilize knowledge acquired earlier in the course.  We are asked to clean up the program a bit more by providing a solution that eliminates some of the unessecary calculates by storing that data in a sorted list. Since the lab only gives high level guidelines of how to implement this, I'll go into detail here.

Let's outline how we will tackle this.

1. When we get the data from the http request, we will store it in directly into dictionary.
2. Upon complete of this, we will sort the dictionary by key. 
3. We can pass this sorted dictionary(which is now a list) to our function which will display the report.  
4. We can then iterate through the list to display content base on the user's requested query date. 

Here's a look at the dictionary sort function
```
    def get_data_as_sorted_list(data):
        reader = csv.reader(data[1:])
        employee_dict = {}
        for row in reader:
            if row[3] not in employee_dict:
                employee_dict[row[3]] = [{'First Name': row[0], 'Surname': row[1]}]
            else:
                employee_dict[row[3]].append({'First Name': row[0], 'Surname': row[1]})
        sorted_employee_dict = sorted(employee_dict.items(), key=operator.itemgetter(0))
        return sorted_employee_dict
```
Here's a look at the display function:
```
    def display_report(start_date,data):
    sorted_employees = get_same_or_newer_dict(data)
    for index, record in enumerate(sorted_employees):
        record_date = datetime.datetime.strptime(record[0],"%Y-%m-%d")
        if record_date > start_date:
            for employee in record[1]:
                print("Started on {}: {} {}".format(record_date.strftime("%b %d, %Y"), employee['First Name'], employee['Surname']))
        
```