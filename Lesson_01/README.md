# Lesson 01: Introduction: Your Fisrt Python Program

'Covers Anaconda installation, the Python interpreter, basic data types, running code, and some built-ins.'
  
Here are some key notes taken from this lesson which may help with the exercises. 
  
## Basic Basics: Data and Operations
The most basic data types in Python are:
- Numbers:
  - Integer `<type 'int'>` (these are 'arbitrary precision', no need to worry whether it's 32 bits or 64 bits, etc.)
  - Float `<type 'float'>`
  - Complex `<type 'complex'>` (using `1j` for the imaginary number)
- Strings `<type 'str'>`
  - No difference between single and double quotes
  - Escape special characters (e.g. quotation marks)
  - Raw String `r'raw string'` prevents need for some escapes
  - Triple-quotes allow multiple line strings
  - Unicode `u'Bert \x26 Ernie' <type 'unicode'>`
- Booleans `True` and `False`
  
We operate on data using:
- **operators**, e.g. mathematical operators `+`, `-`; the keyword `in`, and others
- **functions**, which are operations that take one or more pieces of data as arguments, e.g. `type(*hello')`, `len('world')`, and 
- **methods**, which are attached to a piece of data and called from it using a `.` to separate the data from the method, e.g.`'HelloWorld'.split()`, or `'abc'.upper()`
  
Pieces of basic data can be stored inside containers, including
- Lists
- Dictionaries
- Sets
  
## Built-in Functions and Methods
Some functions work on almost any arguments that you supply:
- `help(x)` : shows interactive help
- `dir(x)` : gives the **directory** of the object, i.e. all the methods available
- `type(x)` : tells you the type of `x` — a type is almost the same as any other object
- `isinstance(a,b)` : tells if object `a` is an instance of `b`, which must be a `type`; something like `type(a)==b` 
- `print`
- `hasattr(a,b)` : tells whether `a` has something by the name `b`; something like `b in dir(a)`
- `getattr`
- `id`
- `input`
  
Constructor functions usually try to do their best with the arguments you give, and return the appropriate data of the requested type:
- `str` : turns numbers (and other things) into their string representations
- `int` : truncates `float`, parses `str`ings containing a single integer, with optional **radix(i.e. base)**, error on `complex`
- `float` : parses `str`ings, gives `float` representation of `int`, error on `complex`
- `complex` : takes `(real,imag)` numeric arguments, or parses a `str` for a single number
  
Other functions only work with one or two types of data:
- Numbers:
  - Functions : `abs`, `round`, `float`, `max`, `min`, `pow`(modular), `chr`, `divmod`, etc.
  - Operators : Standard math, bitwise: `«`,`»`,`&`,`|`,`^`,`~`
  - Methods : Numeric classes don't have methods
- Strings:
  - Functions : `len`, `min`, `max`, `ord`
  - Operators : `+`, `*` (withanumber), `in`
  - Methods : `strip`, `split`, `startswith`, `upper`, `find`, `index`, many more; use `dir('anystring')` to find more.



