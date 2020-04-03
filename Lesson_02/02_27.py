#! /usr/bin/env python3
# -*- coding: utf-8 -*-
''' Lecture 02, Exercise 27

Write a function ifDivisibleBy(num,divisor) to check if a number is evenly divisible
by divisor.
'''

def isDivisibleBy7(num, divisor):
    return(num % divisor == 0)

print(isDivisibleBy7(35,7))
print(isDivisibleBy7(35,4))
