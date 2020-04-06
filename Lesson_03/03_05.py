#! /usr/bin/env python3
# -*- coding: utf-8 -*-
'''Lecture 03, Exercise 05

Modify in_grocery_list to test if grocery_item is a string. Print a message
warning the user if it is not.
'''

def in_grocery_list(grocery_item):
    shopping_list = ['milk', 'eggs', 'bread', 'apples', 'tea']

    if type(grocery_item) != str:
        print('The item is not a string')
        return(0)

    if grocery_item in shopping_list:
        print('That item is in the shopping list')
    else:
        print('That item is not in the shopping list')

in_grocery_list('milk')
in_grocery_list('sugar')
in_grocery_list(1)
