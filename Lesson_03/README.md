# Lesson 03: Flow Control
  
'Python flow control with conditionals and loops (if, while, for, range, etc.)'
  
Here are some key notes taken from this lesson which may help with the exercises.

## Comparisons
The comparison operators are `>`, `>=`, `<`, `<=`, `!=`, and `==`. When working with numbers, they do what you think: return `True` or `False` depending on whether the statement is true or false.  
  
*Note: Python2.x will let you try to compare any two objects, no matter how different. The results may not be what you expect. Python3.x only compares types where a comparison operation has been defined*
  
## Conditional Execution: The if Statement
The `if` statement is an important and useful tool. It basically says, "If a condition is true, do the requested operations."
```python
def even(n): 
	if (n % 2 == 0): 
		print('I am even!')
```
What if we want to be able to say we are not even? Or the user submitted a bad type? We use `else` and `elif` clauses.
```python
def even(n):
	if (type(n) != int):
		print('I only talk about integers')
	elif (n % 2 == 0):
		print('I am even!')
	else:
		print('I am odd!')
```

## Looping Behaviour
### The while Loop
The `while` is used for repeated operations that continue as long as an expression is true. The famous infinite loop:  
```python
while(2+2==4):
	print('forever')
```

### break and continue
For more control, we can use `break` and `continue` (they work just as in C). The break command will break out of the smallest while or for loop. The continue command will halt the current iteration of the loop and continue to the next value.

### The else clause
You can also have an else statement at the end of a loop. It will be run only if the loop completes normally, that is, when the conditional expression results in False. A break will skip it.

### The for Loop
The for loop is probably the most used control flow element as it has the most functionality. It basically says, "for the following explicit items, do something."
```python
for i in [1,2,3,4,5,’a',’b’,’c1]: 
	print(i)
```

### for Loop Fodder: range and xrange
The `range` function returns a list of values based on the arguments you provide. This is a simple way to generate 0 through 9:
```python
for i in range(10):
	print(i)
```

*Note: In Python3, the range function produces an iterator. For now, think of an iterator as an object that knows where to start, where to stop, and how to get from start to stop, but doesn’t keep track of every step along the way all at once. In Python2, xrange acts like Python3's range. range in Python2 produces a list, so the entire range is allocated in memory. You should almost always use xrange instead of range in Python2.*


