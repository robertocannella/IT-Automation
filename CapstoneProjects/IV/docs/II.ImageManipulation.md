# Outline of Capstone Project 4

## Automate updating catalog information

### Part 2 - Working with supplier images

In this section, you will write a Python script named `changeImage.py` to process the supplier images. You will be using the PIL library to update all images within `~/supplier-data/images` directory to the following specifications:

* Size: Change image resolution from 3000x2000 to 600x400 pixel
* Format: Change image format from .TIFF to .JPEG

*Note: The raw images from images subdirectory contains alpha transparency layers. So, it is better to first convert RGBA 4-channel format to RGB 3-channel format before processing the images. Use convert("RGB") method for converting RGBA to RGB image.*

pseudo code
```
Libraries: 
    os
    sys
    Image from PIL

------------------------------------------------

function get_images_as_list (path){
    
    create an empty list of images

    store all items of path into a list
    loop through directory list
        check if the listing is a file
            check if the file is hidden '.'
                append the list of images with this file
    
    return the list of images

end

-----------------------------------------------

}
function resize_and_format(image_list) {

    loop through the image list
        create a new PIL image object
        resize the current image object
        convert the current image object
end       
}


```


After processing the images, save them in the same path `~/supplier-data/images`, with a `JPEG` extension.