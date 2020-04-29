#! /usr/bin/env python3
# -*- coding: utf-8 -*-
'''Lecture 07, Exercise 01

Write a Query class that has the following attributes:
 - classification
 - justification
 - selector
Provide default values for each attribute (consider using None). Make it so
that when you print it, you can display all of the attributes and their values
nicely.
# your class definition here
Afterwards, something like this should work:
query1 = Query("TS//SI//REL_TO_USA,FVEY", "Primary email address of Zendian
                diplomat", "ileona@stato.gov.zd")
'''

class Query():
    def __init__(self, mark=None, desc=None, email=None):
        self.mark = mark
        self.desc = desc
        self.email = email
    def __str__(self):
        return "Mark {0} used for {1} associated with address: {2}.".format(self.mark, self.desc, self.email)

query1 = Query("TS//SI//REL_TO_USA, FVEY", "Primary email address of Zendian diplomat", "ileona@stato.gov.zd")
print(query1)

