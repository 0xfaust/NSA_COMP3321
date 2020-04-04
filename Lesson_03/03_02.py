#! /usr/bin/env python3
# -*- coding: utf-8 -*-
'''Lecture 03, Exercise 02

Write a function snack_check that takes a string snack and returns True or
False depending on whether or not it is your favourite snack.
'''

def snack_check(snack):
    return(snack == 'coffee')

snack = 'coffee'
other_snack = 'banana'

print(snack_check(snack))
print(snack_check(other_snack))

