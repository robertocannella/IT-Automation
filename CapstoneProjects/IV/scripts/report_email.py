#!/usr/bin/env python3

import os
import datetime
import reports
import emails

data = [['name', 'weight', 'description', 'image_name']]
pdf_keys = ['name', 'weight']
pdf_data = [[]]
HOME = os.path.expanduser("~")
data_dir = HOME+'/supplier-data/descriptions/'
attachment_path = '/tmp/processed.pdf'
files = os.listdir(data_dir)



def make_pdf_body():
    for file in files:
        with open(os.path.join(data_dir, file), 'r') as fh:
            current_item = []
            for index,line in enumerate(fh):
                if index > 1:
                    break
                current_item.append(pdf_keys[index])
                current_item.append(line.replace('\n', ''))
                pdf_data.append(current_item)
                current_item = []
            pdf_data.append(' ')
    return pdf_data

def main():
    pdf_data = make_pdf_body()
    title = 'Processed Update on {}<br />'.format(datetime.datetime.now().strftime("%B %d, %Y"))
    attachment_path = '/tmp/processed.pdf'
    reports.generate_report(pdf_data, title, attachment_path)
    
    #set email parameters
    sender = 'automation@example.com'
    recipient = '<REPLACE THIS>'
    subject = 'Upload Completed - Online Fruit Store'
    body = 'All fruits are uploaded to our website successfully. A detailed list is attached to this email.'

    email = emails.generate_email(sender, recipient, subject, body, attachment_path)
    print(email)
    #emails.send(email)

if __name__ == "__main__":
    main()