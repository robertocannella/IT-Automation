# Outline of Capstone Project 4

## Automate updating catalog information

### Part 6 - Configure Health Checks

This is the last part of the lab, where you will have to write a Python script named health_check.py that will run in the background monitoring some of your system statistics: CPU usage, disk space, available memory and name resolution. Moreover, this Python script should send an email if there are problems, such as:

* Report an error if CPU usage is over 80%
* Report an error if available disk space is lower than 20%
* Report an error if available memory is less than 500MB
* Report an error if the hostname "localhost" cannot be resolved to "127.0.0.1"


Complete the script to check the system statistics every 60 seconds, and in event of any issues detected among the ones mentioned above, an email should be sent with the following content:

**From**: automation@example.com

**To**: username@example.com
* Replace username with the username given in the Connection Details Panel on the right hand side.


**Subject line**:

<table><tr><th>Case</th><th>Subject line</th></tr>

<tr><td>

CPU usage is over 80%
</td><td>
Error - CPU usage is over 80%
</td></tr><tr><td>
Available disk space is lower than 20%
</td><td>
Error - Available disk space is less than 20%
</td></tr><tr><td>
available memory is less than 500MB
</td><td>
Error - Available memory is less than 500MB
</td></tr><tr><td>
hostname "localhost" cannot be resolved to "127.0.0.1"
</td><td>
Error - localhost cannot be resolved to 127.0.0.1
</td></tr>
</table>
E-mail Body: Please check your system and resolve the issue as soon as possible

*Note: There is no attachment file here, so you must be careful while defining the generate_email() method in the emails.py script or you can create a separate generate_error_report() method for handling non-attachment email.*

pseudo code
```


* ALL CHECKS SHOULD RETURN TRUE IF TRIGGERED * 

Libraries
    psutil
    shutil
    emails
    socket

function check_cpu_constrained(min_percent){

    return psutil.cpu_percent > min_percent
end
}

function check_disk_percent(disk, min_percent){

    set du to  shutil.disk_usage(disk)
    calculate percent free = du.free / du.total
    return percent_free < min_percent>
end    
}

function check_memfree(min_amount){

    v_mem = psutil.virtual_memory()
    return v_mem.available > min_amount
end
}

function check_resolve_addr(hostname,addr){

    return socket.gethostbyname(hostname) is not addr
end
}

function main(){

    checks = [ (add list of checks , corresponding messages) ]
    set sender
    set recipient
    set body

    loop through checks and messages
        if check() is true
            email emails.generate_email_no_attachment(sender, recipient, subject(message), body)
            emails.send
end
}
