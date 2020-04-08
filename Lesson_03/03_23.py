#! /usr/bin/env python3
# -*- coding: utf-8 -*-
'''Lecture 03, Exercise 23

Write an extract_longer(length, sentence) function that takes a sentence and
word length, then returns a list of the sentence's words that exceed the given
length. If no words match the length, return False.

extract_longer(5, "Try not to interrupt the speaker.")
# ['interrupt','speaker.']
extract_longer(7, "Sorry about the mess.”)
# False
'''

def extract_longer(length, sentence):
    long_words = []
    
    for word in sentence.split(' '):
        if len(word) > length:
            long_words.append(word)
    
    if len(long_words) > 0:
        return long_words
    else:
        return False

print(extract_longer(5, "Try not to interrupt the speaker."))
print(extract_longer(7, "Sorry about the mess."))

