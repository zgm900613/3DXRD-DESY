# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 12:24:37 2018

@author: 朱高明
"""
import pandas as pd
import numpy as np
import math
import os
from tqdm import tqdm

def in_excel(file_path):   #define a function to import excel file
    x = pd.read_excel(file_path)
    xM = x.ix[:, 'GrainNo' : 'file_No']
    xMatrix = np.matrix(xM)
    return(xMatrix)

def rot(E01, E02, E03, E11, E12, E13):
    E01 = float(E01)
    E11 = float(E11)
    if float(E02) < 180:
        E03 = (float(E03) + 90) % 60
    else:
        E03 = 60 - (float(E03) + 90) % 60
    
    if float(E12) < 180:
        E13 = (float(E13) + 90) % 60
    else:
        E13 = 60 - (float(E13) + 90) % 60
        
    E02 = float(E02) % 180
    E12 = float(E12) % 180

    Euler01rad = E01 * math.pi / 180
    Euler02rad = E02 * math.pi / 180
    Euler03rad = E03 * math.pi / 180
    Euler11rad = E11 * math.pi / 180
    Euler12rad = E12 * math.pi / 180
    Euler13rad = E13 * math.pi / 180
    
    Euler0 = np.zeros((12, 3))
    Euler1 = np.zeros((12, 3))
    AngleM = np.zeros((12, 12))
    
    gATM = np.matrix([[0.0, 0.0, 0.0],  [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]])
    
    i = 0
    while i < len(Euler0):
        if i < 6:
            Euler0[i, 0] = Euler01rad
            Euler0[i, 1] = Euler02rad
            Euler0[i, 2] = Euler03rad + i * 60 * math.pi / 180
            Euler1[i, 0] = Euler11rad
            Euler1[i, 1] = Euler12rad
            Euler1[i, 2] = Euler13rad + i * 60 * math.pi / 180
        else:
            Euler0[i, 0] = Euler01rad + 180 * math.pi / 180
            Euler0[i, 1] = 180 * math.pi / 180 - Euler02rad
            Euler0[i, 2] = -Euler03rad + (i - 6) * 60 * math.pi / 180
            Euler1[i, 0] = Euler11rad + 180 * math.pi / 180
            Euler1[i, 1] = 180 * math.pi / 180 - Euler12rad
            Euler1[i, 2] = -Euler13rad + (i - 6) * 60 * math.pi / 180
        i += 1
    
    i = 0
    while i < len(Euler0):
        gATM[0, 0] = math.cos(Euler0[i, 0]) * math.cos(Euler0[i, 2]) - math.sin(Euler0[i, 0]) * math.sin(Euler0[i, 2]) * math.cos(Euler0[i, 1])
        gATM[0, 1] = -math.cos(Euler0[i, 0]) * math.sin(Euler0[i, 2]) - math.sin(Euler0[i, 0]) * math.cos(Euler0[i, 2]) * math.cos(Euler0[i, 1])
        gATM[0, 2] = math.sin(Euler0[i, 0]) * math.sin(Euler0[i, 1])
        gATM[1, 0] = math.sin(Euler0[i, 0]) * math.cos(Euler0[i, 2]) + math.cos(Euler0[i, 0]) * math.sin(Euler0[i, 2]) * math.cos(Euler0[i, 1])
        gATM[1, 1] = - math.sin(Euler0[i, 0]) * math.sin(Euler0[i, 2]) + math.cos(Euler0[i, 0]) * math.cos(Euler0[i, 2]) * math.cos(Euler0[i, 1])
        gATM[1, 2] = - math.cos(Euler0[i, 0]) * math.sin(Euler0[i, 1])
        gATM[2, 0] = math.sin(Euler0[i, 2]) * math.sin(Euler0[i, 1])
        gATM[2, 1] = math.cos(Euler0[i, 2]) * math.sin(Euler0[i, 1])
        gATM[2, 2] = math.cos(Euler0[i, 1])
        
        gBTM = np.matrix([[0.0, 0.0, 0.0],  [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]])    

        j = 0
        while j < len(Euler0):
            gBTM[0, 0] = math.cos(Euler1[j, 0]) * math.cos(Euler1[j, 2]) - math.sin(Euler1[j, 0]) * math.sin(Euler1[j, 2]) * math.cos(Euler1[j, 1])
            gBTM[0, 1] = -math.cos(Euler1[j, 0]) * math.sin(Euler1[j, 2]) - math.sin(Euler1[j, 0]) * math.cos(Euler1[j, 2]) * math.cos(Euler1[j, 1])
            gBTM[0, 2] = math.sin(Euler1[j, 0]) * math.sin(Euler1[j, 1])
            gBTM[1, 0] = math.sin(Euler1[j, 0]) * math.cos(Euler1[j, 2]) + math.cos(Euler1[j, 0]) * math.sin(Euler1[j, 2]) * math.cos(Euler1[j, 1])
            gBTM[1, 1] = - math.sin(Euler1[j, 0]) * math.sin(Euler1[j, 2]) + math.cos(Euler1[j, 0]) * math.cos(Euler1[j, 2]) * math.cos(Euler1[j, 1])
            gBTM[1, 2] = - math.cos(Euler1[j, 0]) * math.sin(Euler1[j, 1])
            gBTM[2, 0] = math.sin(Euler1[j, 2]) * math.sin(Euler1[j, 1])
            gBTM[2, 1] = math.cos(Euler1[j, 2]) * math.sin(Euler1[j, 1])
            gBTM[2, 2] = math.cos(Euler1[j, 1])
        
#        gATM = np.matrix([[gAT11, gAT12, gAT13],  [gAT21, gAT22, gAT23], [gAT31, gAT32, gAT33]])
#        gBTM = np.matrix([[gBT11, gBT12, gBT13],  [gBT21, gBT22, gBT23], [gBT31, gBT32, gBT33]])
            gB = gBTM.T
            
            gAB11 = float(gB[0,:] * gATM[:,0])
            gAB12 = float(gB[0,:] * gATM[:,1])
            gAB13 = float(gB[0,:] * gATM[:,2])
            gAB21 = float(gB[1,:] * gATM[:,0])
            gAB22 = float(gB[1,:] * gATM[:,1])
            gAB23 = float(gB[1,:] * gATM[:,2])
            gAB31 = float(gB[2,:] * gATM[:,0])
            gAB32 = float(gB[2,:] * gATM[:,1])
            gAB33 = float(gB[2,:] * gATM[:,2])
            
#        gAB = np.matrix([[gAB11, gAB12, gAB13], [gAB21, gAB22, gAB23], [gAB31, gAB32, gAB33]])
            if gAB11 <= -1 and gAB11 >= -1.001:
                gAB11 = -1
            if gAB22 <= -1 and gAB22 >= -1.001:
                gAB22 = -1
            if gAB33 <= -1 and gAB33 >= -1.001:
                gAB33 = -1
            if gAB11 >= 1 and gAB11 <= 1.001:
                gAB11 = 1
            if gAB22 >= 1 and gAB22 <= 1.001:
                gAB22 = 1
            if gAB33 >= 1 and gAB33 <= 1.001:
                gAB33 = 1
            yyy = (gAB11 + gAB22 + gAB33 -1) * 0.5
            if yyy >= 1 and yyy < 1.001:
                yyy = 1
            if yyy <= -1 and yyy > -1.001:
                yyy= -1
            AngleRad = math.acos(yyy)
            AngleM[i, j] = AngleRad * 180 / math.pi
            
            j += 1
    
        if i == 0:  #to calculate c_axis Mis
            gAT = gATM
            gBT = gBTM #np.matrix([[gBT11, gBT12, gBT13],  [gBT21, gBT22, gBT23], [gBT31, gBT32, gBT33]])
        i += 1
    
    #--------calculate c-axis Misorientation (C_angle)
    uB1 = 0  
    vB1 = 0
    tB1 = 0
    wB1 = 1
    
    m1B1 = 1.5 * uB1
    m2B1 = np.sqrt(3)/2 *(2 * vB1 + uB1)
    m3B1 = wB1 * 1.62
    m4B1 = np.sqrt(m1B1 * m1B1 + m2B1 * m2B1 + m3B1 * m3B1)
    
    m1norB1 = m1B1/m4B1
    m2norB1 = m2B1/m4B1
    m3norB1 = m3B1/m4B1
    # burgers vectors
    Burg01 = gAT[0, 0] * m1norB1 + gAT[0, 1] * m2norB1 + gAT[0, 2] * m3norB1
    Burg02 = gAT[1, 0] * m1norB1 + gAT[1, 1] * m2norB1 + gAT[1, 2] * m3norB1
    Burg03 = gAT[2, 0] * m1norB1 + gAT[2, 1] * m2norB1 + gAT[2, 2] * m3norB1
    
    Burg11 = gBT[0, 0] * m1norB1 + gBT[0, 1] * m2norB1 + gBT[0, 2] * m3norB1
    Burg12 = gBT[1, 0] * m1norB1 + gBT[1, 1] * m2norB1 + gBT[1, 2] * m3norB1
    Burg13 = gBT[2, 0] * m1norB1 + gBT[2, 1] * m2norB1 + gBT[2, 2] * m3norB1
    
    dot_BurgAB = Burg01 * Burg11 + Burg02 * Burg12 + Burg03 * Burg13
    abs_BurgAB = math.sqrt(Burg01 ** 2 + Burg02 ** 2 + Burg03 ** 2) * math.sqrt(Burg11 ** 2 + Burg12 ** 2 + Burg13 ** 2)
    xxx = dot_BurgAB/abs_BurgAB
    if xxx >= 1 and xxx < 1.0001:
        xxx = 1
    if xxx <= -1 and xxx > 1.0001:
        xxx = -1
    
    c_AngleRad = math.acos(xxx)
    c_Angle = c_AngleRad * 180 / math.pi
    if c_Angle > 90:
        c_Angle = 180 - c_Angle
    
    Min_Angle = float(min(min(AngleM[0, :]), min(AngleM[1, :]), min(AngleM[2, :]), min(AngleM[3, :]), min(AngleM[4, :]), min(AngleM[5, :]), min(AngleM[6, :]), min(AngleM[7, :]), min(AngleM[8, :]), min(AngleM[9, :]), min(AngleM[10, :]), min(AngleM[11, :])))
#    if Min_Angle > 90:
#        Min_Angle = 180 - Min_Angle
    return(Min_Angle, c_Angle)
#---------------------------------------------------------------------------------------------------------------
bbb=rot(33, 112, 132, 33, 113, -47)
print(bbb)
ccc = rot(53, 320, 204, 53, 141, -24)
print(ccc)
ddd = rot(51.2, 220.5, -30.9, 51.6, 40.5, 91)
print(ddd)
eee = rot(-75.7, 109, 231.9, -75, 289, 8.1)
print(eee)
fff = rot(0, 0, 1, 0, 0, 59)
print(fff)

#---------------------------------------------------------------------------------------------------------------
def rotU(UA11, UA12, UA13, UA21, UA22, UA23, UA31, UA32, UA33, UB11, UB12, UB13, UB21, UB22, UB23, UB31, UB32, UB33):
    gA = np.matrix([[UA11, UA12, UA13], [UA21, UA22, UA23], [UA31, UA32, UA33]])
    gB = np.matrix([[UB11, UB12, UB13], [UB21, UB22, UB23], [UB31, UB32, UB33]])
    gAT = gA.T
#    print(gA)
#    print(gAT)
    gAB11 = float(gB[0,:] * gAT[:,0])
    gAB12 = float(gB[0,:] * gAT[:,1])
    gAB13 = float(gB[0,:] * gAT[:,2])
    gAB21 = float(gB[1,:] * gAT[:,0])
    gAB22 = float(gB[1,:] * gAT[:,1])
    gAB23 = float(gB[1,:] * gAT[:,2])
    gAB31 = float(gB[2,:] * gAT[:,0])
    gAB32 = float(gB[2,:] * gAT[:,1])
    gAB33 = float(gB[2,:] * gAT[:,2])
    
    gAB = np.matrix([[gAB11, gAB12, gAB13], [gAB21, gAB22, gAB23], [gAB31, gAB32, gAB33]])
#    print(gAB)
#    DelgAB = math.sqrt(((gAB23 - gAB32) * (gAB23-gAB32)) + ((gAB31 - gAB13) * (gAB31 - gAB13)) + ((gAB12 - gAB21) * (gAB12-gAB21)))
        
#    n1 = (gAB23 - gAB32) / DelgAB
#    n2 = (gAB31 - gAB13) / DelgAB
#    n3 = (gAB12 - gAB21) / DelgAB
    print('-------------------------------')
    print((gAB11 + gAB22 + gAB33 -1) * 0.5)
    AngleRad = math.acos((gAB11 + gAB22 + gAB33 -1) * 0.5)
    Angle = AngleRad * 180 / math.pi
    return(Angle)
#---------------------------------------------------------------------------------------------------------------


#---------------------------------------------------------------------------------------------------------------
def tracking3(file1, file2, line, file_No):
    radius = 120
    if file_No > 10:
        file_No2 = 10
    else:
        file_No2 = file_No
    dis_angle_max = 10
    dis_angle = 1 + (file_No2/10)*(dis_angle_max - 1)
    c_angle_max = 10
    c_angle = 1 + (file_No2/10)*(c_angle_max - 1)
    test = 0
    for i in range(len(file2)):
        if (abs(file1[line, 14] - file2[i, 14]) < radius) and (abs(file1[line, 15] - file2[i, 15]) < radius):
            dis, c_mis = rot(file1[line, 16], file1[line, 17], file1[line, 18], file2[i, 16], file2[i, 17], file2[i, 18])
            if dis < dis_angle and c_mis < c_angle:
                test = 1
                break
    return(test)
#---------------------------------------------------------------------------------------------------------------
def tracking4(file1, file2, line, file_No):
    radius = 120
    if file_No > 10:
        file_No2 = 10
    else:
        file_No2 = file_No
    dis_angle_max = 10
    dis_angle = 1 + (file_No2/10)*(dis_angle_max - 1)
    c_angle_max = 10
    c_angle = 1 + (file_No2/10)*(c_angle_max - 1)
    test = -1
    for i in range(len(file2)):
        if (abs(file1[line, 14] - file2[i, 14]) < radius) and (abs(file1[line, 15] - file2[i, 15]) < radius):
            dis, c_mis = rot(file1[line, 16], file1[line, 17], file1[line, 18], file2[i, 16], file2[i, 17], file2[i, 18])
            if dis < dis_angle and c_mis < c_angle:
                test = i
                c_angle = c_mis
                dis_angle = dis
    return(test)
      
#--------读取数据-------------------------------------------------------------------------------------------------------
file_names = os.listdir(r'E:\SynchrotronXray\DESY_June_2018\Analysis\Stress\Mg_30deg_qtrdeg_t100\combined\New_with_fileNo2019014')
file_names.sort(key = len)
a = 'E:/SynchrotronXray/DESY_June_2018/Analysis/Stress/Mg_30deg_qtrdeg_t100/'

print('-------------------------START--------------------------')
print('Import data')
data_list = []
for i in tqdm(range(len(file_names))):
    file_path = a + 'combined/New_with_fileNo2019014/' + file_names[i]
    data = in_excel(file_path)
    data_list.append(data)
#--------每个晶粒可以被追踪的步数-------------------------------------------------------------------------------------------------------
print('-------------------------------------------------------')
print('Tracking...3...' + str(len(data_list) - 4) + 'steps')
tracking_No = np.zeros((len(data_list[0]), 1))
for i in range(len(data_list) - 4):#改成1是对的
    print('step:' + str(i+1))
    for j in tqdm(range(len(data_list[0]))):
        tk3 = tracking3(data_list[0], data_list[i + 1], j, i)
        tracking_No[j]+= tk3
#        print('Tracking...3...' + 'file:' + str(i) + '___grain:' + str(j))
#--------共有多少晶粒可以被追踪-------------------------------------------------------------------------------------------------------
cut = 6   #改这里
tracked_grs = 0
for i in range(len(tracking_No)):
    if tracking_No[i] >= cut:
        tracked_grs += 1
#---------------------------------------------------------------------------------------------------------------
result_list = []
for i in range(len(file_names)):
    result = np.zeros((tracked_grs, 42)) - 1
    result_list.append(result)
#-------第一步结果留着--------------------------------------------------------------------------------------------------------
j = 0
for i in range(len(data_list[0])):
    if tracking_No[i] >= cut:
        for k in range(42):
            result_list[0][j, k] = data_list[0][i, k]
        j += 1
#--------主程序-------------------------------------------------------------------------------------------------------
print('-------------------------------------------------------')
print('Tracking...4...' + str(len(data_list) - 1) + 'steps')
for i in range(len(data_list) - 1):
    print('step:' + str(i+1))
    for j in tqdm(range(len(result_list[0]))):
        tk4 = tracking4(result_list[0], data_list[i + 1], j, i)
        if tk4 != -1:
            for k in range(42):
                result_list[i + 1][j, k] = data_list[i + 1][tk4, k]
#        print('Tracking...4...' + 'file:' + str(i) + '___grain:' + str(j))
#--------保存-------------------------------------------------------------------------------------------------------
print('-------------------------------------------------------')
print('Output')
tracked_excel = []
for i in range(len(file_names)):
    tk_excel = pd.DataFrame(result_list[i])
    tracked_excel.append(tk_excel)

sheets = ['step0', 'step1', 'step2', 'step3', 'step4', 'step5', 'step6', 'step7', 
          'step8', 'step9', 'step10', 'step11', 'step12', 'step13']

writer =  pd.ExcelWriter(a + 'tracking_results/tracked_t100_(radius120)_nosame_cut6in11_onlyfile0_20190414.xlsx')

for i in range(len(file_names)):
    tracked_excel[i].to_excel(writer, sheet_name = sheets[i])

writer.save()
#--------保存另一种格式-------------------------------------------------------------------------------------------------------

tracked_excel_by_grain = []
for i in range(len(result_list[0])):
    excel_grainX = np.zeros((14, 42))
    for j in range(14):
        for k in range(42):
            excel_grainX[j, k] = result_list[j][i, k]
    tkg_excel = pd.DataFrame(excel_grainX)
    tracked_excel_by_grain.append(tkg_excel)
    
writer =  pd.ExcelWriter(a + 'tracking_results/tracked_t100_(radius120)_nosame_cut6in11_onlyfile0_byGrain_20190414.xlsx')

for i in range(len(result_list[0])):
    tracked_excel_by_grain[i].to_excel(writer, sheet_name = 'grain' + str(i+1))
writer.save()
print('--------------------------End---------------------------')

