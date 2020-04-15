# Lesson 05: File Input and Output
  
Here are some key notes taken from this lesson which may help with the exercises.

## Introduction: Getting Dangerous
Input and output is a core tool in algorithm development and reading from and writing to files is one of the most common forms. 
```python
myfile = open('data.txt', 'w')
myfile.write(”I am writing data to my file")
myfile.close()
```
The variables you put into that `open` command are the filename(as a string -- do not forget the path) and the file *mode*. Here we are writing the file, as indicated by the `''w'` as the second argument to the `open` function. This actually returns something called a `file object`.  
_Danger: Opening a file that already exists for writing **will erase the original file.**_
  
There are only a few file modes which we need to use. You have seen `'w'` (writing). The others are `''r'` (reading), `'a'` (appending), `'r+'` (reading and writing), and `'b'` (binary mode).
  
A cool way to use contents of a file in a block is with the `with` command. Formally, this is called a context manager. Informally, it ensures that the file is closed when the block ends.
```python
with open('data.txt') as f:
	print(f.read())
```
Using `with` is a good idea but is usually not absolutely necessary. Python tries to close files once they are no longer needed. Having files open is not usually a problem, unless you try to open a large number all at once (e.g. inside a loop).

## Reading Lines From Files
Here are some useful methods for file objects:
```python
lines_file = open('fewlines.txt', 'w')
lines_file.writelines("first\n")
lines_file.close()

lines_file = open('fewlines.txt', 'r’)
lines_file.readline()
lines_file.close()

lines = open('fewlines.txt','r').readlines()
```
*Note: both read and readline(s) have optional size arguments that limit how much is read. For readline(s), this may return incomplete lines.*
  
But what if the file is very long and I don't need or want to read all of them at once, `file` objects behave as their own iterator.
```python
lines_file = open('fewlines.txt','r')
for line in lines_file:
	print(line)
```
The below syntax is a very common formula for reading through files. Use the `with` keyword to make sure everything goes smoothly. Loop through the file one line at a time, because often our files have one record to a line. And do something with each line.
```python
with open('fewlines.txt') as myfile:
	for line in my_file:
		print(line.strip()) # The strip function removes newlines and whitespace from the start and finish
```

## Moving Around with tell and seek
The `tell` method returns the current position of the cursor with in the file. The `seek` command sets the current position of the cursor within the file.
```python 
inputfile = open('data.txt', 'r')
inputfile.tell()
inputfile.read(4)
inputfile.seek()
```

## File-Like Objects
There are other times when you really need to have data in a file (because another function requires it be read from a file perhaps). But why waste time and disk space if you already have the data in memory? 
A very useful module to make a string into a file-like object is called `StringIO`. This will take a string and give it file methods like `read` and `write`.

```python
import io 
mystringfile = io.StringIO() # For handing bytes, use io.BytesIO
mystringfile.write("This is my data!")#
mystringfile.read()
mystringfile.seek(0)
mystringfile.read()
newstringfile = io.StringIO("My data")
```

Now let's pretend we have a function that expects to read data from a file before it operates on it. This sometimes happens when using library functions.
```python
def iprintdata(f):
	print(f.read())

iprintdata('my data')
my_io = io.StringIO('my data')
iprintdata(my_io)
```

