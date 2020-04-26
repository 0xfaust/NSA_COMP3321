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
  
Although we could add a `name` to each instance just after creating it,one at a time, wouldn’t it be nice to assign instance-specific attributes like that when the object is first constructed? The `__init__` function lets us do that. Except for the funny underscores in the name, it's just an ordinary function; we can even give it default arguments.

```python
class Person(object):
	species = "Homo sapiens"
	def __init__(self, name = "Unknown", age = 18):
		self.name = name
		self.age = age
	def talk(self):
		return "Hello, my name is {}.".format(self.name)
```
In Python, it isn't unusual to access attributes of an object directly, unlike some languages (e.g. Java), where that is considered poor form and everything is done through getter and setter methods. This is because in Python, attributes can be added and removed at any time, so the getters and setters might be useless by the time that you want to use them.
```python
mark.favorite_color = "green”
del generic_worker.name
```

One potential downside is that Python has no real equivalent of *private* data and methods; everyone can see everything. There is a polite *convention*: other developers are *supposed* to treat an attribute as private if its name starts with a single underscore(`_`). And there is also a trick: names that start with two underscores (`__`) are mangled to make them harder to access.  
The `__init__` method is just one of many that can help your class behave like a full-fledged built-in Python object. To control how your object is printed, implement `__str__`, and to control how it looks as an output from the interactive interpreter, implement `__repr__`. 

```python
def person_str(self):
	return "Name:{0}, Age:{1}".format(self.name, self.age)
Person.__str__ = person_str

def person_repr(self):
	return "Person('{0}’, {1})".format(self.name, self.age)
Person.__repr__ = person_repr
```
Take a minute to think about what just happened:
- We added methods to a class after making a bunch of objects, but `every` object in that class was immediately able to use that method.
- Because they were special methods, we could immediately use built-in Python functions (like `str`) on those objects.

Be careful when implementing special methods. For instance, you might want the default sort of the `Person` class to be based on age. The special method `__lt__(self, other)` will be used by Python in place of the built-in `lt` function, even for sorting. Even though it's easy, this is problematic because it makes objects appear to be equal when they are just of the same age!
  
While we've shown examples of adding methods to a class after the fact, note that it is rarely actually done that way in practice. Here we did that just for convenience of not having to re-define the class every time we wanted to create a new method. Normally you would just define all class methods under the class itself. If we were to do so with the `__str__` , `__repr__`, and `__eq__` methods for the `Person` class above, the class would like the below:

```python 
class Person(object):
	species = "Homo sapiens"
	def __init__(self, name = "Unknown", age=18):
		self.name = name 
		self.age = age
	def talk(self):
		return "Hello, my name is {}.".format(self.name)
	def __str__(self):
		return "Name:{0}, Age:{1}”.format(self.name, self.age)
	def __repr__(self):
		return "Person(,{0}' ,{l})".format(self.name, self.age)
	def __eq__(self, other):
		return self.age == other.age
```

## Inheritance
There are many types of people, and each type could be represented by its own class. It would be a pain if we had to reimplement the fundamental `Person` traits in each new class. Thankfully, **inheritance** gives us a way to avoid that. We've already seen how it works: `Person` inherits from (or is a **subclass** of) the `object` class. However, any class can be inherited from (i.e. have *descendants*).
```python
class Student(Person):
	...

```
An object from the subclass has all the properties of the parent class, along with any additions from its own class definition. You can still easy to override behavior from the parent class easily --just create a method with the same name in the subclass. Using the parent class's behavior in the child class is tricky, but fun, because you have to use the `super` function.
```python
class Employee(Person):
	def talk(self):
		talk_str = super(Employee, self).talk()
		return talk_str + "I work for {)".format(self.employer)
```
The syntax here is strange at first. The `super` function takes a `class` (i.e. a `type`) as its first argument, and an object descended from that class as its second argument. The object has a chain of ancestor classes. The `super` function goes through that chain and returns the class that is after the one passed as the function's first argument. Therefore, `super` can be used to skip up the chain, passing modifications made in intermediate classes.  As a second, more common (but more complicated) example, it's often useful to add additional properties to subclass objects in the constructor.
```python
class Employee(Person):
	def_init_(self, name, age, employer):
		super(Employee, self)._init_(name, age)
		self.employer = employer
		def talk(self):
			talk_str = super(Employee, self).talk()
			return talk_str + "I work for {}".format(self.employer)
```
A `class` in Python can have more than one listed ancestor (which is sometimes called *polymorphism*). We won't go into great detail here, aside from pointing out that it exists and is powerful but complicated.
```python
class StudentEmployee(Student, Employee):
	pass
```
