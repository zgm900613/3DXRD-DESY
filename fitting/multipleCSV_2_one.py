# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 14:01:43 2018

@author: 朱高明
"""

import pandas as pd
import numpy as np
import xlsxwriter
import os
import math

#step = 'step3'
#------------------------- --------------------------------------------------
def inCSV(file_path):
    data_file = pd.read_csv(file_path, skiprows =4, sep = '\s+|,',  header = None)
    Rawdata = data_file.ix[:, 0:3]
    RawdataMatrix = np.matrix(Rawdata)
    return(RawdataMatrix)

def inExcel(file_path):
    data_file = pd.read_excel(file_path)
    Rawdata = data_file.ix[:, 'numbers':'l']
    RawdataMatrix = np.matrix(Rawdata)
    return(RawdataMatrix)

#-----------------------------------------------------------------------------
file_names = os.listdir(r'G:\SynchrotronXray\DESY_June_2018\TEST20180808\Mg_30deg_grain58\step6\Fit2Dfile')
file_dir = 'G:/SynchrotronXray/DESY_June_2018/TEST20180808/Mg_30deg_grain58/step6/'
spots_info = inExcel(r'G:\SynchrotronXray\DESY_June_2018\3D_XRD20180616\spots_information_0_file0\grain_No58_use.xlsx')

#number1 = [0.0] * len(file_names)
number1 = np.zeros(len(file_names))

i = 0    ##split filename No.
while i < len(file_names):
    number1[i] = file_names[i].split('.')[1].split('No')[1]
    i += 1

csv_list = []   ##import all excel files
i = 0
while i < len(file_names):
    file_path = file_dir + 'Fit2Dfile/' + file_names[i]
    CSV_data = inCSV(file_path)
    csv_list.append(CSV_data)
    i += 1
#----------------------------------one excel file-----------------------------
#-----------------------------------------------------------------------------
    
workbook = xlsxwriter.Workbook(file_dir + 'xrd_profiles_step6' + '.xlsx')
worksheet = workbook.add_worksheet()
i = 0
while i < max(number1):  #number of spots
    csv_total = np.zeros((2048, 2))
    j = 0
    while j < len(file_names):  #number of Excel files
        if number1[j] == i + 1:
            k = 0
            while k < 2048:  #len of csv_file
                csv_total[k, 0] = csv_list[j][k, 0]
                csv_total[k, 1] += csv_list[j][k, 1]
                k += 1
        j += 1
    
    m = 0
    while m < 33:
        cut_center = math.ceil(spots_info[i, 7] * 2.048)  #radius
        worksheet.write(m + 1, 2 * i, csv_total[m - 1 + cut_center, 0])
        worksheet.write(m + 1, 2 * i + 1, csv_total[m - 1 + cut_center, 1])
        m += 1
    hkil = str(int(spots_info[i, 9])) + str(int(spots_info[i, 10])) + str(int(spots_info[i, 11])) + str(int(spots_info[i, 12]))
#    worksheet.write(0, 2 * i, '(' + hkil + ')')
    worksheet.write(0, 2 * i, '(' + hkil + ')' + '2Theta')
    worksheet.write(0, 2 * i + 1, 'Intensity')
    
    i += 1
    print(i)
workbook.close()

#---------------------------------multiple Excel files------------------------  
#-----------------------------------------------------------------------------

#i = 0
#while i < max(number1):  #number of spots
#    hkil = str(int(spots_info[i, 9])) + str(int(spots_info[i, 10])) + str(int(spots_info[i, 11])) + str(int(spots_info[i, 12]))
#    workbook = xlsxwriter.Workbook(file_dir + 'Intensity_total_No' + str(i + 1) + '(' + hkil + ')' + '.xlsx')
#    worksheet = workbook.add_worksheet()
#    csv_total = np.zeros((2048, 2))
#    j = 0
#    while j < len(file_names):  #number of Excel files
#        if number1[j] == i + 1:
#            k = 0
#            while k < 2048:  #len of csv_file
#                csv_total[k, 0] = csv_list[j][k, 0]
#                csv_total[k, 1] += csv_list[j][k, 1]
#                k += 1
#        j += 1
#    
#    m = 0
#    while m < 33:
#        cut_center = math.ceil(spots_info[i, 7] * 2.048)  #radius
#        worksheet.write(m + 2, 0, csv_total[m - 1 + cut_center, 0])
#        worksheet.write(m + 2, 1, csv_total[m - 1 + cut_center, 1])
#        m += 1
#    worksheet.write(0, 0, '(' + hkil + ')')
#    worksheet.write(1, 0, '2Theta')
#    worksheet.write(1, 1, 'Intensity')
#    workbook.close()
#    
#    i += 1
#    print(i)
#-----------------------------------------------------------------------------






