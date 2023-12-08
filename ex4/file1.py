# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 13:25:42 2023

@author: Dell
"""


from classCat import cat
from ObjectClass import pickObject
import numpy as np

def spawnObjectMap(arr, objects):
    for obj in objects:
        
        x, y = np.random.randint(0, arr.shape[0]), np.random.randint(0, arr.shape[1])
        
        arr[x, y] = obj.objectName
        
arr = np.array([[ "X" for x in range(50)] for x in range(50)])

Luna = cat("Luna", "snail")
Ariana = cat("Ariana", "rock")
Dante = cat("Dante", "mouse")

print(Luna)
print(Ariana)
print(Dante)

arr[int(len(arr)/2), int(len(arr[0])/2)] = "Luna"
