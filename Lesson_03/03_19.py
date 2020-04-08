#! /usr/bin/env python3
# -*- coding: utf-8 -*-
'''Lecture 03, Exercise 19

Challenge: Write a 'Guess my number' game that generates a random number and 
gives your user a fixed number of guesses. Use input to get the user's guesses.
Think about what loop type you might use and how you might provide feedback 
based on the user's guesses. Hint: what type does input return? You might need
to convert it to a more useful type... However, now what happens if your user 
inputs something that isn't a number?
'''

import random

def guess_my_number():
    answer = random.randint(0, 10)
    turns = 5
    
    print('Guess a number between 1 and 10')

    for turn in range(0, turns):
        print('You have ' + str(turns - turn) + ' guess(\'s) left')
        guess = input('Please make guess number ' + str(turn+1) + ': ')
        if int(guess) == answer:
            print('Correct!')
            exit()
        else:
            print('Incorrect!')

guess_my_number()
