# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 15:31:23 2022

@author: Eleanor Glyn-Smith
"""

import math
import numpy as np


# num = 600851475143

def largest_prime_factor(num):
    factors=[]
    while num%2 == 0:
        num = num/2
        factors.append(2)
    for x in range(3,(math.ceil(np.sqrt(num)))+1):
        if num%x == 0:
            factors.append(x)
            num = num/x
        else:
            x=x+2
    if factors == []:
        return num
    else:
        return max(factors)
