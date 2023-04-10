# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 18:43:35 2022

@author: Admin
"""

n = int(input("Enter the number :- "))

def test_prime(n):
    if (n==1):
        return False
    elif (n==2):
        return True;
    else:
        for x in range(2,n):
            if(n % x==0):
                return False
        return True             
print(test_prime(n))