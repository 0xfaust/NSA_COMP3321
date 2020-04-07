# Lesson 02: Variables and Functions
  
'Introduction to variables and functions in Python.'
  
Here are some key notes taken from this lesson which may help with the exercises.

## My Kingdom for a Variable
A **variable** in Python is a name that's attached to something -- a number, a string, or something more complicated, like a list, an object, or even a type. Python is dynamically typed, which means that a variable, once declared, can hold different types of data over its lifetime. A variable is declared with the = operator.  

## Functions
Python comes with a bunch of built-in functions. We’ve used a few of these already: `dir()`, `min()`, `max()`, `isinstance()`, and `type()`. But functions take memory, and there are hundreds of modules included with Python, so we can't have access to everything that Python can do all at once. In order to use functions that aren't built in, we must tell Python to load them. We do this with the import statement: `import os`.  
This loads the **`os`** module. A **module** is a file containing definitions and statements, and are generally used to hold a collection of relatated functions. The `os` module contains functions relating to the Operating System of the computer where Python is running.  
We'll get into more modules later in the class. For now we'll just touch on two others: `sys`, which contains variables and functions relating to Python's interaction with the system; and `random`, which provides random number generation.  

## Making your own Functions
Functions (in Python) are really just special variables (or datatypes) that can have input and output. Once defined, you can treat them like any other variables.  
Functions are defined with a specific syntax:  
- Start with the keyword `def`,
- followed by the function name, and
- a list of arguments enclosed in `()`, then
- the line ends with a `:`, and
- the body of the function is indented on following lines.
  
Python uses whitespace to determine blocks, unlike C, Java, and other languages that use `{}` for this purpose. To have output from the function, the return keyword is used, followed by the thing to be returned. For no output, use return by itself, or just leave it out.  

## Arguments, Keyword Arguments, and Defaults
You can give arguments default values. This makes them optional. You can call arguments by name also.

## Scope
In programming, scope is an important concept. It is also very useful in allowing us to have flexibility in reusing variable names in function definitions. Whenever we try to get or change the value of a variable, Python always looks for that variable in the most appropriate (closest) scope. Be careful with scope, it can allow you to do some things you might not want to (or maybe you do!), like overriding built-in functions.  

## Input
The `input` function is a quick way to get data accessed from `stdin` (user input). It takes an optional string argument that is the prompt to be issued to the user, and always returns a string.

