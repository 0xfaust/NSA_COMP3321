#! /usr/bin/env python3
# -*- coding: utf-8 -*-
'''Lecture 03, Exercise 16

Use range to write a for loop to print out a numbered grocery list.
'''

shopping_list = ['milk', 'eggs', 'bread', 'apples', 'tea']

for item in range(0, len(shopping_list)):
    print(str(item + 1) + ': ' + shopping_list[item])

