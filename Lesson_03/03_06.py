#! /usr/bin/env python3
# -*- coding: utf-8 -*-
'''Lecture 03, Exercise 06

Challenge: Re-write the you_won function to randomly choose a number from your
price list and print an appropriate messsage depending on whether you won (the
number was greater than 10) or not. Also include the amount of change you will
be receiving in your message. (Recall you are winning the amount change that 
you would have owed...)
'''

import random

def you_won(price_list):
    random_number = price_list[random.randint(0, len(price_list) - 1)]
    print(random_number)
    if random_number > 10:
        print('You have won $' + str(round(abs(10 - random_number),2)))
    else:
        print('You lost')

price_list = [9.42, 5.67, 3.25, 13.40, 7.50]

you_won(price_list)

