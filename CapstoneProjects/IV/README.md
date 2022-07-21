# Capstone Project Four

## Automate updating catalog information

*Introduction*

You work for an online fruits store, and you need to develop a system that will update the catalog information with data provided by your suppliers. The suppliers send the data as large images with an associated description of the products in two files (.TIF for the image and .txt for the description). The images need to be converted to smaller jpeg images and the text needs to be turned into an HTML file that shows the image and the product description. The contents of the HTML file need to be uploaded to a web service that is already running using Django. You also need to gather the name and weight of all fruits from the .txt files and use a Python request to upload it to your Django server.

You will create a Python script that will process the images and descriptions and then update your company's online website to add the new products.

Once the task is complete, the supplier should be notified with an email that indicates the total weight of fruit (in lbs) that were uploaded. The email should have a PDF attached with the name of the fruit and its total weight (in lbs). 

Finally, in parallel to the automation running, we want to check the health of the system and send an email if something goes wrong. 

What you’ll do
* Write a script that summarizes and processes sales data into different categories 
* Generate a PDF using Python
* Automatically send a PDF by email 
* Write a script to check the health status of the system 


code structure:

```
~/  
 |- download_drive_file.sh
 |- example_upload.py
 |- supplier-data.tar.gz
 |- supplier_data.....
 |                   |- descriptions/00*.txt
 |                   |- images/*.tiff
 |                   |- images/*.jpeg
 |- example_upload.py

/scripts|
        |_ changeImage.py
        |               |- get_images_as_list(path)
        |               |- resize_and_format(image_list)
        |               |- main
        |                       |-get_images_as_list(path)
        |                       |-resize_and_format(image_list)
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
        |           |- generate_email_no_attachment([args 1,2,3,4])
        |           |- generate_email([args 1,2,3,4,5])
        |           |- send_email()
        |
        |- supplier_image_upload.py
        |           |- upload_image(path, url)
        |
        |_ run.py 
        |           |- upload_description(path,url)
        |
        |_ health_check.py
                    |- check_cpu_constrained(min_percent)
                    |- check_disk_full(disk, min_percent)
                    |- check_memfree(min_amount)
                    |- check_resolve_addr(hostname,addr)
                    |- main
                            |- check_cpu_constrained(min_percent)
                            |- check_disk_full(disk, min_percent)
                            |- check_memfree(min_amount)
                            |- check_resolve_addr(hostname,addr)                            

``` 