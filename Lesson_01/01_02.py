#! /usr/bin/env python3
# -*- coding: utf-8 -*-
'''Lecture 01, Exercise 02

Your groceries ring up as 9.42, 5.67, 3.25, 13.40 and 7.50 respectively.
Use python as a handy calculator to add up these amounts. 
'''

shopping_list = {'milk':9.42, 'eggs':5.67, 'bread':3.25, 'apples':13.40, 'tea':7.50}
total_cost = 0

for item in shopping_list:
    total_cost += shopping_list[item]

print(total_cost)

