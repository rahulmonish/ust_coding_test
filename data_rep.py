# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 15:20:16 2018

@author: user
"""

import numpy as np
max=0
weight=np.array([11.95,11.91,11.86,11.94,12.00,11.93,12.00,11.94,12.10,11.95,11.99,11.94,11.89,12.01,11.99,11.94])
count=0
for i in range(len(weight)):
    #j=i+1
    for j in range(len(weight)):
        if weight[i]==weight[j]:
            count+=1
        
        if max<count:
            max=count
            max_i= i
    print(weight[i]," \t \t", count)
    count=0
mean= np.mean(weight)
weight.sort()
mode= weight[len(weight)/2]
median= np.median(weight)
print("mean is ",mean,"mode is " ,mode,"median is ", median)