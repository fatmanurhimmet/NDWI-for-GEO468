#!/usr/bin/env python
# coding: utf-8

# In[5]:


get_ipython().system('python --version')


# In[6]:


conda install -c conda-forge matplotlib 


# In[154]:


import rasterio
from rasterio import plot
import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv
get_ipython().run_line_magic('matplotlib', 'inline')


# In[155]:


import os


# In[156]:


os.listdir('Desktop/Dersler/rasterio deneme')


# In[157]:


sentinel_rgb = rasterio.open('Desktop/Dersler/rasterio deneme/subset5_sentinel_rgb.tif') #RGB Bands


# In[158]:


# define constants
figure_border = 25
epsilon = 0.0001
max_y = 5000
max_steps = 500
square_side = 20
threshold_for_ndwi = 0.2
threshold_for_ship = 2


# In[159]:


sentinel_rgb.bounds


# In[160]:


sentinel_rgb.crs


# In[161]:


sentinel_rgb.transform


# In[162]:


sentinel_rgb.indexes


# In[163]:


sentinel_rgb.read(3)


# In[164]:


img = sentinel_rgb.read(3)


# In[165]:


show(img)


# In[166]:


#producing RGB map with sentinel image
from rasterio.plot import show, adjust_band
imgdata = np.array([adjust_band(sentinel_rgb.read(i)) for i in (4,3,2)])
show(imgdata*10)  # factor 10 to increase brightness


# In[ ]:


#NDWI Bands green and NIR
band3 = rasterio.open('Desktop/Dersler/rasterio deneme/sentinel_band3.tif') #green


# In[ ]:


band8 = rasterio.open('Desktop/Dersler/rasterio deneme/sentinel_band8.tif') #NIR


# In[213]:


band3.height
band3.width
band3.crs
band3.transform


# In[214]:


band8.height
band8.width
band8.crs
band8.transform


# In[215]:


band3.read(1)
band8.read(1)


# In[170]:


plot.show(band3)


# In[171]:





# In[216]:


plot.show(band3)
plot.show(band8)


# In[217]:


#multiple band representation
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
plot.show(band3, ax=ax1, cmap='Greys') #green
plot.show(band8, ax=ax2, cmap='Greys') #nir
fig.tight_layout()


# In[218]:


green = band3.read(1).astype('float64')
nir = band8.read(1).astype('float64')


# In[175]:


#NDWI calculation, 5 for eliminating the 0 value of equation
ndwi=((nir-green-5)/(nir+green+5))


# In[ ]:





# In[ ]:





# In[178]:


#export NDWI image
ndwiImage = rasterio.open('Desktop/sentinel_output_ndwi.tif','w',driver='Gtiff',
                          width=band8.width, 
                          height = band8.height, 
                          count=1, crs=band8.crs, 
                          transform=band8.transform,
                         dtype='float64')
ndwiImage.write(ndwi,1)
ndwiImage.close()


# In[179]:


#plot NDWI
ndwiImage = rasterio.open('Desktop/sentinel_output_ndwi.tif') 
fig = plt.figure(figsize=(18,12))
plot.show(ndwiImage, cmap='gray')


# In[210]:


#plot NDWI
ndwi2 = rasterio.open('Desktop/sentinel_output_ndwi.tif')
fig = plt.figure(figsize=(18,12))
plot.show(ndwi)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




