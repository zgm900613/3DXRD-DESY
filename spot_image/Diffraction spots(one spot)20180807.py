# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 22:26:17 2018

@author: 朱高明
"""

import PIL.Image as PI
import matplotlib.pyplot as plt
import numpy as np
import math

step = 6
tif_Mid = 448
grain_No = 58
file = 0

im = PI.open(r'G:\SynchrotronXray\DESY_June_2018\Diffraction spot\(100-1000)\Mg_30deg_qtrdeg_' + str(step) + '\Mg_30deg_qtrdeg_' + str(step) + '_00' + str(tif_Mid - 5) + '_(100_1000).tif')
im002 = PI.open(r'G:\SynchrotronXray\DESY_June_2018\Diffraction spot\(100-1000)\Mg_30deg_qtrdeg_' + str(step) + '\Mg_30deg_qtrdeg_' + str(step) + '_00' + str(tif_Mid - 4) + '_(100_1000).tif')
im101 = PI.open(r'G:\SynchrotronXray\DESY_June_2018\Diffraction spot\(100-1000)\Mg_30deg_qtrdeg_' + str(step) + '\Mg_30deg_qtrdeg_' + str(step) + '_00' + str(tif_Mid - 3) + '_(100_1000).tif')
im102 = PI.open(r'G:\SynchrotronXray\DESY_June_2018\Diffraction spot\(100-1000)\Mg_30deg_qtrdeg_' + str(step) + '\Mg_30deg_qtrdeg_' + str(step) + '_00' + str(tif_Mid - 2) + '_(100_1000).tif')
im103 = PI.open(r'G:\SynchrotronXray\DESY_June_2018\Diffraction spot\(100-1000)\Mg_30deg_qtrdeg_' + str(step) + '\Mg_30deg_qtrdeg_' + str(step) + '_00' + str(tif_Mid - 1) + '_(100_1000).tif')
im104 = PI.open(r'G:\SynchrotronXray\DESY_June_2018\Diffraction spot\(100-1000)\Mg_30deg_qtrdeg_' + str(step) + '\Mg_30deg_qtrdeg_' + str(step) + '_00' + str(tif_Mid) + '_(100_1000).tif')
im105 = PI.open(r'G:\SynchrotronXray\DESY_June_2018\Diffraction spot\(100-1000)\Mg_30deg_qtrdeg_' + str(step) + '\Mg_30deg_qtrdeg_' + str(step) + '_00' + str(tif_Mid + 1) + '_(100_1000).tif')
im106 = PI.open(r'G:\SynchrotronXray\DESY_June_2018\Diffraction spot\(100-1000)\Mg_30deg_qtrdeg_' + str(step) + '\Mg_30deg_qtrdeg_' + str(step) + '_00' + str(tif_Mid + 2) + '_(100_1000).tif')
im107 = PI.open(r'G:\SynchrotronXray\DESY_June_2018\Diffraction spot\(100-1000)\Mg_30deg_qtrdeg_' + str(step) + '\Mg_30deg_qtrdeg_' + str(step) + '_00' + str(tif_Mid + 3) + '_(100_1000).tif')
im108 = PI.open(r'G:\SynchrotronXray\DESY_June_2018\Diffraction spot\(100-1000)\Mg_30deg_qtrdeg_' + str(step) + '\Mg_30deg_qtrdeg_' + str(step) + '_00' + str(tif_Mid + 4) + '_(100_1000).tif')
im109 = PI.open(r'G:\SynchrotronXray\DESY_June_2018\Diffraction spot\(100-1000)\Mg_30deg_qtrdeg_' + str(step) + '\Mg_30deg_qtrdeg_' + str(step) + '_00' + str(tif_Mid + 5) + '_(100_1000).tif')


N = 11  #number of spots

left = np.zeros(N)
right = np.zeros(N)
top = np.zeros(N)
bottom = np.zeros(N)

positions = np.ones((N, 2))

hkil = np.ones((N, 4))

#grain 58, step0, 1390 1130

i = 0  
while i < N:
    left[i] = 1390
    right[i] = left[i] + 50
    top[i] = 1130
    bottom[i] = top[i] + 50
    positions[i, 0] = 1416.9
    positions[i, 1] = 1155.4
    hkil[i, 0] = 0
    hkil[i, 1] = 0
    hkil[i, 2] = 0
    hkil[i, 3] = 2
    i += 1

region100 = im.crop((left[0], top[0], right[0], bottom[0]))  #裁剪  （左，上，右，下）
region002 = im002.crop((left[1], top[1], right[1], bottom[1]))  #裁剪  （左，上，右，下）
region101 = im101.crop((left[2], top[2], right[2], bottom[2]))  #裁剪  （左，上，右，下）
region102 = im102.crop((left[3], top[3], right[3], bottom[3]))  #裁剪  （左，上，右，下）
region103 = im103.crop((left[4], top[4], right[4], bottom[4]))  #裁剪  （左，上，右，下）
region104 = im104.crop((left[5], top[5], right[5], bottom[5]))  #裁剪  （左，上，右，下）
region105 = im105.crop((left[6], top[6], right[6], bottom[6]))  #裁剪  （左，上，右，下）
region106 = im106.crop((left[7], top[7], right[7], bottom[7]))  #裁剪  （左，上，右，下）
region107 = im107.crop((left[8], top[8], right[8], bottom[8]))  #裁剪  （左，上，右，下）
region108 = im108.crop((left[9], top[9], right[9], bottom[9]))  #裁剪  （左，上，右，下）
region109 = im109.crop((left[10], top[10], right[10], bottom[10]))  #裁剪  （左，上，右，下）

font = {'family': 'Arial'}

#下面是新建一个多图
plt.figure(num = 'diffraction dots', figsize = (10,16))

images = (region100, region002, region101, region102, region103, region104, region105, region106, region107, region108, region109)
title = ('1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th', '11th')

i = 0
while i < N:

    plt.subplot(4, 3, i+1)
    plt.title(title[i])
    tif_No = int(tif_Mid - 2 + i)
    plt.imshow(images[i], extent = [left[i], right[i], bottom[i], top[i]], cmap=plt.cm.gray, vmin=0, vmax=256)
    if i == 5:
        circle1=plt.Circle((1074.1232,999.26874), math.sqrt((float(positions[i, 0]) - 1074.1232) ** 2 + (float(positions[i, 1]) - 999.26874) ** 2), color='r', fill = False)  #circle   
        plt.gcf().gca().add_artist(circle1)
        plt.plot([1074.1232, float(positions[i, 0])], [999.26874, float(positions[i, 1])], '--')  #radius
#    
#    plt.text(left[i] + 39.5, top[i] + 3, 'hkil=', ha='right', fontsize = 9, fontname = 'Arial')   #hkil = 
#    plt.text(left[i] + 42, top[i] + 3, str(int(hkil[i, 0])), ha='right', fontsize = 9, fontname = 'Arial')
#    plt.text(left[i] + 44.5, top[i] + 3, str(int(hkil[i, 1])), ha='right', fontsize = 9, fontname = 'Arial')
#    plt.text(left[i] + 47, top[i] + 3, str(int(hkil[i, 2])), ha='right', fontsize = 9, fontname = 'Arial')
#    plt.text(left[i] + 49.5, top[i] + 3, str(int(hkil[i, 3])), ha='right', fontsize = 9, fontname = 'Arial')
#
#    plt.text(left[i] + 39.5, top[i] + 6, 'tif_No=', ha='right', fontsize = 9, fontname = 'Arial')   #tif =
#    plt.text(left[i] + 40, top[i] + 6, str(tif_No), ha = 'left', fontsize = 9, fontname = 'Arial')
#    
    plt.text(left[i] + 41.5, top[i] + 2.5, 'Omega=', ha='right', fontsize = 9, fontname = 'Arial')   #Rotation angle =
    plt.text(left[i] + 42, top[i] + 2.5, str(round((tif_No-1)/4, 2) - 70.5), ha = 'left', fontsize = 9, fontname = 'Arial')
    
#    plt.xticks(np.arange(left[i], right[i], 10), fontsize = 10, fontname = 'Arial')
    plt.axis([left[i], right[i],  bottom[i], top[i]])
#    plt.yticks(np.arange(top[i], bottom[i], 10), fontsize = 10, fontname = 'Arial')
#    plt.grid(True)       #网格
    
    plt.xticks([])
    plt.yticks([])
    i += 1


#plt.savefig('Diffraction_spots(one spot)_of_grain_' + str(grain_No) + '(Mg_30deg_step' + str(step) + '_file' + str(file) + '_' + str(int(hkil[0, 0])) + str(int(hkil[0, 1])) + str(int(hkil[0, 2])) + str(int(hkil[0, 3])) + '.png', dpi = 200, bbox_inches = 'tight')

plt.show()
print('=====================')



