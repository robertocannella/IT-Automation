#!/usr/bin/env python3

import os
import re
import operator
from pprint import pprint

home_dir = os.path.expanduser('~')
working_dir = "."
log_file = os.path.join(home_dir, working_dir, 'syslog.txt')


error_list = []
username = "ahmed.miller"
error_dict = {}
per_user_dict = {}
info_dict = {}

def parse_log(log_file):
    with open(log_file, mode='r',encoding='UTF-8') as file:
        for log in file.readlines():
            result = re.search(r"ticky: (ERROR|INFO) ([\w ]*).*\(([\w ].*)\)", log)
            if result is None:
                continue
            # result[1] = LOGTYPE, result[2] = DESC. result[3] = user

            # Handle error dictionary here:
            if result[1] == 'ERROR':
                if result[2] not in error_dict:
                    error_dict[result[2]] = 1
                else:
                    error_dict[result[2]] += 1
                if result[3] not in per_user_dict:
                    per_user_dict[result[3]] = {'ERROR': 1, 'INFO': 0}
                else:
                    per_user_dict[result[3]]['ERROR'] += 1
    
            # Handle info dictionary here:
            if result[1] == 'INFO':
                if result[2] not in info_dict:
                    info_dict[result[2]] = 1
                else:
                    info_dict[result[2]] += 1
                if result[3] not in per_user_dict:
                    per_user_dict[result[3]] = {'ERROR': 0, 'INFO': 1}
                else:
                    per_user_dict[result[3]]['INFO'] += 1
    return (error_dict, info_dict, per_user_dict)


error_dict,info_dict, per_user_dict = parse_log(log_file)
# for item in error_list:
#     print(item, end = '')
sorted_error = sorted(error_dict.items(), key=operator.itemgetter(1), reverse=True)
sorted_per_user = sorted(per_user_dict.items())
pprint(sorted_error)
pprint(sorted_per_user)