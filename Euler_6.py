# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 14:54:25 2022

@author: Eleanor Glyn-Smith
"""
sum_squares=0
total=0

for x in range(1,101):
    sum_squares=sum_squares+x**2
    total=total+x
    
squared_sum=total**2

print(squared_sum-sum_squares)
