# Outline of Capstone Project 4

## Automate updating catalog information

### Part 5 - Generate a PDF report and send it through email

Once the images and descriptions have been uploaded to the fruit store web-server, you will have to generate a PDF file to send to the supplier, indicating that the data was correctly processed. To generate PDF reports, you can use the ReportLab library. The content of the report should look like this:

```
Processed Update on <Today's date>

[blank line]

name: Apple

weight: 500 lbs

[blank line]

name: Avocado

weight: 200 lbs

[blank line]

...

```

Create a script `reports.py` to generate PDF report to supplier.

Using the `reportlab` Python library, define the method `generate_report` to build the PDF reports. We have already covered how to generate PDF reports in an earlier lesson; you will want to use similar concepts to create a PDF report named processed.pdf.

pseudo code reports.py
```
Libraries:
    from reportlab.platypus import SimpleDocTemplate
    from reportlab.platypus import Paragraph, Spacer, Table, Image
    from reportlab.lib.styles import getSampleStyleSheet

function generate_report(paragraph, title, attachment_path, data_path){

    create a report object form SimpleDocTemplate
    set report_title
    set report_paragraph
    build report as processed.pdf

    return processed.pdf
    
end
}
```
Create another script named `report_email.py` to process supplier fruit description data from `supplier-data/descriptions` directory. 


pseudo code report_email.py
```
Libraries:
    os
    datetime
    reports
    emails

function process_body(){

    create a empty keys lists 
    create an empty body string
    store files into a list

    loop through each file, opening it with read attribute
        enumerate through each line of the file
            append the string with keys[index]: line[index]

    return body string 
end
}

function main(){

    set report parameters
    report = reports.generate_report(paragraph, title, attachment_path, data_path)

    set email parameters
    email = emails.generate_email(sender, recipient, subject, body, attachment_path)

    emails.send(email)

end    
}
```

```
if __name__ == "__main__":
    reports.generate_report(attachment, title, paragraph)
    emails.generate_email(sender, recipient, subject, body, attachment_path)
    emails.send_email()
```

Import all the necessary libraries(os, datetime and reports) that will be used to process the text data from the `supplier-data/descriptions` directory into the format above.


Once you have completed this, call the main method which will process the data and call the `generate_report` method from the `reports` module.

You will need to pass the following arguments to the `reports.generate_report` method: 
* the text description processed from the text files as the paragraph argument,
 * the report title as the title argument 
 * the file path of the PDF to be generated as the attachment argument (use `‘/tmp/processed.pdf'`)

pseudo code emails.py
```
Libraries:
    email.message
    mimetypes
    os.path
    smtplib

function generate_email(sender, recipient, subject, body, attachment_path){

    create email.message object
        set FROM, TO, SUBJECT, CONTENT

    process attachment
        use guess mime type 
    
    add attachment to email
        set maintype
        set subtype
        set filename
    
    return message
    
end
}

function send_email(){

    set mail_server
    send message
    quit mail_server

end    
}

```



Once the PDF is generated, you need to send the email using the `emails.generate_email()` and `emails.send_email()` methods.

Create `emails.py` using the nano editor.

Define `generate_email` and `send_email` methods by importing necessary libraries.

Use the following details to pass the parameters to emails.`generate_email()`:

From: automation@example.com

To: username@example.com
* Replace username with the username given in the Connection Details Panel on the right hand side.
Subject line: Upload Completed - Online Fruit Store

E-mail Body: All fruits are uploaded to our website successfully. A detailed list is attached to this email.

Attachment: Attach the path to the file `processed.pdf`


Now, check the webmail by visiting `[linux-instance-external-IP]/webmail`. Here, you'll need a login to roundcube using the username and password mentioned in the Connection Details Panel on the left hand side, followed by clicking Login.

Now you should be able to see your inbox, with one unread email. Open the mail by double clicking on it. There should be a report in PDF format attached to the mail. View the report by opening it.


files structure
```
/scripts|
        |_ reports.py
        |           |- generate_report(args[1,2,3])
        |
        |_ report_email.py
        |           |- main 
        |                   |- reports.generate_report([args 1,2,3])
        |                   |- emails.generate_email([args 1,2,3,4,5])
        |                   |- emails.send_email()
        |
        |_ emails.py
                    |- generate_email([args 1,2,3,4,5])
                    |- send_email()

```