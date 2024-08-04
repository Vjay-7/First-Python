# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 08:47:35 2022

@author: Admin
"""

start= int(input("Start: "))
end = int(input("End: "))

for i in range(start,end+1):
    if i>1:
        for x in range(2, i):
            if (i % x) == 0:
                break
        else:
            print(i)
    