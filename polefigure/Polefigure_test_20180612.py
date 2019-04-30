# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 11:58:45 2018

@author: 朱高明
"""

import pandas as pd
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Circle

#aaa = 'qtrdeg_6_file8_t100'
aaa = 'tracked_t100_(radius120)_nosame_cut6in11_onlyfile0_20190430'

def in_excel(file_path):   #define a function to import excel file
    x = pd.read_excel(file_path)
    xM = x.ix[:, 'GrainNo' : 'Intensity']
    xMatrix = np.matrix(xM)
    return(xMatrix)

def rot(E01, E02, E03):
    Euler01 = float(E01) - 90
    Euler02 = float(E02)
    Euler03 = 90 - float(E03)
    Euler01rad = Euler01 * math.pi / 180
    Euler02rad = Euler02 * math.pi / 180
    Euler03rad = Euler03 * math.pi / 180
    
    s1 = math.sin(Euler01rad)
    s2 = math.sin(Euler02rad)
    s3 = math.sin(Euler03rad)
    c1 = math.cos(Euler01rad)
    c2 = math.cos(Euler02rad)
    c3 = math.cos(Euler03rad)
    
    g11 = -s1*s3 - c1*c3*c2
    g21 = c1*s3 - s1*c3*c2
    g31 = c3*s2
    g12 = c3*s1 - s3*c1*c2
    g22 = -c1*c3 - s1*s3*c2
    g32 = s3*s2
    g13 = c1*s2
    g23 = s1*s2
    g33 = c2
    
    g = np.matrix([[g11, g12, g13],  [g21, g22, g23], [g31, g32, g33]])
#    gT = g.T
    return(g)

#EulerM = in_excel('G:\SynchrotronXray\DESY_June_2018\Analysis\Stress\Mg_30deg_qrtdeg_0_t200.xlsx')#EulerMatrix and others
EulerM = in_excel(r'E:\SynchrotronXray\DESY_June_2018\Analysis\Stress\Mg_30deg_qtrdeg_t100\tracking_results\\' + aaa+ '.xlsx')#EulerMatrix and others
                                                                                                                                                                                                                 
npoles = 2

xs = np.zeros((len(EulerM)))
ys = np.zeros((len(EulerM)))
ii = np.zeros((len(EulerM)))

i =0
while i < len(EulerM):
    cou = 0
    gM =  rot(EulerM[i, 16], EulerM[i, 17], EulerM[i, 18])
    r = np.eye((3))
    gM = r*gM
    j = 0
    while j < npoles:
        if j == 0:
            poless = [[0],[0],[1]]
        else:
            poless = [[0],[0],[-1]]
            
        polematrix = np.squeeze(gM*poless)
        polematrix2 = np.array(polematrix)
        pole = polematrix2[0]
#        print('-------')
#        print(pole)
        if pole[2] >= 0:
            x = pole[0]
            y = pole[1]
            z = pole[2]
            if z == 0:
                if x > 0:
                    EulerM[i, 17] = math.pi/2
                else:
                    EulerM[i, 17] = -math.pi/2
            else:
                phi_check = math.atan2(y, x)
                if x == 0 and y != 0:
                    theta_check = math.atan(y/z/math.sin(phi_check))
                else:
                    theta_check = math.atan(x/z/math.cos(phi_check))
#                print(theta_check, phi_check)
                theta_sphere = theta_check
                phi_sphere = phi_check
            xx = math.sqrt(2)*math.sin(theta_sphere/2.0)*math.cos(phi_sphere)
            yy = math.sqrt(2)*math.sin(theta_sphere/2.0)*math.sin(phi_sphere)
            cou += 1
        j += 1
    xs[i] = xx
    ys[i] = yy
    ii[i] = EulerM[i, 0]
    i += 1
#    print(i)
x = xs
y = ys

jj = range(len(EulerM))   #change jj to ii in line(cir1) and delete this line and change txt+1 to txt

fig = plt.figure()
ax = fig.add_subplot(111)
radius = 1
cir1 = Circle((0, 0), radius, clip_on=False, linewidth=0.8, edgecolor='green', facecolor=(0, 0, 0, 0))
ax.add_patch(cir1)
plt.axis('scaled')
plt.axis('equal') 
ax.scatter(x, y, marker='o', c='', edgecolors='b',  alpha = 0.8)#linewidth = 0.5, s = 30,
#for i, txt in enumerate(ii):
#    ax.annotate(int(txt), (x[i]+0.015, y[i]-0.015), fontsize = 12)
for i, txt in enumerate(jj):
    if i + 1 != ([34, 39])# and i + 1 != 39 and i + 1 != 57 and i + 1 != 61 and i + 1 != 87:#新加的，20190430
        ax.annotate(int(txt+1), (x[i]+0.015, y[i]-0.015), fontsize = 12)
    else:
        ax.annotate(int(txt+1), (x[i]+0.015, y[i]-0.015), fontsize = 12, color = 'red')
    

plt.xticks([])
plt.yticks([])
plt.axis('off')
plt.xlim((-1, 1))
plt.ylim((-1, 1))
plt.rc('figure', figsize=(10,10))
plt.title('Polefigure_' + aaa, fontsize = 18)
plt.savefig(r'E:\SynchrotronXray\DESY_June_2018\3D_XRD20180616\plot_pole_figure20180819\Polefigure_' + aaa + '.png',dpi = 300, bbox_inches = 'tight')

plt.show()



























