#! /usr/bin/env python3
# -*- coding: utf-8 -*-
'''Lecture 03, Exercise 04

Write an in_grocery_list function that takes in  a grocery_item print a message
depending on whether grocery_item is in your grocery list.
'''

def in_grocery_list(grocery_item):
    shopping_list = ['milk', 'eggs', 'bread', 'apples', 'tea']

    if grocery_item in shopping_list:
        print('That item is in the shopping list')
    else:
        print('That item is not in the shopping list')

in_grocery_list('milk')
in_grocery_list('sugar')

