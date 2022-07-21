# Outline of Capstone Project 4

## Automate updating catalog information

### Part 4 - Uploading the descriptions

The Django server is already set up to show the fruit catalog for your company. You can visit the main website by entering `linux-instance-IP-Address` in the URL bar or by removing /media/images from the existing URL opened earlier. 

Check out the Django REST framework, by navigating to `linux-instance-IP-Address/fruits` in your browser.

Currently, there are no products in the fruit catalog web-server. You can create a test fruit entry by entering the following into the content field:

```
{
    "name": "Test Fruit",
    "weight": 100,
    "description": "This is the description of my test fruit", "image_name": "icon.sheet.png"
}
```

After entering the above data into the content field click on the POST button. Now visit the main page of your website (by going to `http://[linux-instance-external-IP]/`), and the new test fruit you uploaded appears.

To add fruit images and their descriptions from the supplier on the fruit catalog web-server, create a new Python script that will automatically POST the fruit images and their respective description in JSON format.

Write a Python script named `run.py` to process the text files `(001.txt, 003.txt ...)` from the `supplier-data/descriptions` directory. The script should turn the data into a JSON dictionary by adding all the required fields, including the image associated with the fruit (image_name), and uploading it to `http://[linux-instance-external-IP]/fruits` using the Python requests library.

The data model in the Django application fruit has the following fields: `name`, `weight`, `description` and `image_name`. The weight field is defined as an integer field. So when you process the weight information of the fruit from the .txt file, you need to convert it into an integer. For example if the weight is "500 lbs", you need to drop "lbs" and convert "500" to an integer.

The image_name field will allow the system to find the image associated with the fruit. Don't forget to add all fields, including the image_name! The final JSON object should be similar to:

```
{
    "name": "Watermelon",
    "weight": 500,
    "description": "Watermelon is good for relieving heat, eliminating annoyance and quenching thirst. It contains a lot of water, which is good for relieving the symptoms of acute fever immediately. The sugar and salt contained in watermelon can diuretic and eliminate kidney inflammation. Watermelon also contains substances that can lower blood pressure.", "image_name": "010.jpeg"}
```

Iterate over all the fruits and use post method from Python requests library to upload all the data to the URL `http://[linux-instance-external-IP]/fruits`

pseudo code
```
Libraries:
    os
    requests
    json



function upload_description(path, url){

    create an empty description json object
    create a keys lists 

    store files into a list
    loop through each file, opening it with read attribute
        enumerate through each line of the file
            add the line as json value to the json file 
        create a post request, storing the response object
            check response ok
    
end
}
```