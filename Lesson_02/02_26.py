#! /usr/bin/env python3
# -*- coding: utf-8 -*-
''' Lecture 02, Exercise 26

Write a function ifDivisibleBy7(num) to check if a number is evenly divisible
by 7.
'''

def isDivisibleBy7(num):
    return(num % 7 == 0)

print(isDivisibleBy7(21))
print(isDivisibleBy7(25))
