#! /usr/bin/env python3
# -*- coding: utf-8 -*-
'''Lecture 02, Exercise 17

Rewrite all_the_snacks so that num and spacer have defaults 100 and ', '
respectively. Using your favourite snack as input, try running your function
with no additional argument. 
'''

def all_the_snacks(snack, spacer=', ', num=100):
    return ((snack + spacer) * num)

snack = 'coffee'

print(all_the_snacks(snack))

