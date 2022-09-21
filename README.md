# arg_repr.py
Get an exact representation of your function call arguments.
```python
from args_repr import myargs_repr

def function(*args):
    print(myargs_repr())
    
function(
    "banana",
    1337,
    [1, 2, 3, 4],
    object()
)
```
```console
$ python test.py

    "banana",
    1337,
    [1, 2, 3, 4],
    object()


```
This works by traversing the source code from the beginning of the function call (achievable by taking `f_lineno` from the caller frame) up until the closing paren.\
Although there are a lot of tests on test.py,
it's not perfect, so you're welcome to try and break the code - fix it - add tests - PR - ?? - profit.
