# -*- coding: utf-8 -*-
"""
Created on Sun Jul 29 16:15:47 2018

@author: GM Zhu
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 01:41:30 2018

@author: 朱高明
"""
#step 0 file 0 grain 1, step 1 file5 grain 28, step2 file1 grain29, step 5 file6 grain 47, step 10 file 9 grain 95, step 13 file 7 grain 42
#step0 file0 grain 46, step5 file3 grian 37
#step0 file0 grain 58, step 3 file3 grain 82, step5 file7 grain 79, step6 file9 grain48, step8 file3 grain23, step10 file7 grain 95, 

import math
import os  #遍历文件
import PIL.Image as PI  #切图
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import time
from colorama import Fore  # color
import gc #清除缓存

font = {'family': 'Arial'}

start_time = time.clock()
grain_No = 1
step = 15

def inlog(file_path):   #define a function to import log file
    x = pd.read_table(file_path, skiprows = 19, sep = '\s+|,', header = None)
    xM = x.ix[:, 0 : 5]
    xMatrix = np.matrix(xM)
    return(xMatrix)
#logMatrix = inlog('Mg_30deg_qtrdeg_0_t200.log')
#print(logMatrix)

def inflt(file_path):  #define a function to import flt file
    x = pd.read_table(file_path, sep = '\s+|,', header = None)
    xM = x.ix[:, 0 : 30]
    xMatrix = np.matrix(xM)
    return(xMatrix)
#fltMatrix = inflt('Mg_30deg_qtrdeg_0_t200.flt')
#print(fltMatrix)

logMatrix = inlog(r'G:\SynchrotronXray\DESY_June_2018\LOG\ten_times\Mg_30deg_qtrdeg_0_file0_t100.log')      
fltMatrix = inflt(r'G:\SynchrotronXray\DESY_June_2018\FLT\Mg_30deg_qtrdeg_0_t100.flt')      

#--------------------the following lines are to import all the tif files--------------
file_names = os.listdir(r'G:\SynchrotronXray\DESY_June_2018\Diffraction spot\(100-1000)\Mg_30deg_qtrdeg_' + str(step))       #get the file names
a = 'G:/SynchrotronXray/DESY_June_2018/Diffraction spot/(100-1000)/Mg_30deg_qtrdeg_' + str(step) + '/'

image_list = []

i = 0
while i < 561:   #import all files
    file_path = a + file_names[i]
    im = PI.open(file_path, 'r')    #import single file
    image_list.append(im)   #can use image_list[i] in the next
#    print(i+1)
    i += 1
#image_list[5].show()
print(Fore.YELLOW + time.asctime(time.localtime(time.time())), ':All tif images are imported; cost', '%s seconds' % (time.clock() - start_time))
print(Fore.RESET + '--------------------------------')
#print('---%s seconds---' % (time.clock() - start_time))



#while grain_No < 124:
    
#----------------------find peakids in log file for single grain-----------
#    grain_No = 8
i = 0
while i < len(logMatrix):
    if str(logMatrix[i, 0]) == 'Grain':
        if int(logMatrix[i, 1]) == grain_No:
            peakids = np.zeros(int(logMatrix[i, 3]))
            hkil = np.zeros((int(logMatrix[i, 3]), 4))
            j = 0
            while j < len(peakids):
                peakids[j] = int(logMatrix[i + 12 + j, 2])
                hkil[j, 0] = int(logMatrix[i + 12 + j, 3])
                hkil[j, 1] = int(logMatrix[i + 12 + j, 4])
                hkil[j, 2] = -(hkil[j, 0] + hkil[j, 1])
                hkil[j, 3] = int(logMatrix[i + 12 + j, 5])
                j += 1
    i += 1
print(peakids)
print(hkil)
print(Fore.YELLOW + str(time.asctime(time.localtime(time.time()))), ':peakids was all found; cost', '%s seconds' % (time.clock() - start_time))
print(Fore.RESET + '--------------------------------')

#----------------------find diffraction spots positions and intensities-----------
i = 0
positions = np.zeros((len(peakids),6))
while i < len(peakids):
    j = 1
    while j < len(fltMatrix):
        if peakids[i] == int(fltMatrix[j, 29]):
#            positions = np.zeros((len(peakids),6))
            positions[i, 0] = peakids[i]    #peak id
            positions[i, 1] = float(fltMatrix[j, 0])     #sc(position_y)
            positions[i, 2] = float(fltMatrix[j, 1])     #fc(position_x)
            positions[i, 3] = float(fltMatrix[j, 2])     #omega
            positions[i, 4] = round((70.5 + positions[i, 3]) * 4 + 1)    #integer, represent the tif file number
            if positions[i, 4] > 561:
                positions[i, 4] = 561
            if positions[i, 4] < 1:
                positions[i, 4] = 1
            positions[i, 5] = float(fltMatrix[j, 13])    #sum_intensity
        j += 1
    i += 1
print(positions)
print(Fore.YELLOW + str(time.asctime(time.localtime(time.time()))), ':positions and intensities were all found; cost', '%s seconds' % (time.clock() - start_time))
print(Fore.RESET + '--------------------------------')

