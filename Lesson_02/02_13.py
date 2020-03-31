#! /usr/bin/env python3
# -*- coding: utf-8 -*-
'''Lecture 02, Exercise 13

Rewrite all_the_snacks so that it also takes a variable num that lets you
customise the number of times your snack gets printed out.
'''

def all_the_snacks(snack, spacer, num):
    return ((snack + (' '  * spacer)) * num)

shopping_list = {'milk':9.42, 'eggs':5.67, 'bread':3.25, 'apples':13.40, 'tea':7.50}

for item in shopping_list:
    print(all_the_snacks(item, 2, 3))

