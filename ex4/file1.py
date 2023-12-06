# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 13:25:42 2023

@author: Dell
"""


from classCat import cat
from ObjectClass import pickObject
import numpy as np



Luna = cat("Luna", "snail")
Ariana = cat("Ariana", "rock")
Dante = cat("Dante", "mouse")

cats = [Luna.name, Ariana.name, Dante.name]

def map_generator(map_size, house_size):
    arr = np.array([["X" for x in range(map_size)] for x in range(map_size)])
    center_x, center_y = (len(arr[0]) // 2, len(arr[0]) // 2)
    left_top_x = center_x - (house_size // 2)
    left_top_y = center_y - (house_size // 2)
    arr[left_top_y:left_top_y + house_size, left_top_x:left_top_x + house_size] = 'H'
    return arr

arr = map_generator(50, 10)



# def hunting(cats, objects, time, arr):
#     for cat in cats:
#         time = 2
#         while time > 0 and objects > 0:
