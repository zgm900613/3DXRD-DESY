# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 08:30:18 2018

@author: GM Zhu
"""

import numpy as np
import pandas as pd

#from numpy import *
#A = zeros((2,3), dtype=float)


#data_file0 = pd.read_log('MgCa_45deg_halfdeg_5_t200.log') #(1)the first file
#data_file1 = pd.read_excel('OutPut_Eulers.xlsx') #(2)the second file
#
#f = open('MgCa_45deg_halfdeg_5_t200.log','r')
#f = open('xxx.txt','r')
#s = f.read()
#print(s)
#lines = f.readlines()
#print(lines)
#print(lines)
#A_row = 0
#for line in lines:
#    list = line.strip('\n').split(' ')
#    A[A_row:] = list[0:2]
#    A_row += 1
#print(A)



#
#Rawdata0 = data_file0.ix[:,'1':'23']
#Rawdata1 = data_file1.ix[:,'Number':'q3']
#
#Rawdata0Matrix = np.matrix(Rawdata0)
#Rawdata1Matrix = np.matrix(Rawdata1)
##print(Rawdata0Matrix)
##print(Rawdata1Matrix)
#
#print(Rawdata0Matrix)


#i = 0
#j = 0
#a = 0
#
#while i < 300:
#    print(i)
#    if i == 0:

#
    
#def loadData(path):
#    f = open(path, 'r')
#    s = f.read()
#    print(s)
#loadData('xxx.txt')
#    data=list()
#    with  open(path,'r') as fileReader:
#        lines = fileReader.readlines()  # 读取全部内容
#        f = open (path,'r')
#        s = f.read
#        for line in lines:
#            line = line.strip()
#            line = line.split("\t")#根据数据间的分隔符切割行数据
#            data.append(line[:])
#
#    data=np.array(data)
#    data = data.astype(str)
#    np.random.shuffle(data)
#    label=data[:,0]
#    features=data[:,1:]
#    print("data loaded!")
#    return features,label-1
#loadData('MgCa_45deg_halfdeg_5_t200.log')

x =  pd.read_table('test20180606.txt', sep = '\s+')
print x