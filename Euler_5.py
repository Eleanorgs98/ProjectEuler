# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 14:33:02 2022

@author: Eleanor Glyn-Smith
"""
import numpy as np

def prime_factors(num):
    '''
    Generates a list of the prime factors of a number.
    '''
    factors=[]
    original=num
    while num%2 == 0:
        num = num/2
        factors.append(2)
    for x in range(3,int((original/2))+1):
        while num%x == 0:
            factors.append(x)
            num = num/x
        x=x+2
    if factors == []:
        factors.append(original)
    return factors

prime_decomp = []
for x in range(2,21,1): # find prime factors of given range
    prime_decomp.append(prime_factors(x))

primes=[]
for i in range(len(prime_decomp)): # Extracts the prime numbers from all the factors
    if len(prime_decomp[i])==1:
        primes.append(prime_decomp[i][0])
        
counter=np.zeros((len(primes),len(prime_decomp))) # create 2d array to store the number of occurences of each prime factor
for j in range(len(primes)):
    for k in range(len(prime_decomp)):
        counter[j,k]=(prime_decomp[k].count(primes[j]))         
    
indices=[]
solution=1
for p in range(len(primes)): 
    indices.append(max(counter[p])) # find the maximum number of occurences of each prime number in any of the prime factor decompositions
    solution=solution*(primes[p]**indices[p]) # the solution is the product of each prime factor to the power of the maximum occurence of the given factor
print(solution)
    