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

A virtual environment has the package manager `pip` pre-ihstalled, which can be hooked into the internal mirror of the Python Package Index (PyPi) by exporting the correct address to the `PIP_INDEX_URL` environment variable.
```
$ source NEWENV/bin/activate
$ pip install requests
```
```python
import requests
import sys

print(requests.__version__)
print(sys.path)
```

**Now we have a place to install custom code and a way to share it!**
- Develop code inside `~/NEWENV/lib/python2.7/site-packages`
- Capture installed packages with `pip freeze >> requirements.txt` and install them to a new `virtualenv` with `pip install requirements.txt`

## The Ultimate Package
`IPython` is an alternative interactive shell for Python with lots of cool features, among which are:
- tab completion,
- color output,
-rich history recall,
- better help interface,
- 'magic' commands,
- a web-based notebook interface with easy-to-share files, and
- distributed computing (don't ask about this)

```
$ pip install ipython
$ ipython

# To use the web interface, you have to install supplemental packages:
$ pip install pyzmq tornado jinja2 pygments
$ ipython notebook --no-mathjax

# Just two more packages are required to get awesome inline graphics
$ pip install numpy
$ pip install matplotlib
```

