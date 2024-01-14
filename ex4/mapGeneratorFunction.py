# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 13:24:09 2023

@author: Dell
"""
import numpy as np
from queue import Queue


def map_generator(map_size, objects):

# Generating map
    arr = np.array([["0" for _ in range(map_size)] for _ in range(map_size)])
    center_x, center_y = (len(arr[0]) // 2, len(arr[0]) // 2)
    arr[center_x,center_y] = 'H'
    
# Insert objects in the map
    for item, quantity in objects.items():
        for _ in range(quantity):
            rand_x, rand_y = np.random.randint(map_size), np.random.randint(map_size)

            while arr[rand_x, rand_y] != "0":
                rand_x, rand_y = np.random.randint(map_size), np.random.randint(map_size)
            
            arr[rand_x, rand_y] = item
            
    return arr

def calculate_distance(point1, point2):
    return np.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

    
def Hunting(cat_name, fav_objects, arr, reamining_objects, visited_paths, objects_collected, time, cat_location, visited, q, center_x, center_y):
    # Set the initial position of the cat at the center of the map
    arr[center_x, center_y] = cat_name
    objects_score = 0
    path = []
    
    # Create a boolean array to track visited locations
    visited = np.zeros_like(arr, dtype=bool)
    visited[cat_location[0], cat_location[1]] = True

    # Create a queue for breadth-first search and add the initial location
    q = Queue()
    q.put(cat_location)

    # Search for the preferred objects using BFS
    while objects_score < reamining_objects and time > 0 and not q.empty():
        current_location = q.get()
        
        current_path = [current_location]

        # Iterate over neighbors (up, down, left, right)
        for neighbor in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_location = (current_location[0] + neighbor[0], current_location[1] + neighbor[1])

            # Check if the new location is within the map boundaries and has not been visited
            if 0 <= new_location[0] < len(arr) and 0 <= new_location[1] < len(arr[0]) and not visited[new_location[0], new_location[1]]:
                object_at_location = arr[new_location[0], new_location[1]]

                # If the cat's object is one of the preferred objects, mark it as found
                if object_at_location in fav_objects:
                    objects_collected += 1
                    objects_score += 1
                    
                    path.append(current_location);

                    # Move the cat to the new location
                    arr[current_location[0], current_location[1]] = "0"  # Remove the cat from the previous position
                    arr[new_location[0], new_location[1]] = cat_name  # Move the cat to the new position
                    time -= 100

                    # Update the current location of the cat
                    cat_location = [new_location[0], new_location[1]]

                    # Clear visited array and queue for the next search
                    visited = np.zeros_like(arr, dtype=bool)
                    visited[cat_location[0], cat_location[1]] = True
                    q = Queue()
                    q.put(cat_location)

                q.put(new_location)
                visited[new_location[0], new_location[1]] = True
                
                can_move = True
                for visited_path in visited_paths:
                    if new_location in visited_path:
                        can_move = False
                        break

                if can_move:
                    current_path.append(new_location)
                    visited_paths.append(current_path)
                else:
                    continue
                
                if objects_collected == 5:
                    # Cat returns home after collecting 5 objects
                    
                    # Move the cat back to the center of the map
                    while cat_location != [center_x, center_y] and time > 0:
                        if cat_location[0] > center_x:
                            cat_location[0] -= 1
                            time -= 0.01
                        elif cat_location[0] < center_x:
                            cat_location[0] += 1
                            time -= 0.01
                
                        if cat_location[1] > center_y:
                            cat_location[1] -= 1
                            time -= 0.01
                        elif cat_location[1] < center_y:
                            cat_location[1] += 1
                            time -= 0.01
                    
                    objects_collected = 0
                    arr[cat_location[0], cat_location[1]] = "0"  # Remove the cat from the last position
                
    return f"Path Hunting of {cat_name}: {path}\n{cat_name} got: {objects_score} {fav_objects}";              
    