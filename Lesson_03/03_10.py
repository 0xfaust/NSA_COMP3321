#! /usr/bin/env python3
# -*- coding:utf-8 -*-
'''Lecture 03, Exercise 10

Challenge: Write a while loop that prints 100 copies of your favourite snack
on one single (wrapped) line. Hint: use +.
'''

snack = 'coffee'
snack_string = ''
i = 1

while (i < 101):
    snack_string += snack + ' '
    i += 1

print(snack_string)