#----------------------plot all diffractinos spots-----------

left = np.zeros(len(positions))
right = np.zeros(len(positions))
top = np.zeros(len(positions))
bottom = np.zeros(len(positions))
numbers = np.zeros(len(positions))

i = 0    #calculate the range of x and y
while i < len(positions):
    left[i] = math.ceil(positions[i, 2]/10) * 10 - 30   #向上取整，2.3 = 3
    right[i] = left[i] + 50
    top[i] = math.ceil(positions[i, 1]/10) * 10 - 30
    bottom[i] = top[i] +50
    numbers[i] = i
    i += 1

i = 0   #correct the range of x and y
while i < len(positions):
    if left[i] < 0:
        left[i] = 0
        right[i] = 50
    if top[i] < 0:
        top[i] = 0
        bottom[i] = 50
    if right[i] > 2048:
        right[i] = 2040
        left[i] = 1990
    if bottom[i] > 2048:
        bottom[i] = 2040
        top[i] = 1990       
    i += 1

print(left, right, top, bottom)
print(Fore.YELLOW + str(time.asctime(time.localtime(time.time()))), ':x and y positions were corrected; cost', '%s seconds' % (time.clock() - start_time))
print(Fore.RESET + '--------------------------------')

#region_list = []
#i = 0
#while i < 561:
#    croped_image = image_list[i].crop((left[i], top[i], right[i], bottom[i]))
#    region_list.append(croped_image)
#    i += 1

print(Fore.YELLOW + str(time.asctime(time.localtime(time.time()))), ':regions were cutted; cost', '%s seconds' % (time.clock() - start_time))
print(Fore.RESET + '--------------------------------')

plt.figure(figsize = (40,30))   #plot a big image   #num = 'diffraction spots',

i = 0
while i < len(positions):
    plt.subplot(math.ceil(len(positions)/12), 12, i+1)
    plt.title('Number %s' %(int(numbers[i]) + 1), fontsize = 10)
    tif_No = int(positions[i,4])
    croped_image = image_list[tif_No-1].crop((left[i], top[i], right[i], bottom[i]))
#    region_list.append(croped_image)
    plt.imshow(croped_image, extent = [left[i], right[i], bottom[i], top[i]], cmap=plt.cm.gray, vmin=0, vmax=256)
#    font ={'family': 'Arial'}
    
    circle1=plt.Circle((1074.1232,999.26874), math.sqrt((float(positions[i, 2]) - 1074.1232) ** 2 + (float(positions[i, 1]) - 999.26874) ** 2), color='r', fill = False)  #circle   
    plt.gcf().gca().add_artist(circle1)
    plt.plot([1074.1232, float(positions[i, 2])], [999.26874, float(positions[i, 1])], '--')  #radius
    
    plt.text(left[i] + 39.5, top[i] + 3, 'hkil=', ha='right', fontsize = 9, fontname = 'Arial')   #hkil = 
    plt.text(left[i] + 42, top[i] + 3, str(int(hkil[i, 0])), ha='right', fontsize = 9, fontname = 'Arial')
    plt.text(left[i] + 44.5, top[i] + 3, str(int(hkil[i, 1])), ha='right', fontsize = 9, fontname = 'Arial')
    plt.text(left[i] + 47, top[i] + 3, str(int(hkil[i, 2])), ha='right', fontsize = 9, fontname = 'Arial')
    plt.text(left[i] + 49.5, top[i] + 3, str(int(hkil[i, 3])), ha='right', fontsize = 9, fontname = 'Arial')

    plt.text(left[i] + 39.5, top[i] + 6, 'tif_No=', ha='right', fontsize = 9, fontname = 'Arial')   #tif =
    plt.text(left[i] + 40, top[i] + 6, str(tif_No), ha = 'left', fontsize = 9, fontname = 'Arial')
    
    plt.text(left[i] + 39.5, top[i] + 9, 'Angel=', ha='right', fontsize = 9, fontname = 'Arial')   #Rotation angle =
    plt.text(left[i] + 40, top[i] + 9, str(round(round(positions[i, 3]*4)/4, 2)), ha = 'left', fontsize = 9, fontname = 'Arial')
    
    plt.xticks(np.arange(left[i], right[i], 10), fontsize = 10, fontname = 'Arial')
    plt.axis([left[i], right[i],  bottom[i], top[i]])
    plt.yticks(np.arange(top[i], bottom[i], 10), fontsize = 10, fontname = 'Arial')
    plt.grid(True)       #网格
    i += 1
plt.savefig('Diffraction_spots_of_grain_' + str(grain_No) + '(Mg_30deg_step' + str(step) + '_(use_position_step0).png', dpi = 200, bbox_inches = 'tight')
#plt.show()
grain_No += 1
del bottom, croped_image, hkil, i, j, left, numbers, peakids, positions, right, tif_No, top, circle1
gc.collect()

print(Fore.YELLOW + str(time.asctime(time.localtime(time.time()))), ':Done; cost', '%s seconds' % (time.clock() - start_time))
print(Fore.RESET + '--------------------------------')
 
















