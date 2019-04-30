# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 18:30:45 2018

@author: 朱高明
"""

#http://tool.chinaz.com/tools/unicode.aspx   unicode编码

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from colorama import Fore
import math

font = {'family': 'Arial'}
grain_No = 58
step = str(0)
max_int = 50000

def inExcel1(file_path):
    data_file = pd.read_excel(file_path)
    Rawdata = data_file.ix[1:, :]
    RawdataMatrix = np.matrix(Rawdata)
    return(RawdataMatrix)

def inExcel2(file_path):
    data_file = pd.read_excel(file_path)
    Rawdata = data_file.ix[:, 'numbers':'l']
    RawdataMatrix = np.matrix(Rawdata)
    return(RawdataMatrix)

E0 = inExcel1(r'G:\SynchrotronXray\DESY_June_2018\TEST20180808\Mg_30deg_grain58\step' + step + r'\total.xlsx')
spots_info = inExcel2(r'G:\SynchrotronXray\DESY_June_2018\3D_XRD20180616\spots_information_0_file0\grain_No58_use.xlsx')
print(E0)
print(len(E0))

plt.figure(figsize = (30,35))

i = 0
while i < int(E0.shape[1]/2):
    hkil = str(int(spots_info[i, 9])) + str(int(spots_info[i, 10])) + str(int(spots_info[i, 11])) + str(int(spots_info[i, 12]))
    
    plt.subplots_adjust(hspace=0.4, wspace=0.25)
    plt.subplot(math.ceil(E0.shape[1]/2/8), 8, i + 1)
    plt.title('Number %s' %(i + 1), fontsize = 10)
    plt.plot(E0[:, 2 * i], E0[:, 2 * i + 1], 'o-')
    plt.xlabel('2Theta', fontsize = 10)
    plt.xticks(fontsize = 10, fontname = 'Arial')
    plt.axis([E0[0, 2 * i], E0[32, 2 * i], 0, max_int])
    plt.yticks(np.arange(0, max_int + 10000, 10000), fontsize = 10, fontname = 'Arial')

    plt.text(E0[0, 2 * i] + 0.207, 0.94 * max_int, 'hkil:' + '(' + hkil + ')', ha='right', fontsize = 10, fontname = 'Arial')
    plt.text(E0[0, 2 * i] + 0.207, 0.88 * max_int, u'\u03c9' + '_from:' + str(round(round(spots_info[i, 4]*4)/4 - 2, 2)) + u'\u00B0', ha='right', fontsize = 10, fontname = 'Arial')
    plt.text(E0[0, 2 * i] + 0.207, 0.82 * max_int, u'\u03c9' + '_to:' + str(round(round(spots_info[i, 4]*4)/4 + 2, 2)) + u'\u00B0', ha='right', fontsize = 10, fontname = 'Arial')

#    plt.text(E0[0, 2 * i] + 0.17, 0.95 * max_int, 'hkil=', ha='right', fontsize = 10, fontname = 'Arial')
#    plt.text(E0[0, 2 * i] + 0.17, 0.95 * max_int, '(' + hkil + ')', ha = 'left', fontsize = 10, fontname = 'Arial')

#    plt.text(E0[0, 2 * i] + 0.18, 28500, str(int(spots_info[i, 9])), ha='right', fontsize = 10, fontname = 'Arial')
#    plt.text(E0[0, 2 * i] + 0.19, 28500, str(int(spots_info[i, 10])), ha='right', fontsize = 10, fontname = 'Arial')
#    plt.text(E0[0, 2 * i] + 0.20, 28500, str(int(spots_info[i, 11])), ha='right', fontsize = 10, fontname = 'Arial')
#    plt.text(E0[0, 2 * i] + 0.21, 28500, str(int(spots_info[i, 12])), ha='right', fontsize = 10, fontname = 'Arial')

#    plt.text(E0[0, 2 * i] + 0.17, 27000, 'Omega_from:', ha='right', fontsize = 10, fontname = 'Arial')
#    plt.text(E0[0, 2 * i] + 0.17, 27000, str(round(round(spots_info[i, 4]*4)/4 - 2, 2)), ha = 'left', fontsize = 10, fontname = 'Arial')
#    plt.text(E0[0, 2 * i] + 0.17, 25500, 'Omega_to:', ha='right', fontsize = 10, fontname = 'Arial')
#    plt.text(E0[0, 2 * i] + 0.17, 25500, str(round(round(spots_info[i, 4]*4)/4 + 2, 2)), ha = 'left', fontsize = 10, fontname = 'Arial')

#    plt.text(E0[0, 2 * i] + 0.17, 27500, 'Omega_from:', ha='right', fontsize = 10, fontname = 'Arial')

    i += 1

plt.savefig('2Theta_Intensity_grain_' + str(grain_No) + 'step' + step + '.png', dpi = 200, bbox_inches = 'tight')






























































