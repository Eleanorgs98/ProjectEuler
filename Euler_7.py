# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 16:30:54 2022

@author: Eleanor Glyn-Smith
"""                
def is_prime(n):
    '''
    Determines if the given number is prime using the 6K +- 1 algorithm
    Args:
        n: The integer to evaulate primality on
    Returns:
        A Boolean indicating Primality
    '''
    if n<=3:
        return n>1
    if (n%2 == 0) or (n%3 == 0):
        return False
    i = 5
    count = 1
    while i <= n**0.5:
        if (n%i == 0) or (n%(i+2) == 0):
            return False
        i = i+6
        count = count+1
    return True

def next_prime(start):
    '''
    A generator providing the next prime after (and including) the given start point
    Args:
        The integer to first evaluate primality on
    Yields:
        The next prime number
    
    '''
    num = start
    while True:
        if is_prime(num):
            temp = num
            num = num+1
            yield(temp)
        
        else:
            num = num+1
            

t = next_prime(1)
for i in range(10002):
    if i == 10000: #Stopping at 10000 so the next calculated value is the desired prime
        print(next(t))
    else:
        next(t)
    

    
