#! /usr/bin/env python3
# -*- coding: utf-8 -*-
'''Lecture 05, Exercise 03

Copy the sonnet from https://urn.nsa.ic.gov/t/tx6qm and paste into sonnet.txt.

Write the counts dictionary to a file, one key:value per line.
'''

def word_count_file(input_filename, output_filename):
    input_file = open(input_filename, 'r')
    output_file = open(output_filename, 'w')
    
    count = {}

    for line in input_file:
        for word in line.split():
            word = word.lower()
            if word in count:
                count[word] += 1
            else:
                count[word] = 1
    
    for key, value in count.items():
        output_file.write(key + ':' + str(value) + '\n')

    input_file.close()
    output_file.close()

word_count_file('sonnet.txt', 'sonnet_dict.txt')

