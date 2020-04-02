#! /usr/bin/env python3
# -*- coding: utf-8 -*-
''' Lecture 02, Exercise 21

Write an 'April fools' color_swapper function that takes my_color and 
neighbor_color as inputs and prints a message declaring your and your
neighbour's favourite colours are respectively. Add a line before the print 
that swaps the contents of the variables so that now the message is printed
with your favourite colours swapped. Run your function and then print the 
contents of my_color and neighbor_color. How were you able to swap them in the
function without swapping them in your notebook?
'''

def color_swapper(my_color, neighbor_color):
    my_color, neighbor_color = neighbor_color, my_color
    print('Your favourite color is: ' + my_color)
    print('Your neighbours favourite colour is: ' + neighbor_color)

my_color = input('Please enter your favourite colour: ')
neighbor_color = input('Please enter your neighbour\'s favourite colour: ')

color_swapper(my_color, neighbor_color)
print(my_color)
print(neighbor_color)

