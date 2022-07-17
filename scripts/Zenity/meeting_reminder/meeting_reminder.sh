#!/bin/bash


#TODO: SMTP SERVER MUST BE CONFIGURED TO USE THIS FILE
# This is only a test file

meeting_info=$(zenity --forms \
        --title 'Meeting' \
        --text 'Reminder information' \
        --add-calendar 'Date' \
        --add-entry 'Title' \
        --add-entry 'Emails' \
        --forms-date-format="%Y-%m-%d" \
        2>/dev/null)

if [[ -n "$meeting_info" ]]; then 
    python3 send_reminders.py "$meeting_info"
fi
