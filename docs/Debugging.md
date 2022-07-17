# Debugging Techniques

## General steps
Ensure documentation through each of the following steps
* Gather Information 
* Find the root cause 
* Long term remediation/prevention

<hr>

## System Tools

Some tools to help find the root cause
* `strace <file_name>`:   Calls that the programs running on our computer make to the kernel

    ```
        strace -o <output_file> <executable_file>
        strace <executable_file> | less
    ```
    In the simplest case strace runs the specified command until it exits.  It intercepts and records the system calls which arecalled by a process and the signals which are received by a process.  The name of each system call, its arguments and its return value are printed on standard error or to the filespecified with the -o option. [more...](https://man7.org/linux/man-pages/man1/strace.1.html)

## Addressing Slowness

Identifying an application bottleneck
* cpu time (close unnessary running programs)
* disk space (uninstall unused applications or delete/move data from the disk)
* network bandwidth (stop other processes using the network)
Identifying a hardware slowdown
* CPU | disk I/O | network connection | graphics card

`top`: This tool let's us see which currently running processes are using the most CPU time

`iotop`: Displays read and write speeds of a storage device, the percentage of time the process spent waiting for I/O, etc.

`iftop`: Listens to the network traffic on specific interface and displays bandwidth usage in the table.


