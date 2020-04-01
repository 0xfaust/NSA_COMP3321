#! /usr/bin/env python3
# -*- coding: utf-8 -*-
'''Lecture 02, Exercise 18

Try running all_the_snacks with your favourite snack and the spacer '! ' and
no additional inputs. How would you run it while inputting your favourite snack
and 42 for num while keeping the default spacer? Can you use this method to enter
spacer and num in reverse order?
'''

def all_the_snacks(snack, spacer=', ', num=100):
    return ((snack + spacer) * num)

snack = 'coffee'

print(all_the_snacks(snack, '! '))
print(all_the_snacks(snack, num=42))
print(all_the_snacks(snack, num=10, spacer='...'))

