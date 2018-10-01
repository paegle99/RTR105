Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, '__package__': None}
>>> __builtins__
<module '__builtin__' (built-in)>
>>> __builtins__.doc__

Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    __builtins__.doc__
AttributeError: 'module' object has no attribute 'doc__'
>>> __builtins__.__doc__
"Built-in functions, exceptions, and other objects.\n\nNoteworthy: None is the `nil' object; Ellipsis represents `...' in slices."
>>> print(__builtins___.__doc__)

Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    print(__builtins___.__doc__)
NameError: name '__builtins___' is not defined
>>> print(__builtins__.__doc__)
Built-in functions, exceptions, and other objects.

Noteworthy: None is the `nil' object; Ellipsis represents `...' in slices.
>>> a=10
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, 'a': 10, '__package__': None}
>>> a=20
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, 'a': 20, '__package__': None}
>>> b=1.56
>>> vars()
{'a': 20, 'b': 1.56, '__builtins__': <module '__builtin__' (built-in)>, '__package__': None, '__name__': '__main__', '__doc__': None}
>>> c='Q'
>>> vars()
{'a': 20, 'c': 'Q', 'b': 1.56, '__builtins__': <module '__builtin__' (built-in)>, '__package__': None, '__name__': '__main__', '__doc__': None}
>>> a*b
31.200000000000003
>>> c*C

Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    c*C
NameError: name 'C' is not defined
>>> a*A

Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    a*A
NameError: name 'A' is not defined
>>> a*a
400
>>> type(a)
<type 'int'>
>>> type(b)
<type 'float'>
>>> type(c)
<type 'str'>
>>> 
