# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 18:12:39 2022

@author: Eleanor Glyn-Smith
"""
def fib(x0=0,x1=1):
    '''
    Creates an infinite generator for the fibonacci sequence
    '''
    while True:
        x0,x1 = x1,x0+x1
        yield x1
        

t = fib()
total = 0
num = next(t)
while num < (4*(10**6)): # Stops when the fibonacci numbers exceed 4 million
    if num%2 == 0: # Considers the even fibonacci numbers only 
        total = total + num
    num = next(t)

print(total)