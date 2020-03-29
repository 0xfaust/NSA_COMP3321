#! /usr/bin/env python3
# -*- coding: utf-8 -*-
'''Lecture 02, Exercise 08

Run dir(random). Find a function in random that you can use to return a
random item from your grocery list. Remember you can use help() to find out
what different functions do!
'''
import random

shopping_list = {'milk':9.42, 'eggs':5.67, 'bread':3.25, 'apples':13.40, 'tea':7.50}

print(dir(random))
print(random.choice(list(shopping_list.keys())))

