#! /usr/bin/env python3
# -*- coding: utf-8 -*-
'''Lecture 07, Exercise 02

Make a RangedQuery class that inherits from Query and has the additional
attributes:
- begin date
- end date
For now, just make the dates of the form YYYY-MM-DD. Don't worry about date
formatting or error checking for now. We'll talk about the datetime module 
and exception handling later.
Provide defaults for these attributes. Make sure you incorporate the Query 
class's initialiser into the RangedQuery initialiser. Ensure the new class
can also be printed nicely. 
Afterwards this should work:
query2 = RangedQuery("TS//SI//REL_TO_USA,FVEY", "Primary email address of Zendian
                diplomat", "10.254.18.162", "2016-12-01", "2016-12-31")
'''

class Query():
    def __init__(self, mark=None, desc=None, email=None):
        self.mark = mark
        self.desc = desc
        self.email = email
    def __str__(self):
        return "Mark {0} used for {1} associated with address: {2}.".format(self.mark, self.desc, self.email)

class RangedQuery(Query):
    def __init__(self, mark, desk, email, start=None, end=None):
        super(RangedQuery, self).__init__(mark, desk, email)
        self.start = start
        self.end = end
    def __str__(self):
        return super(RangedQuery, self).__str__() + " starting on {0} and ending on {1}".format(self.start, self.end)

query2 = RangedQuery("TS//SI//REL_TO_USA,FVEY", "Primary email address of Zendian diplomat", "10.254.18.162", "2016-12-01", "2016-12-31")
print(query2)

