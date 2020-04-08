#! /usr/bin/env python3
# -*- coding: utf-8 -*-
'''Lecture 03, Exercise 22

Using the shout fuction from the first set of basic exercises, write a 
shout_words(sentence) function that takes a string argument and 'shouts' each
word on its own line. 
shout_words("Everybody likes bananas")
# EVERYBODY!
# LIKES!
# BANANAS!
'''

def shout(word):
    return(word.upper() + '!')

def shout_words(sentence):
    for word in sentence.split(' '):
        print(shout(word))

shout_words('Everybody likes bananas')

