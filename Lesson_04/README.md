# Lesson 04: Container Data Types
  
Here are some key notes taken from this lesson which may help with the exercises.

## Introduction
Data Containers allow us to build up complicated structures. There are different ways of putting data into containers, depending on what we need to do with it, and Python has several built-in containers to support the most common use cases. Python's built-in container types include:
1. `list`
2. `tuple`
3. `dict`
4. `set`
5. `frozenset`
Of these, `tuple` and `frozenset` are **immutable**, which means that they cannot be changed after they are created, whether that's by addition, removal, or some other means. Numbers and strings are also immutable, which should make the following statement more sensible: the **variable** that names an immutable object can be reassigned, but the immutable object itself can't be changed.  
To create an instance of any container, we call its name as a function (sometimes known as a *constructor*). With no arguments, we get an empty instance, which isn't very useful for immutable types. Shortcuts for creating non-empty lists, tuples, dicts, and even sets will be covered in the following sections. 


