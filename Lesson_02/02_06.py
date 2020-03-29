#! /usr/bin/env python3
# -*- coding: utf-8 -*-
'''Lecture 02, Exercise 06

Make a list of your grocery prices (9.42, 5.67, 3.25, 13.40 and 7.50 respectively) and store in a variable. Use built in functions to find the price of the cheapest and most expensive item on your grocery list.
'''

shopping_list = {'milk':9.42, 'eggs':5.67, 'bread':3.25, 'apples':13.40, 'tea':7.50}

print(min(shopping_list, key=shopping_list.get))
print(max(shopping_list, key=shopping_list.get))
