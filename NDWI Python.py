#!/usr/bin/env python
# coding: utf-8
get_ipython().system('python --version')
conda install -c conda-forge matplotlib 

import rasterio
from rasterio import plot
import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv
get_ipython().run_line_magic('matplotlib', 'inline')

import os
os.listdir('Desktop/Dersler/rasterio deneme')
sentinel_rgb = rasterio.open('Desktop/Dersler/rasterio deneme/subset5_sentinel_rgb.tif') #RGB Bands


# define constants
figure_border = 25
epsilon = 0.0001
max_y = 5000
max_steps = 500
square_side = 20
threshold_for_ndwi = 0.2
threshold_for_ship = 2



sentinel_rgb.bounds
sentinel_rgb.crs
sentinel_rgb.transform
sentinel_rgb.indexes
sentinel_rgb.read(3)

img = sentinel_rgb.read(3)
show(img)



#producing RGB map with sentinel image
from rasterio.plot import show, adjust_band
imgdata = np.array([adjust_band(sentinel_rgb.read(i)) for i in (4,3,2)])
show(imgdata*10)  # factor 10 to increase brightness


#NDWI Bands green and NIR
band3 = rasterio.open('Desktop/Dersler/rasterio deneme/sentinel_band3.tif') #green
band8 = rasterio.open('Desktop/Dersler/rasterio deneme/sentinel_band8.tif') #NIR

band3.height
band3.width
band3.crs
band3.transform

band8.height
band8.width
band8.crs
band8.transform

band3.read(1)
band8.read(1)
plot.show(band3)
plot.show(band8)

#multiple band representation
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
plot.show(band3, ax=ax1, cmap='Greys') #green
plot.show(band8, ax=ax2, cmap='Greys') #nir
fig.tight_layout()

green = band3.read(1).astype('float64')
nir = band8.read(1).astype('float64')

#NDWI calculation, 5 for eliminating the 0 value of equation
ndwi=((nir-green-5)/(nir+green+5))

#export NDWI image
ndwiImage = rasterio.open('Desktop/sentinel_output_ndwi.tif','w',driver='Gtiff',
                          width=band8.width, 
                          height = band8.height, 
                          count=1, crs=band8.crs, 
                          transform=band8.transform,
                         dtype='float64')
ndwiImage.write(ndwi,1)
ndwiImage.close()

#plot NDWI
ndwiImage = rasterio.open('Desktop/sentinel_output_ndwi.tif') 
fig = plt.figure(figsize=(18,12))
plot.show(ndwiImage, cmap='gray')


#plot NDWI
ndwi2 = rasterio.open('Desktop/sentinel_output_ndwi.tif')
fig = plt.figure(figsize=(18,12))
plot.show(ndwi)

#added histogram code is belows
#plot a histogram NDWI
def image_histogram(ndwi2):
    from rasterio.plot import show_hist
    co, ce =show_hist(ndwi)
    fig = plt.figure(figsize=(10,7))
    fig.set_facecolor('yellow')
    plt.plot(ce[1::], co[1::])
    plt.show()
get_ipython().run_line_magic('matplotlib', 'inline')
image_histogram(ndwi2) 






















