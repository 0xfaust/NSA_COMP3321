#! /usr/bin/env python3
# -*- coding: utf-8 -*-
''' Lecture 02, Exercise 22

Challenge: Write a global_color_swapper that swaps your colours globally. Run 
your function and then print the contents if my_color and neighbor_color. Why
might this be a bad idea, even for an April fool's joke?
'''

def global_color_swapper():
    global my_color
    global neighbor_color
    my_color, neighbor_color = neighbor_color, my_color

my_color = 'black'
neighbor_color = 'red'

global_color_swapper()

print(my_color)
print(neighbor_color)

