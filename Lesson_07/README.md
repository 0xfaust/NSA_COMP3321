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

## Your First Class
Just as the keyword `def` is used to define functions, the keyword `class` is used to define a `type` object that will generate a new kind of object, which you get to name!.
```python
class Person(object):
	pass

print(type(Person))
```
At first, the `Person` class doesn't do much, because it's totally empty! This isn't as useless as it seems, because, just like everything else in Python, classes and their objects are *dynamic*. The `(object)` after `Person` is not a function call; here it names the parent class. Even though the `Person` class looks boring, the fundamentals are there:
- the `Person` class is just as much of a class as `int` or any other built-in,
- we can make an *instance* by using the class name as a constructor function, and
- the `type` of the instance `nobody` is `Person`, just like `type(1)` is `int`.
  
```python 
class Person(object):
	species = "Homo sapiens"
	def talk(self):
		return "Hello there, how are you?"
nobody = Person()
print(nobody.species)
nobody.talk()
```
It's **very important** to give any method(i.e. function defined in the class) at least one argument, which is almost always called `self`. This is because internally Python translates `nobody.talk()` into something like `Person.talk(nobody)`
