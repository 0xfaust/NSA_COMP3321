#! /usr/bin/env python3
# -*- coding: utf-8 -*-
''' Lecture 02, Exercise 30

Identify the type of each of the following variables, and add the type after
each variable in a comment. 
'''

variables = [2999, # int
             90.0, # float
             "145", # str
             "\u0CA0_\u0CA0", # str 
             "True", # str
             True, # bool
             len("sample"), # int
             100**30, # int
             1 >= 1, # bool
             30%7, # int
             30/7, # float
             90.0 + 7, # float
             128 << 1, # int
             bin(255), # str
             [128 << 1, 90.0+7, 30/7, bin(255)], # list
             len([128 << 1, 90.0+7, 30/7, bin(255)])] # int

for variable in variables:
    print(str(variable) + str(type(variable)))

