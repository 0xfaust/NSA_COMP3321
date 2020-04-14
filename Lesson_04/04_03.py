#! /usr/bin/env python3
# -*- coding: utf-8 -*-
'''Lecture 04, Exercise 03

Write a function that takes a portion mark as input and returns the full
classification. 
- convert_classification('U//FOUO') should return 'UNCLASSIFIED//FOR OFFICIAL
USE ONLY'
- convert_classification('S//REL TO USA, FVEY') should return 'SECRET//REL TO USE, FVEY'
'''

def convert_classification(portion_mark):
    portion_dict = {'U//': 'UNCLASSIFIED//',
                    'FOUO': 'FOR OFFICIAL USE ONLY',
                    'S//': 'SECRET//'}
    for key, value in portion_dict.items():
        portion_mark = portion_mark.replace(key, value)
    return portion_mark

print(convert_classification('U//FOUO'))
print(convert_classification('S//REL TO USA, FVEY'))

