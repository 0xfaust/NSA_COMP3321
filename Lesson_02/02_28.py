#! /usr/bin/env python3
# -*- coding: utf-8 -*-
''' Lecture 02, Exercise 28

Make a function shout(word) that accepts a string and returns that string in
capital letters with an exclaimation mark.
'''

def shout(word):
    return(word.upper() + '!')

print(shout('bananas'))

