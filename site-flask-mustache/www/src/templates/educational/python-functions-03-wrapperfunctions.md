Since Functions are objects in Python, the name of the function is actually the alias for the object.

Given this example:

```python
def add_special(x, y):
  return (x + y);
# fed
```

The name `add_special` is a registered Alias within the module ("namespace" / scope) where this function is defined.

This means that we can do things like:

```python
def add_special(x, y):
  return (x + y);
# fed

add_also = add_special;

>>> add_special(3, 5)
8

>>> add_also(3, 5)
8
```

As shown, we've created a new alias `add_also` that points to the same object as the original alias (function name) `add_special`.

The above example is mostly pointless, but something like that comes in handy if we were to create a module called `my_maths.py` with the following content:

```python
# @file
# @brief My custom Mathematics module
#
# @author Tommy P. Keane
# @email talk@tommypkeane.com

def add_special(x, y):
  return (x + y);
# fed
```

And in another module we can do the following:

```python
import my_maths;

new_add = my_maths.add_special;

z = new_add(3, 5);

print("z:", z);
# z: 8
```

By creating the new alias `new_add` we can simplify the in-module calls to `my_maths.add_special`, in case the code seems too verbose or the naming is hurting readability.

Arguably a more specific import could've been used like `from my_maths import add_special;`, but often for extensibility and readability in large codebases, it can be much more helpful to do a module import and then specifically call any methods or classes through the dot-operator.

The argument against such an approach is usually that if `add_special` gets renamed in the original module, every module that calls it will need a code-change everywhere it's used. By abstracting the call through the `new_add` alias, you could make it so that only the one line would need to be updated if `add_special` was renamed or replaced with an equivalent function.

Arguably, you could use this approach of creating new alias to a function when you use a placeholder function or some library that you're not sure of. In case the library doesn't work out, if the call signature is still the same, you could swap it out at that one line and all your code everywhere else would still work because it's all referencing `new_add`.

That's a bit of an aside, but this all introduces the abstraction that's at the heart of a __wrapper function__.

Wrapper Functions are functions which take other functions as arguments, and then call the functions that were passed-in.

In this example we create a function that adds two numbers, and then we create a wrapper function that will pre-print the arguments and post-print the result.

```python
def add_special(x, y):
  return (x + y);
# fed


def show_maths(math_func):

  def do_maths(x, y):
    print("x:", x);
    print("y:", y);
    z = math_func(x, y);
    print("z:", z);
    return (z);
  # fed

  return (do_maths);
# fed

show_add_special = show_maths(add_special);
```

The results of the two different calls would then look like this:

```python
>>> add_special(3, 5);
8

>>> show_add_special(3, 5);
x: 3
y: 5
z: 8
```

As you can see from above, `show_maths` returns a function alias that it created internally. This inner function calls the given function that was provided to `show_maths`.

With this design, the `show_maths` function is a "wrapper function", since it wraps around the inner `do_maths` and wraps around whatever function is provided as the `math_func` argument.

As you can see, the `math_func` is called with the arguments provided to `do_maths`, where `do_maths` is the return value of the `show_maths` function.

As such, this gives us the ability to do the following short-hand:

```python
def add_special(x, y):
  return (x + y);
# fed


def show_maths(math_func):

  def do_maths(x, y):
    print("x:", x);
    print("y:", y);
    z = math_func(x, y);
    print("z:", z);
    return (z);
  # fed

  return (do_maths);
# fed


z = show_maths(add_special)(3, 5,);


>>> print(z);
8
```

In the above example, we skip the extra alias of `show_add_special` and just let the interpreter order-of-operations play-out so that we call the return of `show_maths` with the arguments `3` and `5`.

Lastly, let's combine the wrapper function with the previous concept of a generic function.

Let's say that we don't know what the arguments are for a function, or we want something super generic. Instead of giving named/positional arguments for the inner-scoped function, we can use the generic `*` and `**` syntax to make something that we can use ubiquitously:

```python
def show_maths(math_func):

  def do_maths(*args, **kwargs):
    print("*args:", *args);
    print("**kwargs:", **kwargs);
    results = math_func(*args, **kwargs);
    print("results:", results);
    return (results);
  # fed

  return (do_maths);
# fed
```

The above is now able to be used generically with any `math_func` that takes any number of named (`*args`) or unnamed (`**kwargs`) arguments.

This obviously lacks some detail in the printouts, since it has to be generic, but this is just a simple example. In other implementations you could do all kinds of things using this approach, like opening and closing files or sockets around message-formatting functions, for example.
