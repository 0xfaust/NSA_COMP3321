#! /usr/bin/env python3
# -*- coding: utf-8 -*-
'''Lecture 04, Exercise 02

Write a function that takes a list as a parameter and returns a second list
composed of any objects that appear more than once in the original list.
- duplicates([1,2,3,6,7,3,4,5,6]) should return [3,6]
- what should duplicates(['cow', 'pig', 'goat', 'horse', 'pig']) return?
'''

def duplicates(original_list):
    unique_set = set(original_list)
    unique_list = list(unique_set)
    return [item for item in original_list if not item in unique_list or unique_list.remove(item)]

print(duplicates([1,2,3,6,7,3,4,5,6]))
print(duplicates(['cow', 'pig', 'goat', 'horse', 'pig']))

