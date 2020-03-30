#! /usr/bin/env python3
# -*- coding: utf-8 -*-
'''Lecture 02, Exercise 09

Write code to randomly select a price from your list of grocery prices, round
to the nearest integer, and print the result.
'''
import random

shopping_list = {'milk':9.42, 'eggs':5.67, 'bread':3.25, 'apples':13.40, 'tea':7.50}

print(int(random.choice(list(shopping_list.values()))))

