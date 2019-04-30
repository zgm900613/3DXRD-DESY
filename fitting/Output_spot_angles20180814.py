# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 01:53:42 2018

@author: 朱高明
"""

#the following code can be used to output spot positions, spot angles to the center, gvecters of the spots

import math
import numpy as np
import pandas as pd
import xlsxwriter



y_center = 999.64
x_center = 1073.9
#spot_No = 8
grain_No = 58

def inflt(file_path):  #define a function to import flt file
    x = pd.read_table(file_path, sep = '\s+|,', header = None)
    xM = x.ix[:, 0 : 30]
    xMatrix = np.matrix(xM)
    return(xMatrix)
    
def inlog(file_path):   #define a function to import log file
    x = pd.read_table(file_path, skiprows = 19, sep = '\s+|,', header = None)
    xM = x.ix[:, 0 : 5]
    xMatrix = np.matrix(xM)
    return(xMatrix)

logMatrix = inlog(r'G:\SynchrotronXray\DESY_June_2018\LOG\ten_times\Mg_30deg_qtrdeg_0_file0_t100.log')      
fltMatrix = inflt(r'G:\SynchrotronXray\DESY_June_2018\FLT\Mg_30deg_qtrdeg_0_t100.flt')      
file_dir = 'G:/SynchrotronXray/DESY_June_2018/3D_XRD20180616/spots_information_0_file0/'
#----------------------find peakids -----------

i = 0
while i < len(logMatrix):
    if str(logMatrix[i, 0]) == 'Grain':
        if int(logMatrix[i, 1]) == grain_No:
            peakids = np.zeros(int(logMatrix[i, 3]))
            numbers = np.zeros((int(logMatrix[i, 3]), 1))
            hkil = np.zeros((int(logMatrix[i, 3]), 4))
            j = 0
            while j < len(peakids):
                peakids[j] = int(logMatrix[i + 12 + j, 2])
                numbers[j, 0] = j + 1
                hkil[j, 0] = int(logMatrix[i + 12 + j, 3])
                hkil[j, 1] = int(logMatrix[i + 12 + j, 4])
                hkil[j, 2] = -(hkil[j, 0] + hkil[j, 1])
                hkil[j, 3] = int(logMatrix[i + 12 + j, 5])
                j += 1
    i += 1
print(peakids)
print(hkil)

#----------------------find diffraction spots positions and intensities-----------
i = 0
positions = np.zeros((len(peakids),8))
while i < len(peakids):
    j = 1
    while j < len(fltMatrix):
        if peakids[i] == int(fltMatrix[j, 29]):
#            positions = np.zeros((len(peakids),6))
            positions[i, 0] = peakids[i]    #peak id
            positions[i, 1] = float(fltMatrix[j, 0])     #sc(position_y)
            positions[i, 2] = float(fltMatrix[j, 1])     #fc(position_x) parallel
            positions[i, 3] = float(fltMatrix[j, 2])     #omega
            positions[i, 4] = round((70.5 + positions[i, 3]) * 4 + 1)    #integer, represent the tif file number
            if positions[i, 4] > 561:
                positions[i, 4] = 561
            if positions[i, 4] < 1:
                positions[i, 4] = 1
            positions[i, 5] = float(fltMatrix[j, 13])    #sum_intensity
            positions[i, 6] = math.sqrt((float(positions[i, 2]) - x_center) ** 2 + (float(positions[i, 1]) - y_center) ** 2)
            Arc_tan = math.atan(abs(float(positions[i, 1]) - y_center)/abs(float(positions[i, 2]) - x_center))
            Arc_tan_angle = Arc_tan * 180 / math.pi
            if (float(positions[i, 1]) - y_center) < 0 and (float(positions[i, 2]) - x_center) > 0:
                positions[i, 7] = Arc_tan_angle
            elif (float(positions[i, 1]) - y_center) < 0 and (float(positions[i, 2]) - x_center) < 0:
                positions[i, 7] = 180 - Arc_tan_angle
            elif (float(positions[i, 1]) - y_center) > 0 and (float(positions[i, 2]) - x_center) < 0:
                positions[i, 7] = 180 + Arc_tan_angle
            else:
                positions[i, 7] = 360 - Arc_tan_angle
        j += 1
    i += 1
print(positions)


All_data = np.hstack((numbers, positions, hkil))

#Len_spot2center = math.sqrt((float(positions[spot_No, 2]) - x_center) ** 2 + (float(positions[spot_No, 1]) - y_center) ** 2)


workbook = xlsxwriter.Workbook(file_dir + 'grain_No' + str(grain_No) + '.xlsx')
worksheet = workbook.add_worksheet()

titles = ('numbers', 'peakid', 'position_y(sc)', 'position_x(fc)', 'omega', 'tif_No', 'sum_intensity', 'radius', 'angle', 'h', 'k', 'i', 'l')

i = 0
while i < 83:
    j = 0
    while j < 13:
        worksheet.write(i + 2, j, All_data[i, j])
        if i == 0:
            worksheet.write(i + 1, j, titles[j])
        j += 1
    i += 1

worksheet.write(0, 0, 'grain_No'+ str(grain_No))

workbook.close()
