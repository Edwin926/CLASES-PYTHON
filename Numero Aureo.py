# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 11:01:09 2020

@author: CEC
"""

def fibo(n):
    a, b = 0,1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()
fibo(1000)