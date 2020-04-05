#! /usr/bin/env python3
# -*- coding: utf-8 -*-
'''Lecture 03, Exercise 03

Re-write the snack_check to take a string snack and print an appropriate
response depending on whether the input is your favourite snack or not.
'''

def snack_check(snack):
    if snack == 'coffee':
        print('That is also my favourite snack')
    else:
        print('That is not my favourite snack')

snack_check(input('What is your favourite snack? '))

