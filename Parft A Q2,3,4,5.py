# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 16:29:41 2022

@author: Admin
"""

import numpy as np
list = [23,27,25,45,67]
vtr = np.array(list)

dp = np.rec.fromarrays(list, dtype= {'names': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'],
                                   'formats':['f8','f8', 'f8', 'f8', 'f8']})

avg = np.average(vtr)

hv = list[0]
for number in list:
    if number > hv:
        hv = number



#print("Vector :- " ,vtr)
#print(dp)
#print(avg)
#print(hv)
