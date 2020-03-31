#! /usr/bin/env python3
# -*- coding: utf-8 -*-
'''Lecture 02, Exercise 15

Write a price_matcher function that takes no arguments, but prints a random
grocery item and a random price from your price list every time it is run.
'''

import random

def price_matcher():
    shopping_list = {'milk':9.42, 'eggs':5.67, 'bread':3.25, 'apples':13.40, 'tea':7.50}

    print(random.choice(list(shopping_list.keys())))
    print(int(random.choice(list(shopping_list.values()))))

price_matcher()
