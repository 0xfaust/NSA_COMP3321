#! /usr/bin/env python3
# -*- coding: utf-8 -*-
'''Lecture 03, Exercise 17

Use enumerate to print out a numbered grocery list. You've now done this three
ways. What are some pros and cons to each technique? There are often several
different ways to get the same output! However, usually one is more elegant
than the others.
'''

shopping_list = ['milk', 'eggs', 'bread', 'apples', 'tea']

for item in enumerate(shopping_list):
    print(item)

