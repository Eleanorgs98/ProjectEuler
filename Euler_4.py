# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 15:58:42 2022

@author: Eleanor Glyn-Smith
"""



import time
start_time = time.time()
largest_pal = 0
for i in range(999,100,-1):
    for j in range(999,100,-1):
        num = i*j
        if (num > largest_pal) and (i>=j):
            num = str(num)   
            if num[0:3] == num[-1:-4:-1]:
                largest_pal = int(num)
print(largest_pal)
print("--- %s seconds ---" % (time.time() - start_time))


    

    

    
    