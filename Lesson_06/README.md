# Lesson 06: Development Environment and Tooling
   
Here are some key notes taken from this lesson which may help with the exercises.

## Package Management
**The Problem:** Python has a "batteries included" philosophy - it has a comprehensive standard library, but by default, using other packages leaves something to be desired:
- Python doesn't have a `classpath`, and unless you are root, you can’t install new packages for the whole system.
- How do you share a script with someone else when you don't know what packages are installed on their system?
- Sometimes you have to use ProjectA, which relies on a package that requires awesome-packagev.1.1, but you're writing ProjectB and want to use some features that are new in awesome-packagev.2.0?
- The best-in-class package manager isn't in the Python standard library.

## The Solution: virtualenv
The `virtualenv` package creates **virtual environments**, i.e. isolated spaces containing their own Python instances. It provides a utility script that manipulates your environment to **activate** your environment of choice. 
  
The `-p` flag indicates which Python executable to use as the base for the virtual environment:
```
$ virtualenv NEWENV -p /usr/local/bin/python
$ source NEWENV/bin/activate
$ deactivate
```

