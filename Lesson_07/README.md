# Lesson 07: Object Orienteering: Using Classes
  
'Introduction to classes, objects and inheritance in Python.'
  
Here are some key notes taken from this lesson which may help with the exercises.

## Introduction
From the name of it you can see that **object-oriented programming** is oozing with abstraction and complication. Take heart: there's no need to fear or avoid object-oriented programming in Python! It's just another easy-to-use, flexible, and dynamic tool in the deep toolbox that Python makes available.
  
Consider for example the difference between a **function** and a **method**:
```python
name = "Mark"
len(name) # function
name.upper() # method
```

In this example, `name` is an **instance** of the `str` **type**. In other words, `name` is an object of that type. An **object** is just a convenient wrapper around a combination of some *data* and *functionality* related to that data, embodied in **methods**. Until now, you've probably thought of every `str` just in terms of its data, i.e. the literal string "Mark" that was used to assign the variable. The **methods** that work with `name` were defined just once, in a **class definition**, and apply to every string that is ever created. **Methods** are actually the same thing as functions that live *inside* a class instead of *outside* it.
