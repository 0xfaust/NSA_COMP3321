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
Many built-in functions and even some operators work with container types, where it makes sense.

## Lists
A list is an ordered sequence of zero or more objects, which are often of different types. It is commonly created by putting square brackets [] around a comma-separated list of its initial values:
`fruit = ['Apple', 'Orange', 'Pear', 'Lime']`

Values can be added to or removed from the list in different ways: 
```python 
fruit.append(’Banana')
fruit.insert(3,'Cherry')
fruit.extend(['Cherry','Banana'])
fruit.remove('Banana')
fruit.pop()
```

## List Comprehension
One of the most common uses of a list is to iterate over its elements with a `for` loop, storing off the results of each iteration in a new list. Python removes the repetitive boilerplate code from this type of procedure with **list comprehensions**.  `d = [[i, i ** 2, i ** 3] for i in range(10) if i % 2]`

## Sorting and Reordering
The `sorted` function works on more than just lists, but always returns a new list with the same contents as the original in sorted order. There is also a `sort` method on lists that performs an in-place sort.
```python
sorted_fruit = sorted(fruit)
fruit.sort()
```

Reversing the order of a list is similar, with a built-in `reversed` function and an in-place `reverse` method for lists. The `reversed` function returns an iterator, which must be converted back into a list explicitly. To sort something in reverse, you *could* combine the `reversed` and the `sorted` methods, but you *should* use the optional `reverse` argument on the `sorted` and `sort` functions.
```python
r_fruit = list(reversed(fruit))
fruit.reverse()
sorted(r_fruit, reverse = True)
```

## Tuples
Much like a list, a `tuple` is an ordered sequence of zero or more objects of any type. They can be constructed by putting a comma-separated list of items inside parentheses (), or even by assigning a comma-separated list to a variable with no delimiters at all. Parentheses are heavily overloaded-they also indicate function calls and mathematical order of operations--so defining a one-element tuple is tricky: the one element must be followed by a comma. Because a `tuple` is **immutable**, it won't have any of the methods that change lists, like `append` or `sort`. 
`a = (1, 2, 'first and second')`

## Interlude: Index and Slice Notation
For the ordered containers `list` and `tuple`, as well as for other ordered types like strings, it's often useful to retrieve or change just one element or a subset of the elements, *Index* and *slice* notation are available to help with this. Indexes in Python always start at 0. We'll start out with a new list and work by example:
```python
animals = ['tiger', 'monkey', 'cat', 'dog', 'horse', 'elephant']
animals[l]
animals[1:3]
animals[::-1] == list(reversed(animals))
```
Becauses slicing returns a new list and not just a view on the list, it can be used to make a copy (technically a `shallow` copy)
```python
same_animals = animals
different_animals = animals[:]
same_animals[0] = 'lion'
animals[0]
different_animals[0] = 'leopard'
different_animals[0] == animals[0]
```

## Dictionaries
A `dict` is a container that associates keys with values. The keys of a `dict` must be unique, and only immutable objects can be keys. Values can be any type. The dictionary construction shortcut uses curly braces { } with a colon : between keys and values (e.g. `my_dict = {key: value, keyl: value1))`. Alternate constructors are available using the `dict` keyword. Values can be added, changed, or retrieved using index notation with *keys* instead of *index* numbers. Some of the operators, functions, and methods that work on sequences also work with dictionaries.
```python
bugs = {"ant": 10, "prayingmantis": 0}
bugs['fly'] = 5
bugs.update({'spider': 1})
del bugs['spider']
'fly' in bugs
```

Dictionaries have several additional methods specific to their structure. Methods that return lists, like `items`, `keys`, and `values`, are not guaranteed to do so in any particular order, but may be in consistent order if no modifications are made to the dictionary in between the calls. The `get` method is often preferable to index notation because it does not raise an error when the requested key is not found; instead, it returns `None` by default, or a default value that is passed as a second argument.

```python
bugs.items()
bugs.keys()
bugs.values()
bugs.get('fly')
```

## Sets and Frozensets
A `set` is a container that can only hold unique objects. Adding something that’s already there will do nothing (but cause no error). Elements of a set must be immutable (like keys in a dictionary). The `set` and `frozenset` constructors take any iterable as an argument, whether it's a `list`, `tuple`, or otherwise. Curly braces {} around a list of comma-separated values can be used in Python2.7 and later as a shortcut constructor, but that could causeconfusion with the `dict` shortcut. Two sets are equal if they contain the same items, regard less of order.
```python 
numbers = set([l,1,1,1,1,3,3,3,3,3,2,2,2,3,3,4])
numbers.add(4)
numbers.update([3,4,7])
numbers.pop()
numbers.remove(7)
numbers.discard(7)
```
A frozen set is constructed in a similar way; the only difference is in the mutability. This makes frozen sets suitable as dictionary keys, but frozen sets are uncommon.  
`a = frozenset([l,l,l,l,l,3,3,3,3,32,2,2,3,3,4])`
  
Sets adopt the notation of bitwise operators for set operations like union, intersection, and symmetric difference. This is similar to how the `+` operator isused for concatenating lists and tuples.
```python
house_pets = {'dog', 'cat', 'fish'}
farm_animals = {'cow', 'sheep’, 'pig', 'dog', 'cat'}
house_pets & farm_animals # intersection
house_pets | farm_animals # union
house_pets ^ farm_animals # symmetric difference
house_pets - farm_animals # asymmetric difference
```
There are verbose set methods that do the same thing, but with two important difference: they accept lists, tuples, and other iterables as arugments, and can be used to update the set in place. Comparison of sets is similar: operators can be used to compare two sets, while methods can be used to compare sets with other iterables. Unlike numbers or strings, sets are often incomparable.

## Coda: More Built-In Functions
We've seen how some built-in functions operate on one or two of these container types, but all of the following can be applied to any container, although they probably won't always work; that depends on the contents of the container. There are some caveats:
* When passed a dictionary as an argument, these functions look at the keys of the dictionary, not the values.
* The `any` and `all` functions use the boolean context of the values of the container, e.g. `0` is `False` and non-zero numbers are `True`, and all strings are `True` except for the empty string `''`, which is `False`.
* The `sum` function only works when the contents of the container are numbers.

```python
generic_container = farm_animals
all(generic_container)
any(generic_container)
```

