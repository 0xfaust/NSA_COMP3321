#! /usr/bin/env python3
# -*- coding: utf-8 -*-
'''Lecture 02, Exercise 16

Challenge: modify your price_matcher to return item, price rather than print
them. Write a free_change function that calls your new price_matcher and uses
the result to print your item and the absolute value of the change for the item
assuming you paid $10.
'''

import random

def price_matcher():
    shopping_list = {'milk':9.42, 'eggs':5.67, 'bread':3.25, 'apples':13.40, 'tea':7.50}
    item = random.choice(list(shopping_list.keys()))
    price = int(random.choice(list(shopping_list.values())))

    return(item, price)

item, price = price_matcher()
print(item + ', ' + str(abs(10-price)))
