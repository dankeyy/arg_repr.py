from arg_repr import arg_repr
import functools

def f(*args):
    return arg_repr()

eprint = functools.partial(print, end='\n---------------------\n')
eprint()

eprint(f("("))
eprint(f("\""))
eprint(f(r"\""))

eprint(f('get', 'rekt'))
got = rekt = 0
eprint(f(rekt, got))
eprint(f(""))
eprint(f("\\"))
eprint(f("a\\"))
eprint(f("\\a"))
eprint(f("    ("
         ))

cool = 2
eprint(f(cool))

eprint(f(x := 'banana'))

banana = 2
eprint(
    f(
        banana,
        lambda: 1,
        (lambda: 2)(),
        object(),
        1,
        2
    ),
)

def g():
    eprint(f(
    "from g scope"
            )
    )

g()

eprint(f(
    1,
        2
))


# some more sane tests
assert f("a\\") == r'"a\\"'
assert f("\\") == r'"\\"'
assert f("foo\"bar(") == r'"foo\"bar("', f("foo\"bar(")
assert f("(") == "\"(\"", f("(")
assert f("foo'bar") == "\"foo'bar\"", f("foo'bar")
assert f("foo\"bar") == r'''"foo\"bar"'''
assert f('foo\"bar') == r"'foo\"bar'"

def k():
    assert f(banana, 2) == "banana, 2", f(banana, 2)
    assert f(2) == "2"
k()


assert f((lambda: 1)())  == "(lambda: 1)()"
assert f((1,2, 3))  == "(1,2, 3)"
assert f( [1,2,3] )  == " [1,2,3] "
assert f("banana") == "\"banana\""
