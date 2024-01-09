# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 13:25:42 2023
@author: Dell
"""


from catClass import cat
from mapGeneratorFunction import map_generator
from mapGeneratorFunction import Hunting
import numpy as np



Luna = cat("Luna", "snail")
Ariana = cat("Ariana", "rock")
Dante = cat("Dante", "mouse")

cats = [Luna.name, Ariana.name, Dante.name]
objects = {"rock":200,"snail":90, "mouse":80, "leaf":300, "fildmouse":150}


arr = map_generator(50, objects)
visited_paths = []

for cat_name in cats:
    cat_instance = next(cat for cat in [Luna, Ariana, Dante] if cat.name == cat_name)
    Hunting(cat_instance.name, cat_instance.best_object, arr, objects[cat_instance.best_object], visited_paths)


    
            