#! /usr/bin/env python3
# -*- coding: utf-8 -*-
'''Lecture 02, Exercise 05

Use the 'fast swapping' to swap your favourite snack with your neighbours.
Print both variables to see the result.
'''

snack = 'coffee'
other_snack = 'tea'

print(snack, other_snack)

snack, other_snack = other_snack, snack

print(snack, other_snack)
