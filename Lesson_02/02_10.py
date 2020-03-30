#! /usr/bin/env python3
# -*- coding: utf-8 -*-
'''Lecture 02, Exercise 10

Challenge: Your grocery store is having a weird promotion called 'win free
challenge'! A random item from your (price) list is chosen and you pay 10
dollars. If the item is less than 10 dollars you get the item and the change
back as normal; however, if you get lucky and the price is more than 10
dollars you get the item and the difference in price back as change. Write
code randomly pick a price from your price list and print out the amount of
change the cashier has to pay you during this promotion. Hint: use the built
in abs function.
'''

import random

shopping_list = {'milk':9.42, 'eggs':5.67, 'bread':3.25, 'apples':13.40, 'tea':7.50}

item, price = random.choice(list(shopping_list.items()))
print(item)
print(abs(10 - price))

