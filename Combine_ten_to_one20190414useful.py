# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 14:02:51 2018

@author: 朱高明
"""

import pandas as pd
import numpy as np
import xlsxwriter

def inExcel(file_path):
    data_file = pd.read_excel(file_path)
    Rawdata = data_file.ix[:, 'GrainNo':'sc6']
    RawdataMatrix = np.matrix(Rawdata)
    return(RawdataMatrix)

step = 13

E_10files = []
for i in range(10):
    E0 = inExcel(r'E:\SynchrotronXray\DESY_June_2018\Analysis\Stress\Mg_30deg_qtrdeg_t100\Mg_30deg_qtrdeg_' + str(step) + '_file' + str(i) + '_t100.xlsx')
    E_file_No = np.zeros((len(E0), 1)) + i  #得到file号码
    E0 = np.append(E0, E_file_No, axis = 1) #左右合并E0和file号码
    E_10files.append(E0) #合并所有的10个文件

Excel = np.vstack((E_10files[0], E_10files[1], E_10files[2], E_10files[3], E_10files[4],  
                   E_10files[5], E_10files[6], E_10files[7], E_10files[8], E_10files[9])) #上下合并所有的

workbook = xlsxwriter.Workbook(r'E:\SynchrotronXray\DESY_June_2018\Analysis\Stress\Mg_30deg_qtrdeg_t100\combined\New_with_fileNo2019014\Mg_30deg_qtrdeg_' + str(step) + '_t100_comb.xlsx')
worksheet = workbook.add_worksheet()

i = 0
while i < len(Excel):
    j = 0
    while j < 42:
        worksheet.write(i+1, j, Excel[i, j])
        j += 1
    i += 1

title = ('GrainNo','StressE11', 'E22', 'E33', 'E12', 'E13','E23', 'vonMises', 'strain1', 'strain2', 'strain3','strain4', 'strain5', 'strain6', 'PositionX', 'PositionY', 'Euler1', 'Euler2', 'Euler3', 'U11', 'U12', 'U13', 'U21', 'U22', 'U23', 'U31', 'U32', 'U33', 'Intensity', 'twinshear1', 'twin2', 'twin3', 'twin4', 'twin5', 'twin6', 'stress_crystal1', 'sc2', 'sc3', 'sc4', 'sc5', 'sc6', 'file_No')
j = 0  #表头写入
while j < 42:
    worksheet.write(0, j, title[j])
    j += 1
print('OOOOOOOOOOOOOOOOOOKKKKKKKKKKKKKKKKKKKKKK')
workbook.close()