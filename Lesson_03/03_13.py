#! /usr/bin/env python3
# -*- coding: utf-8 -*-
'''Lecture 03, Exercise 13

Write a for loop that prints out a numbered list of your grocery items.
'''

shopping_list = ['milk', 'eggs', 'bread', 'apples', 'tea']
i = 1
for item in shopping_list:
    print(str(i) + ': ' + item)
    i += 1

