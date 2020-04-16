#! /usr/bin/env python3
# -*- coding: utf-8 -*-
'''Lecture 05, Exercise 02

Copy the sonnet from https://urn.nsa.ic.gov/t/tx6qm and paste into sonnet.txt.

Write a function called word_count() that takes a file name and returns a 
dictionary containing the counts for each word. Remove all punctuation except
apostrophe. Lowercase all words.
'''

def word_count(input_filename):
    input_file = open(input_filename, 'r')
    
    count = {}

    for line in input_file:
        for word in line.split():
            word = word.lower()
            if word in count:
                count[word] += 1
            else:
                count[word] = 1

    input_file.close()
    return count

count = word_count('sonnet.txt')
print(count)

