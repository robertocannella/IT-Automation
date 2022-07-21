# Outline of Capstone Project 4

## Automate updating catalog information

### Part 3- Uploading images to web server

You have modified the fruit images through changeImage.py script. Now, you will have to upload these modified images to the web server that is handling the fruit catalog. To do that, you'll have to use the Python requests module to send the file contents to the `[linux-instance-IP-Address]/upload` URL.

Copy the external IP address of your instance from the Connection Details Panel on the left side and enter the IP address in a new web browser tab. This opens a web page displaying the text "Fruit Catalog".

In the home directory, you'll have a script named `example_upload.py` to upload images to the running fruit catalog web server. To view the example_upload.py script use the cat command.

Here is the example file:
```
#!/usr/bin/env python3
import requests

# This example shows how a file can be uploaded using 
# the Python Requests module

url = "http;//localhost/upload"
with open ('/usr/share/apache2/icons/icon.sheet.png, 'rb') as opened
    r = requests.post(url, files={'file': opened})
```

In a similar way, you are going to write a script named `supplier_image_upload.py` that takes the jpeg images from the supplier-data/images directory that you've processed previously and uploads them to the web server fruit catalog.

pseudo code
```
Libraries:
    os
    requests

function upload_image(path, url){

    store files into a list
    loop through each file, opening it with read attribute
        create a post request, storing the response object
        check response ok
end
}
```
