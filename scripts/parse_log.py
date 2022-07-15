#!/usr/bin/env python3

import os
import re
import operator
import csv
from pprint import pprint

home_dir = os.path.expanduser('~')
working_dir = "."
log_file = os.path.join(home_dir, working_dir, 'syslog.txt')

# Python Dictionaries
error_dict = {}
per_user_dict = {}
info_dict = {}

# CSV Exports
error_dict_csv = 'error_message.csv'
info_dict_csv = 'info_message.csv'
per_user_csv = 'user_statistics.csv'

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



with open (error_dict_csv, "w", newline='') as csvfile:
    fieldnames = ['Error', 'Count']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for tup in sorted_error:
        writer.writerow({'Error': str(tup[0]), 'Count': str(tup[1])})

with open (per_user_csv, "w", newline='') as csvfile:
    fieldnames = ['Username', 'INFO', 'ERROR']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for tup in sorted_per_user:
        writer.writerow({'Username': str(tup[0]), 'INFO': str(tup[1]['INFO']), 'ERROR': str(tup[1]['ERROR'])})

pprint(sorted_per_user)