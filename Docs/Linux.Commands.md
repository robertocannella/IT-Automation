# Linux Commands


## Utility
`ps` displays information about a selection of the active processes.

`top` display Linux processes

`wc <file_name>`: counts the amount of characters, words, and lines in the given file; can also count the same values of whatever it receives via stdin

`file <file_name>`: prints the type of the given file, as recognized by the operating system

`sort <file_name>`: sorts the lines of the file alphabetically

`cut -d[separator] -f[fields] <file_name>`: for each line in the given file, splits the line according to the given separator and prints the given fields (starting from 1)
**useful when parsing log files*

`who`: prints the list of users currently logged into the computer

`uptime`: shows how long the computer has been running

`killall`: sends a signal to all processes running any of the specified commands. If no signal name is specified, `SIGTERM` is sent
<table><th>Signal Name</th><th>Signal value</th><th>Effect</th>
<tr><td>SIGHUP</td><td>1</td><td>Hangup</td></tr>
<tr><td>SIGINT</td><td>2</td><td>Interrupt from keyboard</td></tr>
<tr><td>SIGKILL</td><td>9</td><td>Kill signal</td></tr>
<tr><td>SIGTERM</td><td>15</td><td>Termination signal</td></tr>
<tr><td>SIGSTOP</td><td>17,19,23</td><td>Stop the process</td></tr>
</table>
	

## Networking 


<hr>

## System

`systemctl`: The systemctl command is a utility which is responsible for examining and controlling the systemd system and service manager.[more...](https://www.liquidweb.com/kb/what-is-systemctl-an-in-depth-overview/)

<hr>

## Program functionality
<hr>

## Piping

<hr>

## Python Modules

`glob`: The glob module finds all the pathnames matching a specified pattern according to the rules used by the Unix shell, although results are returned in arbitrary order. Akin to taking advantage of star [*] in BASH.