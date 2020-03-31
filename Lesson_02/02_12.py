#! /usr/bin/env python3
# -*- coding: utf-8 -*-
'''Lecture 02, Exercise 12

You may have noticed that your all_the_snacks function prints all your snacks
squished together. Rewrite all_the_snacks so that it takes an additional
argument spacer. Use + to combine your snack and spacer before multiplying.
Test your function with different inputs. What happens if you use strings for
both snack and spacer? Both numbers? A string and integer? Is it what you
expected?
'''

def all_the_snacks(snack, spacer):
    return ((snack + (' '  * spacer)) * 100)

shopping_list = {'milk':9.42, 'eggs':5.67, 'bread':3.25, 'apples':13.40, 'tea':7.50}

for item in shopping_list:
    print(all_the_snacks(item, 2))

#print(all_the_snacks('hello', 'world'))
#print(all_the_snacks(5,3))
print(all_the_snacks('hello', 5))
#print(all_the_snacks(5, 'hello'))
