#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 10:24:35 2019

@author: krishna
"""

##simple python program to find the inverse of an array (without exception handling)
import numpy as np
arr = np.array([[-1, 2, 0, 4],
 [4, -0.5, 6, 0],
 [2.6, 0, 7, 8],
 [3, -7, 4, 2.0]])
inverse = np.linalg.inv(arr)
print(inverse)