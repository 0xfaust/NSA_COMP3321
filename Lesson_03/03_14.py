#! /usr/bin/env python3
# -*- coding: utf-8 -*-
'''Lecture 03, Exercise 14

Clearly your favourite snack is more important that the other items on your
list. Modify your for loop from Exercise 3 (13) to use break stop printing
once you have found your favourite snack on the list. Question: Could you have
achieved the same result without using a break? Bonus: if your snack isn't on 
the list, have your code print a warning at the end. 
'''

shopping_list = ['milk', 'eggs', 'bread', 'apples', 'tea']
snack = 'coffee'
in_list = False
i = 1

for item in shopping_list:
    print(str(i) + ': ' + item)
    if item == snack:
        in_list = True
        break
    i += 1

if in_list == False:
    shopping_list.append(snack)

print(shopping_list)

