#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 10:13:24 2019

@author: krishna
"""

# Python program to demonstrate
# binary operators in Numpy
import numpy as np

a = np.array([[1, 2],
 [3, 4]])
b = np.array([[4, 3],
 [2, 1]])

# add arrays
print ("Array sum:\n", a + b)

# multiply arrays (elementwise multiplication)
print ("Array multiplication:\n", a*b)

# matrix multiplication
print ("Matrix multiplication:\n", a.dot(b))  