#!/usr/bin/env python3

import os
import shutil
import sys
import socket
import psutil

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

def check_cpu_constrained():
    """Returns True if the cpu is having to much usage, False otherwise"""
    is_not_constrained = True
    count = psutil.cpu_count()
    for i in range(count):
        print("Checking CPU:{} percent..".format(i+1) ,end = '')
        percentage = psutil.cpu_percent(i+1)
        print(percentage, '%')

    return psutil.cpu_percent(1) > 75

def main():
    checks = [
        (check_reboot, "Pending reboot"),
        (check_root_full, "Root partition full."),
        (check_no_network, "No working network"),
        (check_cpu_constrained, "CPU is constrained")
    ]
    everything_ok = True
    for check, msg in checks:
        if check():
            print(msg)
            everything_ok = False

    if not everything_ok:
        sys.exit(1)


    print("Everything is fantastic!")
    sys.exit(0)
main()