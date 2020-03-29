#! /usr/bin/env python3
# -*- coding: utf-8 -*-
'''Lecture 02, Exercise 07

import random and run help(random.randint). Use randint to randomly print
between 0 and 100 copies of your favourite snack.
'''
import random

help(random.randint)
snack = 'coffee'

print((snack + ' ') * random.randint(0,100))
