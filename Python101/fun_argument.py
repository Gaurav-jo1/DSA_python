# By saying z = None, Now z is a optional argument.


def complicated_function1(x, y, z=None):
    print(x, y)
    pass


# What it does is accept any number of positional argumnets.
# We store them in a tuple - immutable
def complicated_function2(x, y, *args):
    print(x, y, args)
    pass


# **kwargs means we accept any key word arguments.
# They store in a dictionary
def complicated_function3(*args, **kwargs):
    print(args, kwargs)
    print(kwargs["x"])
    pass


def complicated_function4(*args, **kwargs):
    print(args, kwargs)
    pass


def complicated_function5(a, b, c=True, d=False):
    print(a, b, c, d)
    pass


complicated_function1(1, 4)
complicated_function2(1, 2, 5, 6, 2, 5, 1)
complicated_function3(x=1, z="Hello", b=True)
complicated_function4(1, 2, 4, 5, x=1, z="Hello", b=True)
complicated_function5(*[1,2 ], **{"c": "hello", "d": "cool"}) 