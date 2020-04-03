#! /usr/bin/env python3
# -*- coding: utf-8 -*-
''' Lecture 02, Exercise 31

What value is in varaible my_var at the end of these assignments? Add a 
comparison after the last statement in the form of my_val == 
'''

my_var = 99 # 99
my_var += 11 # 110
my_var = str(my_var) # '110'
my_var *= 2 # '110110'
my_var = len(my_var) # 6
my_var *= 4 # 24

my_val = 24

print(my_val == my_var)
