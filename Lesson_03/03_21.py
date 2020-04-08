#! /usr/bin/env python3
# -*- coding: utf-8 -*-
'''Lecture 03, Exercise 21

Using a loop and enumerate, write a function getindex(string, character) to 
recreate the string method index.
"skyscraper".index('c')
# 4
getindex("skyscraper", 'c')
# 4
'''

def getindex(string, character):
    for index, value in enumerate(string):
        if value == character:
            print(index)
            exit()

getindex("skyscraper", 'c')

