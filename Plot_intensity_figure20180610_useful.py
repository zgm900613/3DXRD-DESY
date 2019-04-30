# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 01:21:42 2018

@author: GM Zhu
"""

import pandas as pd
import matplotlib.pyplot as plt
#aaa = 'qtrdeg_6_file2_t100'
aaa = 'MgCa_0deg_halfdeg_0_t200'
#bbb = 100000
bbb = 30000
Raw = pd.read_excel(r'G:\SynchrotronXray\DESY_June_2018\Analysis\Stress\MgCa_0deg_halfdeg_t200\combined\\' + aaa+ '.xlsx')
x = Raw['PositionX']
y = Raw['PositionY']
Int = Raw['Intensity']
Int = Int/bbb
Num = Raw['GrainNo']
#print(x)
fig, ax = plt.subplots()
ax.scatter(x, y, s = Int, alpha = 0.5)
for i, txt in enumerate(Num):
    ax.annotate(txt, (x[i], y[i]), fontsize = 12)
plt.xlim((-600, 600))
plt.ylim((-600, 600))
plt.rc('figure', figsize=(10,10))
plt.xlabel(r'Position_X (μm)', fontsize = 15)
plt.ylabel(r'Position_Y (μm)', fontsize = 15)
plt.title('intensity_' + aaa, fontsize = 18)
plt.xticks(fontsize = 12)
plt.yticks(fontsize = 12)
ax.xaxis.set_ticks([-400, -200, 0, 200, 400])   #网格
plt.grid(True)       #网格
plt.savefig(r'G:\SynchrotronXray\DESY_June_2018\3D_XRD20180616\plot_Intensity20180819\intensity_' + aaa+ '.png',dpi = 300, bbox_inches = 'tight')
plt.show() 


