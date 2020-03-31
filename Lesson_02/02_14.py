#! /usr/bin/env python3
# -*- coding: utf-8 -*-
'''Lecture 02, Exercise 14

Write an in_grocery_list function that takes in a grocery_item returns True or
False depending on whether the item is on your list.
'''

def in_grocery_list(grocery_item):
    shopping_list = {'milk':9.42, 'eggs':5.67, 'bread':3.25, 'apples':13.40, 'tea':7.50}
    
    if grocery_item in shopping_list:
        return True
    else:
        return False

print(in_grocery_list('tea'))
print(in_grocery_list('coffee'))

