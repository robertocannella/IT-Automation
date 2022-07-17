# Debugging Resources Techniques Bash/Python

Contians useful resources and samples of typical debugging/resource improvement techniques.

## General steps
Ensure documentation through each of the following steps
* Gather Information 
* Find the root cause 
* Long term remediation/prevention

<hr>

## Monitoring resources
Check out the following links for more information:

[Mircrosoft Process Monitor](https://docs.microsoft.com/en-us/sysinternals/downloads/procmon)

[Linux Performance](http://www.brendangregg.com/linuxperf.html)

[The USE Method](http://brendangregg.com/usemethod.html)

[Activity Monitor in Mac](https://support.apple.com/en-au/guide/activity-monitor/welcome/mac)

[Performance Monitor on Windows10](https://www.windowscentral.com/how-use-performance-monitor-windows-10)

[Resource Monitor on Windows7](https://www.digitalcitizen.life/how-use-resource-monitor-windows-7)

[Microsoft Process Explorer](https://docs.microsoft.com/en-us/sysinternals/downloads/process-explorer)


[nice levels](https://www.reddit.com/r/linux/comments/d7hx2c/why_nice_levels_are_a_placebo_and_have_been_for_a/)

## System Tools

Some tools to help find the root cause
* `strace <file_name>`:   Calls that the programs running on our computer make to the kernel

    ```
        strace -o <output_file> <executable_file>
        strace <executable_file> | less
    ```
    In the simplest case strace runs the specified command until it exits.  It intercepts and records the system calls which arecalled by a process and the signals which are received by a process.  The name of each system call, its arguments and its return value are printed on standard error or to the filespecified with the -o option. [more...](https://man7.org/linux/man-pages/man1/strace.1.html)

* `psutil` (process and system utilities): a cross-platform library for retrieving information on running processes and system utilization (CPU, memory, disks, network, sensors) in Python. [more...](https://pypi.org/project/psutil/)
    * `psutil.cpu_percent()`: shows that CPU utilization
    * `psutil.disk_io_counters()`: byte read and write for disk I/O
    * `psutil.net_io_counters()`: byte received and send for newtork I/O bandwidth

* `rsync` (remote sync): a utility for efficiently transferring and synchronizing files between a computer and an external hard drive and across networked computers by comparing the modification time and size of files. [more1...](https://linux.die.net/man/1/rsync) [2...](linuxtechi.com/rsync-command-examples-linux/)
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
<hr>

## Addressing Slowness

Identifying an application bottleneck
* cpu time (close unnessary running programs)
* disk space (uninstall unused applications or delete/move data from the disk)
* network bandwidth (stop other processes using the network)
Identifying a hardware slowdown
* CPU | disk I/O | network connection | graphics card

    `top`: This tool let's us see which currently running processes are using the most CPU time [more...](https://man7.org/linux/man-pages/man1/top.1.html)

    `iotop`: Displays read and write speeds of a storage device, the percentage of time the process spent waiting for I/O, etc. [more...](https://linux.die.net/man/1/iotop)

    `iftop`: Listens to the network traffic on specific interface and displays bandwidth usage in the table. [more...](https://linux.die.net/man/8/iftop)

## Memory Access Times

Fastest readtime: CPU internal memory

Fast readtime: RAM 

Slower readtime: DISK

Slowest readtime: NETWORK


**Cache**: A cache stores data in a form that's faster to access than its original form. [more...](https://en.wikipedia.org/wiki/Cache_(computing))

What happens when you run out of RAM? At first, the OS will just remove from RAM anything that's cached, but not strictly necessary. If there's still not enough RAM after that, the operating system will put the parts of the memory that aren't currently in use onto the hard drive in a space called swap. Reading and writing from disk is much slower than reading and writing from RAM


## Web Server Debugging

`ab`(apache benchmark): ab is a tool for benchmarking your Apache Hypertext Transfer Protocol (HTTP) server.[more...](https://httpd.apache.org/docs/2.4/programs/ab.html)

## Process Priority

`renice`: alter priority of running processes. [more...](https://man7.org/linux/man-pages/man1/renice.1.html)

shell script:

    ```
    for pid in $( pidof <command>); do renice 19 $pid; done
    ```
