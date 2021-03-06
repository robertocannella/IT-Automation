#!/usr/bin/env python3

import os
import shutil
import socket 
import psutil
import emails

def check_reboot():
    """Returns true if the computer has a pending reboot."""
    home = os.path.expanduser("~")
    return os.path.exists(home+"/run/reboot-required")

def check_disk_full(disk,min_gb, min_percent):
    """Returns True if there isn't enough disk space, False otherwise."""
    du = shutil.disk_usage(disk)
    #calculate the percentage of free space
    percent_free = 100 * du.free / du.total
    #calculate how many free gigabytes
    gigabytes_free = du.free / 2**30
    if gigabytes_free < min_gb or percent_free < min_percent:
        return True
    return False

def check_disk_percent(disk='/', min_percent=20):
    du = shutil.disk_usage(disk)
    percent_free = 100 * du.free / du.total
    return percent_free < min_percent

def check_memfree(min_amount=50000000):
    v_mem = psutil.virtual_memory()
    return v_mem.available < min_amount

def check_resolve_addr(hostname='localhost',addr='127.0.0.1'):
    return socket.gethostbyname(hostname) != addr

def check_cpu_constrained(min_percent=80):
    return psutil.cpu_percent(1) > min_percent

def check_root_full():
    """Returns True if the root partition is full, False otherwise."""
    return check_disk_full(disk='/', min_gb=2,min_percent=10)

def check_no_network():
    """Returns True if it fails to resolve Google's URL, False otherwise."""
    try:
        socket.gethostbyname("www.google.com")
        return False
    except:
        return True



def check_cpu_constrained_multi(min_percent):
    """Returns True if the cpu is having to much usage, False otherwise"""
    count = psutil.cpu_count()
    for i in range(count):
        print("Checking CPU:{} percent..".format(i+1) ,end = '')
        percentage = psutil.cpu_percent(i+1)
        print(percentage, '%')

        return psutil.cpu_percent(1) > min_percent

def main():
    # Add checks heres
    checks = [
        (check_cpu_constrained, "Error - CPU usage is over 80%"),
        (check_disk_percent, "Error - Available disk space is less than 20%"),
        (check_memfree, "Error - Available memory is less than 500MB"),
        (check_resolve_addr, "Error - localhost cannot be resolved to 127.0.0.1")
    ]

    # Email notification settings
    sender = 'automation@example.com'
    recipient = '<CHANGE THIS PART>'
    body = 'Please check your system and resolve the issue as soon as possible.'

    # Run checks here
    for check, msg in checks:
        if check():

            email = emails.generate_email_no_attachment(sender, recipient, msg, body)
            print(email)
            emails.send_message(email)

if __name__ == '__main__':
    main()