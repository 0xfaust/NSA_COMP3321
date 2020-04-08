#! /usr/bin/env python3
# -*- coding:utf-8 -*-
'''Lecture 03, Exercise 15

Challenge: use the string method split to write a for loop that splits out each
word in the string "blood-oxygenation level dependent functional magnetic 
resonance imaging" Hint: run help(str.split)
'''

wordNet_string = 'blood-oxygenation level dependent functional magnetic resonance imaging'

for word in wordNet_string.split(' '):
    print(word)

