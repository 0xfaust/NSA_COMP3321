#! /usr/bin/env python3
# -*- coding: utf-8 -*-
''' Lecture 02, Exercise 24

Write a function called 'Volume2' which calculates the box volume, assuming
the height is 1, if not given.
'''

def volume2(width, length, height=1):
    return(width * length * height)

print(volume2(2, 5))

