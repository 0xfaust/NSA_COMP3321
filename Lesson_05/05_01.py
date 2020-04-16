#! /usr/bin/env python3
# -*- coding: utf-8 -*-
'''Lecture 05, Exercise 01

Copy the sonnet from https://urn.nsa.ic.gov/t/tx6qm and paste into sonnet.txt.

Write a function called file_capitalize() that takes an input file name and an
output file name, then writes each word from the input file with only the first
letter capitalized to the output file. Remove all punctuation except apostrophe.
'''

def file_capitalize(input_filename, output_filename):
    input_file = open(input_filename, 'r')
    output_file = open(output_filename, 'w')
    
    for line in input_file:
        for word in line.split():
            output_file.write(word.capitalize())

    input_file.close()
    output_file.close()

file_capitalize('sonnet.txt', 'sonnet_caps.txt' )

