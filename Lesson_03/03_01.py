#! /usr/bin/env python3
# -*- coding: utf-8 -*-
'''Lecture 03, Exercise 01

Write a you_won function that randomly picks a number from your price list
(9.42, 5.67, 3.25, 13.40 and 7.50) and prints True or False depending on 
whether the random number is greater than 10.
'''
import random

def you_won(price_list):
    random_number = price_list[random.randint(0, len(price_list) - 1)]
    print(random_number)
    if random_number > 10:
        return True
    else:
        return False

price_list = [9.42, 5.67, 3.25, 13.40, 7.50]

print(you_won(price_list))

