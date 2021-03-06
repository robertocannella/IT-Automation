# Outline of Capstone Project 4

## Automate updating catalog information

### Part 1 - Fetching supplier data


You'll first need to get the information from the supplier that is currently stored in a Google Drive file. The supplier has sent data as large images with an associated description of the products in two files (.TIF for the image and .txt for the description).

Here, you'll find two script files download_drive_file.sh and the example_upload.py files. 

To download the file from the supplier onto our linux-instance virtual machine we will first grant executable permission to the download_drive_file.sh script.

```
sudo chmod +x ~/download_drive_file.sh
```

Run the download_drive_file.sh shell script with the following arguments:

```
./download_drive_file.sh 1LePo57dJcgzoK4uiI_48S01Etck7w_5f supplier-data.tar.gz
```

You have now downloaded a file named supplier-data.tar.gz containing the supplier's data. Let's extract the contents from this file using the following command:

```
tar xf ~/supplier-data.tar.gz
```
The subdirectory `images` contain images of various fruits, while the descriptions subdirectory has text files containing the description of each fruit. 

The first line contains the name of the fruit followed by the weight of the fruit and finally the description of the fruit.


```
Mango
300 lbs
Mango contains higher levels of vitamin C than ordinary fruits. Eating mango can also reduce cholesterol and triglycerides and help prevent cardiovascular disease.  Due to its high level of vitamins, regular consumption of mango play an important role in improving body function and moisturizing the skin.
```

