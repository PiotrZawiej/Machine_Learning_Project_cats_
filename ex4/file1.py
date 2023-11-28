# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 13:25:42 2023

@author: Dell
"""


from classCat import cat
import numpy as np

arr = np.array([["X" for x in range(50)] for x in range(50)])
print(arr[49,49])

Luna = cat("Luna", "snail")

print(Luna.name, Luna.best_object)
