# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 13:25:42 2023
@author: Dell
"""


from catClass import cat
import numpy as np



Luna = cat("Luna", "snail")
Ariana = cat("Ariana", "rock")
Dante = cat("Dante", "mouse")

cats = [Luna.name, Ariana.name, Dante.name]
objects = {"rock":5,"snail":5, "mouse":5}

def map_generator(map_size, house_size, objects):
    arr = np.array([["0" for _ in range(map_size)] for _ in range(map_size)])
    center_x, center_y = (len(arr[0]) // 2, len(arr[0]) // 2)
    left_top_x = center_x - (house_size // 2)
    left_top_y = center_y - (house_size // 2)
    arr[left_top_y:left_top_y + house_size, left_top_x:left_top_x + house_size] = 'H'
    
    for item, quantity in objects.items():
        for _ in range(quantity):
            rand_x, rand_y = np.random.randint(map_size), np.random.randint(map_size)
            
            if arr[rand_x, rand_y] == "H":
                while arr[rand_x, rand_y] == "H":
                    rand_x, rand_y = np.random.randint(map_size), np.random.randint(map_size)
            
            arr[rand_x, rand_y] = item
            
    return arr

arr = map_generator(50, 10, objects)



# def hunting(cats, objects, time, arr):
#     for cat in cats:
#         time = 2
#         while time > 0 and objects > 0: