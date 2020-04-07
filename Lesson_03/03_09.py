#! /usr/bin/env python3
# -*- coding:utf-8 -*-
'''Lecture 03, Exercise 09

Mix and match! Write a while loop that uses the * to print multiple copies of
your favourite snack per line. Print out 10 lines with the number of copies per
line corresponding to the line number (your first line will have one copy and
your last line will have 10).
'''

snack = 'coffee'
i = 1

while (i < 11):
    print((snack + ' ') * i)
    i += 1

