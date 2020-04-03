#! /usr/bin/env python3
# -*- coding: utf-8 -*-
''' Lecture 02, Exercise 29

Make a function introduce() to ask the user for their name and shout it back
to them. Call your function shout to make this happen.
'''

def shout(word):
    return(word.upper() + '!')

def introduce():
    print('HI ' + shout(input('What\'s your name? ')))

introduce()

