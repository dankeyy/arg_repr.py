# arg_repr.py
Get an exact representation of your function call arguments.
```python
from args_repr import arg_repr

def function(*args):
    print(arg_repr())
    
function(
    "banana",
    1337,
    [1, 2, 3, 4],
    object()
)
```
```python
$ python test.py

    "banana",
    1337,
    [1, 2, 3, 4],
    object()


```
This works by carefully traversing the source code from the beginning of the function call (achievable by taking `f_lineno` from the caller frame) up until the closing paren.

So far my tests seem to pass. Please let me know if you encounter any issues.

New - added support for interactive mode, both ipython and regular repl. 

#### Note - multi lines repr is problematic for versions <=3.7 (old parser issue).
