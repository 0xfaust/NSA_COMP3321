#! /usr/bin/env python3
# -*- coding: utf-8 -*-
'''Lecture 02, Exercise 11

Write an all_the_snacks function that takes a snack (string) and uses the *
operator to print it out 100 times. Test your function using each of the items
on your grocery list. What happens if you enter a number into your function?
Is the result as expected?
'''

def all_the_snacks(snack):
    return (snack * 100)

shopping_list = {'milk':9.42, 'eggs':5.67, 'bread':3.25, 'apples':13.40, 'tea':7.50}

for item in shopping_list:
    print(all_the_snacks(item))

print(all_the_snacks(5))

