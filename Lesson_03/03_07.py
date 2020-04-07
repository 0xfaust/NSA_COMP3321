#! /usr/bin/env python3
# -*- coding:utf-8 -*-
'''Lecture 03, Exercise 07

Advanced challenge: Write a function that imports datetime and uses it to
determine the current time. This function should print an appropriate
message based on the time ex: if the current time is between 0900 and 1000,
print the message 'Morning lecture time!'
'''

import datetime

def timeMessage():
    time = datetime.datetime.now()
    if time.hour in range(0, 6):
        print('Night Time')
    elif time.hour in range(6, 12):
        print('Morning Time')
    elif time.hour in range(12, 18):
        print('Afternoon Time')
    elif time.hour in range(18, 24):
        print('Evening Time')

timeMessage()

