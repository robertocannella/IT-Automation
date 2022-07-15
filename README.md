# IT-Automation

Google IT Automation Course

# Log Analysis Project

## Introduction
Imagine your company uses a server that runs a service called ticky, an internal ticketing system. The service logs events to syslog, both when it runs successfully and when it encounters errors.

The service's developers need your help getting some information from those logs so that they can better understand how their software is used and how to improve it. So, for this lab, you'll write some automation scripts that will process the system log and generate reports based on the information extracted from the log files.


This is the format of the reports we are aiming for:

**ERROR MESSAGE**

<table>
    <th>Error</th>
    <th>Count</th>
        <tr><td>Timeout while retrieving information</td><td>15</td></tr>
        <tr><td>The ticket was modified while updating</td><td>13</td></tr>
        <tr><td>Connection to DB failed</td><td>12</td></tr>
        <tr><td>Tried to add information to a closed ticket</td><td>10</td></tr>
        <tr><td>Permission denied while closing ticket</td><td>9</td></tr>
        <tr><td>Ticket doesn't exist</td><td>7</td></tr>
<table>

**USER STATISTICS**
<table>
    <th>Username</th>
    <th>INFO</th>
    <th>ERROR</th>
<tr><td>ac</td><td>2</td><td>2</td></tr>
<tr><td>ahmed.miller</td><td>2</td><td>4</td></tr>
<tr><td>blossom</td><td>2</td><td>6</td></tr>
<tr><td>bpacheco</td><td>0</td><td>2</td></tr>
<tr><td>breee</td><td>1</td><td>5</td></tr>
<tr><td>britanni</td><td>1</td><td>1</td></tr>
<tr><td>enim.non</td><td>2</td><td>3</td></tr>
<tr><td>flavia</td><td>0</td><td>5</td></tr>
</table>

What you'll do
* Use regex to parse a log file
* Append and modify values in a dictionary
* Write to a file in CSV format
* Move files to the appropriate directory for use with the CSV->HTML converter

<hr>

##  Exercise-1
### Use regex to parse a log file

We'll be working with a log file named syslog.log, which contains logs related to ticky.

The log lines follow a pattern similar to the ones we've seen before. Something like this:
```
May 27 11:45:40 ubuntu.local ticky: INFO: Created ticket [#1234] (username)

Jun 1 11:06:48 ubuntu.local ticky: ERROR: Connection to DB failed (username)
```

When the service runs correctly, it logs an INFO message to syslog. It then states what it did and states the username and ticket number related to the event. If the service encounters a problem, it logs an ERROR message to syslog. This error message indicates what was wrong and states the username that triggered the action that caused the problem.

In this section, we'll search and view different types of error messages. The error messages for ticky details the problems with the file with a timestamp for when each problem occurred.

These are a few kinds of listed error:

* Timeout while retrieving information
* The ticket was modified while updating
* Connection to DB failed
* Tried to add information to a closed ticket
* Permission denied while closing ticket
* Ticket doesn't exist

## Search using bash shell
To search all the ERROR logs, use the following command:
```
grep "ERROR" syslog.log
```

To enlist all the ERROR messages of specific kind use the below syntax.
```
grep "ERROR Tried to add information to closed ticket" syslog.log
```

## Search using python shell

Let's now write a few regular expressions using a python3 interpreter.

We can also grep the ERROR/INFO messages in a pythonic way using a regular expression. Let's now write a few regular expressions using a python3 interpreter.

```
python3
```

Import the regular expression module (re).  And create a line variable to simulate an instance of looping through log file lines

```
import re
line = "May 27 11:45:40 ubuntu.local ticky: INFO: Created ticket [#1234] (username)"
```
To match a string stored in line variable, we use the search() method by defining a pattern.  The regex below is seaching for a string that matches ```ticky: INFO: ``` followed by a group indicated by the parenthesis ```()```.  The group is seaching for ```any length of 'alpha/digit/hyphen' ```followed by a ```space```.  Note the addition white spice after the group declaration, before the closing double quote.  
 We then pass the line to check to the ```re.search()``` method
```
re.search(r"ticky: INFO: ([\w ]*) ", line)
```
output:
```
<_sre.SRE_Match object; span=(29, 57), match='ticky: INFO: Created ticket '>
```

Start fetching logs of ticky for a specific username. We'll need them in later sections. Here's what we plan on doing in the script.  We'll focus on just having the ability to parse the file for specified users and errors:


1) Set the user to search for.
2) Create an empty list to store the errors.
3) Open the syslog file and store contents in a file object.
4) Iterate through each log for matching.
    * a) match using regex to any logtype ```(ERROR|INFO)```
    * b) match using regex to any description ```([\w ]*)```
    * b) match using regex to any user ```\(([\w ].*)\)``` 
5) Conditionally add the error to our list.


Here's what we think the code will look like initially.  
```
#!/usr/bin/env python3

import os
import re

home_dir = os.path.expanduser('~')
working_dir = "."
log_file = os.path.join(home_dir, working_dir, 'syslog.txt')


error_list = []
username = "ahmed.miller"

def parse_log(log_file):
    with open(log_file, mode='r',encoding='UTF-8') as file:
        for log in file.readlines():
            result = re.search(r"ticky: (ERROR|INFO) ([\w ]*).*\(([\w ].*)\)", log)
            if result is None:
                continue
            if username in result.groups():
                error_list.append(log)
    return error_list


error_list = parse_log(log_file)
for item in error_list:
    print(item, end = '')
print(len(error_list))
            
```
