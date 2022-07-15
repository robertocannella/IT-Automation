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
