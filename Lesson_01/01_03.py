#! /usr/bin/env python3
# -*- coding: utf-8 -*-
'''Lecture 01, Exercise 03

But wait! You decide you want to buy five of the last item. Re-calculate
your total.
'''

shopping_list = {'milk':9.42, 'eggs':5.67, 'bread':3.25, 'apples':13.40, 'tea':7.50}
total_cost = 0

for item in shopping_list:
    total_cost += shopping_list[item]

total_cost += shopping_list['tea']*4

print(total_cost)

