#! /usr/bin/env python3
# -*- coding: utf-8 -*-
'''Lecture 01, Exercise 06

Challenge: Run dir('any string'). Pick two methods that sound interesting 
and run help('any string'.interesting_method) for both of them. Can you figure
out how to use these methods?
'''

print(dir('any_string'))
help('any_string'.find)
help('any_string'.rsplit)

print('any_string'.find('string'))
print('any_string'.rsplit('_'))
