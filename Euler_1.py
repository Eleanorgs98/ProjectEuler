# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 15:00:05 2022

@author: Eleanor Glyn-Smith
"""
total = 0
for i in range(1000):
    if (i%3 == 0) or (i%5 == 0):
        total = total +i
        
print(total)

        