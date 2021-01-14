# Special Topics in Remote Sensing Homework
## Basic Ship and Bridge Detection by Using Normalized Difference Water Index
### Fatmanur Himmet 0101626
This code calculates the NDWI of Sentinel 2A image in Kocaeli Gulf region. Satellite image taken from this area shows Osmangazi Bridge and ships on the sea. So the NDWI enable us to separate these ships, the bridge and coastal line from the sea. 

***
### Image Properties
Sentinel 2A image which is taken from the satellite the date 12.08.2020. 

***
### Used Image Bands
- __Band 4, Band 3 and Band 2 which are Red, Green and Blue Bands for RGB True Colors__
- __Band 8 which is NIR Band__

***
### Jupyter Notebook which have pyhton 3.6.12 version and its libraries in conda environment were used in this project.
 __Libraries__
- Rasterio
- Matplotlib
- Numpy
- Opencv

***
### __The RGB colors of the image is shown:__ 
-![RGB Image Plot](RGB_Image_Plot.JPG)
### __Band3 and Band8 Plots which are Used for NDWI:__
-![Band3_Band8_Plot](Band3_Band8_Plot.JPG)

-NDWI = Band3 - Band8 / Band3 + Band8


