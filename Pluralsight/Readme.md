## Python: Beyond Basics

### Beyond Basic Functions
 + Functions are First class , that is they are objects and can be passed on as any other objects

```
>>> import socket
>>> def resolve(host):
...     return socket.gethostbyname(host)
...
>>> resolve
<function resolve at 0x000001BC0F8D2E18>
>>> resolve('google.com')
'172.217.5.78'
```

 + `__call__()` :
  + Objects of our design to become callable , just like functions , these can be called using regular function call syntax
  + This is useful when we have a function which maintains state between calls and need to modify a state by querying that state
+ Classes are also callable in python

  ```python
  from resolver import resolver
  resolve = Resolver() #with the brackets, it is calling
  ```
+ lambda `lambda x: x.split()[-1]`
  + lambda returns a function object that is infact callable and we can bind a name through assignment
  + Expressions which evaluates to function
  + Anonymous
  + Argument list terminated by a colon, separated by commas
  + zero Arguments: lambda:
  + Body of lambda is a single expression
  + No return
  + No docstrings
  + Keep lambdas simple and not too complicated as they are Anonymous and cannot be called by names
```python
scientists  = ['Marie Curie', 'Albert Einstein', 'Niels Bohr', 'Isaac Newton', 'Dmitri Mendeleev',\
 'Antoine Lavoisier', 'Carl Linnaeus', 'Alfred Wegener', 'Charles Darwin']
 #scientists is the iterable
sorted(scientists, key=lambda name: name.split()[-1])
#['Niels Bohr', 'Marie Curie', 'Charles Darwin', 'Albert Einstein', 'Antoine Lavoisier', 'Carl Linnaeus', 'Dmitri Mendeleev', 'Isaac Newton', 'Alfred Wegener']
```

+ callable
 + String instances are not callable
```python
is_odd = lambda x:x%2!==0
```

+ Extended Argument syntax
  + Args is passed as a tuple
  + `*args`  -> positional arguments
  + `**args` -> keyword only arguments
```python
def extended(*args, **kwargs):
      pass
```
```python
def hypervolume(length, *length): # Better practice that just doing def hypervolume(*length):
      v=length
      for item in lengths:
        v*=item
      return v
```
```python
>>> def print_args(arg1, arg2, arg3, *args, kwarg1, kwarg2, **kwargs):
...     print(arg1)
...     print(arg2)
...     print(arg3)
...     print(args)
...     print(kwarg1)
...     print(kwarg2)
...     print(kwargs)
...
>>> print_args(1,2,3,4,5,kwarg1=6,kwarg2=7, kwarg3=8, kwarg4=9)
1
2
3
(4, 5)
6
7
{'kwarg3': 8, 'kwarg4': 9}
>>> def color(red, green, blue, **kwargs):
...     print("r=", red)
...     print("g=", green)
...     print("b=", blue)
...     print(kwargs)
...
>>> k={'red':21, 'green':68, 'blue':120, 'alpha':52}
>>> color(**k)
r= 21
g= 68
b= 120
{'alpha': 52}
```

+ Transpose operation here , Rows into columns and columns into rows
  + `list(zip(*table))` , zip* idiom , is very important
```python
>>> daily = [[12, 14, 15, 15, 17, 21, 22, 22, 23, 22, 20, 18],]
>>> daily = [[12, 14, 15, 15, 17, 21, 22, 22, 23, 22, 20, 18], [13, 14, 14, 14, 16, 20, 21, 22, 22, 21, 19, 17], [2, 2, 3, 7, 9, 10, 11, 12, 10, 9, 8, 8]]
>>> daily
[[12, 14, 15, 15, 17, 21, 22, 22, 23, 22, 20, 18], [13, 14, 14, 14, 16, 20, 21, 22, 22, 21, 19, 17], [2, 2, 3, 7, 9, 10, 11, 12, 10, 9, 8, 8]]
>>> for item in zip(*daily):
...     print(item)
...
(12, 13, 2)
(14, 14, 2)
(15, 14, 3)
(15, 14, 7)
(17, 16, 9)
(21, 20, 10)
(22, 21, 11)
(22, 22, 12)
(23, 22, 10)
(22, 21, 9)
(20, 19, 8)
(18, 17, 8)
>>> transposed = list(zip(*daily))
>>> from pprint import pprint as pp
>>> pp(transposed)
[(12, 13, 2),
 (14, 14, 2),
 (15, 14, 3),
 (15, 14, 7),
 (17, 16, 9),
 (21, 20, 10),
 (22, 21, 11),
 (22, 22, 12),
 (23, 22, 10),
 (22, 21, 9),
 (20, 19, 8),
 (18, 17, 8)]
>>> pp(daily)
[[12, 14, 15, 15, 17, 21, 22, 22, 23, 22, 20, 18],
 [13, 14, 14, 14, 16, 20, 21, 22, 22, 21, 19, 17],
 [2, 2, 3, 7, 9, 10, 11, 12, 10, 9, 8, 8]]
```

### Closures and Decorators
  +  `def` , defines the functions , functions are defined at runtime
    + A new function is created each time def is executed
    + `LEGB rule` : Local , Enclosing, global, Built-in
    + classes and functions are first class objects
  + Closure - maintain references to objects from earlier scopes
    + Python used this when using inner functions
    + `__closure__`
```python
    >>> def enclosing():
...     x='closed over'
...     def local_func():
...             print(x)
...     return local_func
...
>>> lf = enclosing()
>>> lf()
closed over
>>> lf.__closure__
(<cell at 0x000001DA363D52B8: str object at 0x000001DA366A2370>,)
```
  + `global` keyword to introduce the global namespace into the local namespace
  +  `nonlocal` introduce names from the enclosing namespace into the local namespace
  + These fundamentals are not that useful and they are not used on a daily basis, but is useful to understand the code
