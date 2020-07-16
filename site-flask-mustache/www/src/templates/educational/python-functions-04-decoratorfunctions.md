The previous section introduced Wrapper Functions in Python, which can actually be implemented in a slightly less-verbose manner using the __Decorator__ syntax and the `@` special-character.

In the __Wrapper Functions__ section we showed the following example:

```python
def add_special(x, y,):
  return (x + y);
# fed

def show_maths(math_func,):
  def do_maths(x, y,):
    print("x:", x,);
    print("y:", y,);
    z = math_func(x, y,);
    print("z:", z,);
    return (z);
  # fed
  return (do_maths);
# fed
 
showy_add = show_maths(add_special,);

z = showy_add(3, 5,);
```

In the above example, `show_maths` can now be used to "wrap" any extant dyadic-function by passing its alias, and will return a new dyadic-function alias that will print the arguments and then print the result, before and after running the function.

That basic wrapper syntax becomes extremely useful in just those kinds of situations where you want to do something before or after a function, repeatedly, and you want to centralize your code. Avoiding repetitious code and allowing the computer to repeat things for you is one of the tenets of good software development.

The only problem is that now you need to do extra alias wrangling. We had a perfectly good function name with `add_special`, but now we need to use `showy_add` to get the wrapper benefits. But what if we didn't want to have to deal with a new alias, and we just wanted to keep our original alias?

Not only does that mitigate the need to come up with all kinds of new function names -- and avoids the trouble of unimaginative people creating really gross function names -- that would also allow us to "secretly" modify extant functions with a wrapper that does ___not___ require any changes to the code that calls the function.

It's not really a "secret", but it allows us to basically inject functionality without having to change a lot of code. As long as things are readable or sensible, this is great. This could be used to wrap functions with logging features, as shown in the example, and not have to worry about going around changing the syntax of every call to the functions.

So how do we do this?

One "cheating" way to do this is to just cross-our-fingers and do some alias swapping:

```python
def add_special(x, y):
  return (x + y);
# fed

def show_maths(math_func,):
  def do_maths(x, y,):
    print("x:", x,);
    print("y:", y,);
    z = math_func(x, y,);
    print("z:", z,);
    return (z);
  # fed
  return (do_maths);
# fed

add_special = show_maths(add_special,);

z = add_special(3, 5,);
```

The sketchy thing about the above code is that we're reassigning the alias we originally created, so if we change that original alias we have to keep this new one up to date -- which honestly isn't a real burden, because you have to change everywhere that you called it, too.

A bigger concern is that if we get a little too clever, we risk dropping all references to the original function without properly deep-copying it, thus making the downstream alias invalid. This won't happen in a simple example like above, but if things get too complicated, you're at the mercy of the interpreter and making sure it knows what you meant to do.

Now, personally, I kinda like the above example because it's really blunt in terms of readability. Going from top to bottom, there's basically no question about what's happening -- it's all there. There's probably no real risk to using the above syntax, and worst-case you're a little extra verbose.

The __Decorator__ syntax is almost identical, except we now remove the need to do any alias shuffling, and instead we rely on the `@` character to be handled by the interpreter:

```python
def show_maths(math_func,):
  def do_maths(x, y,):
    print("x:", x,);
    print("y:", y,);
    z = math_func(x, y,);
    print("z:", z,);
    return (z);
  # fed
  return (do_maths);
# fed

@show_maths
def add_special(x, y,):
  return (x + y);
# fed

z = add_special(3, 5,);
```

For safety's sake (and readability's sake), we've rearranged the original example and defined the wrapper-function `show_maths` before our target function `add_special`. This is because we're going to use the `show_maths` decorator-syntax by putting `@show_maths` on the line directly above the `def` line.

Technically, as long as everything is at the same scope in the same module, we don't need to worry about the ordering, but I find it nicer to do it this way.

As you can see, we're now 1 line shorter, as we don't need to re-alias `add_special` because the `@` symbol is doing it for us, already.

The above examples are _identical_, so technically it's just a matter of preference / convention.

However, the `@` decorator syntax starts to come in handy when we start looking at generic methods, or wanting to pass arguments to the decorator (the wrapper-function).

Let's create a new wrapper-function that checks if either of the 2 arguments to a dyadic maths-function are evenly (_read:_ integer) divisible by `10`, and we'll start by using the syntax we know.

```python
def check_for_tens(math_func,):
  def do_maths(x, y,):
    if ((x % 10) == 0):
        print("x is evenly divisible by 10");
    # fi
    if ((y % 10) == 0):
        print("y is evenly divisible by 10");
    # fi
    z = math_func(x, y);
    return (z);
  # fed
  return (do_maths);
# fed
```

Now, let's say that we want to genercise (_"make generic"_) this function so that we can check for divisibility by whatever value is provided to the wrapper function.

Immediately, this poses a bit of an issue with the syntax as we've introduced it. The wrapper takes in a function and returns a function, and this is mandatory for using the `@` decorator syntax. So, how do we pass in a new variable `d` to be the divisor we want to test?

Here, the precedence order of operators for the interpreter comes into play. You can find precedence details in the official documentation -- [Python Operator Precedence](https://docs.python.org/3/reference/expressions.html#operator-precedence) -- but we'll summarise the important bit: parentheses `()` are called _before_ the decorator `@`.

That means that if we can wrap our wrapper in a function that takes our `d` argument, and return the wrapper function before using the `@`, then we can do this!

So let's rewrite `check_for_tens` as `check_for_divisor`:

```python
def check_for_divisor(d,):
    def check_for_divisor_wrapper(math_func,):
      def do_maths(x, y,):
        if ((x % d) == 0):
            print("x is evenly divisible by {0:d}".format(d,));
        # fi
        if ((y % d) == 0):
            print("y is evenly divisible by {0:d}".format(d,));
        # fi
        z = math_func(x, y,);
        return (z);
      # fed
      return (do_maths);
    # fed
    return (check_for_divisor_wrapper);
# fed
```

We can now use our new double-wrapper function as a decorator that takes an argument:

```python
@check_for_divisor(10,)
def add_special(x, y,):
  return (x + y);
# fed

>>> w = add_special(3, 25,);
""

>>> z = add_special(50, 35,);
"x is evenly divisible by 10"
```

This may all seem really obtuse, so let's go over it again.

From the above nested definition, we have 3 functions: `check_for_divisor`, `check_for_divisor_wrapper`, and `do_maths`. By then calling:

```python
@check_for_divisor(10,)
def add_special(x, y,):
```

We're saying:

1. Call `check_for_divisor` with the argument `10`, which returns `check_for_divisor_wrapper`.
1. Call the return (`check_for_divisor_wrapper`) function by passing in `add_special`.
1. Reassign the `add_special` alias to the return (`do_maths`).

So, to be clear, when we call `w = add_special(3, 25,)` we're _actually_ calling `w = do_maths(3, 25,)`, which has been updated to use `d = 10` internally thanks to the `@check_for_divisor(10,)` call.

Everywhere in our code, though, we'll only refer to `add_special`. Thus `check_for_divisor` "decorates" the `add_special` definition, which, itself, remains accessible in the code. This is why it's a decorator, not a wrapper or a replacement.

Lastly, you may be wondering what the implication is of this alias mess-about that we've done. Mostly, it's fine, but as we just said, we're _actually_ calling `w = do_maths(3, 25,)`, we've just re-aliased it. Fun fact, though, re-aliasing doesn't actually change the `__name__` member of a function object. The `__name__` is the alias that was used to originally define a function.

So, in this case we'll see that the `__name__` of `add_special` becomes `do_maths`, once it's decorated:

```python
@check_for_divisor(10,)
def add_special(x, y,):
  return (x + y);
# fed

print(add_special.__name__);
# "do_maths"
```

Arguably, this is a very good thing. This actually leaves behind a "receipt" indicating that `add_special` has been wrapped and re-aliased -- _a.k.a._, "decorated". But, this can pose a new problem. Look at the following situation:

```python
@check_for_divisor(10,)
def add_special(x, y,):
  return (x + y);
# fed

@check_for_divisor(10,)
def sub_special(x, y,):
  return (x - y);
# fed

print(add_special.__name__);
# "do_maths"

print(sub_special.__name__);
# "do_maths"
```

Ruh-roh, both functions now have the same `__name__`, because they're both calling the same function (though, it's different instances). But how can we have two instances of the "same" function? We don't. Functions that are defined within a function are known as being locally-scoped, _but_ as soon as we return the alias from the outer function, then that inner-function persists in memory for the lifetime of the interpreter runtime.

Every function call to the wrapper, thus, creates a new "instance" of the same function with the same characteristics. The `__name__` may be the same, but the memory addresses are different, indicating that they're different "instances". We can verify that by printing the `__repr__` as provided by calling `print()` on the alias:

```python
print(add_special);
# <function check_for_divisor.<locals>.check_for_divisor_wrapper.<locals>.do_maths at 0x1019b7ee0>

print(sub_special);
# <function check_for_divisor.<locals>.check_for_divisor_wrapper.<locals>.do_maths at 0x1019da040>
```

Whoa!? See? each `do_maths` instance is nested within the inner `<locals>` set of local-memory ("variables") within each of the nested wrapper functions. Ultimately though one is at (in my circumstances) address `0x1019b7ee0` and the other is at `0x1019da040`.

Now, since these are different "instances", this kind of poses a problem with the naming situation. It's not actually accurate to rely on the `__name__`, as is, under these circumstances. Sure, it tells us the alias of the original function name that's being called, but really, that's misleading because different instances could've been constructed with different parameters, and many things could be different. If we were trying to use the `__name__` to identify or compare callers, then we'd be in a state of ambiguity.

What would be really nice is if we could preserve the `__name__` of the wrapped function. Thankfully the `__name__` element is mutable! So let's just reassign it.

So we originally had:

```python
def check_for_divisor(d,):
    def check_for_divisor_wrapper(math_func,):
      def do_maths(x, y,):
        if ((x % d) == 0):
            print("x is evenly divisible by {0:d}".format(d,));
        # fi
        if ((y % d) == 0):
            print("y is evenly divisible by {0:d}".format(d,));
        # fi
        z = math_func(x, y,);
        return (z);
      # fed
      return (do_maths);
    # fed
    return (check_for_divisor_wrapper);
# fed
```

Now let's add a line to reassign the `__name__` before we return the function.

```python
def check_for_divisor(d,):
    def check_for_divisor_wrapper(math_func,):
      def do_maths(x, y,):
        if ((x % d) == 0):
            print("x is evenly divisible by {0:d}".format(d,));
        # fi
        if ((y % d) == 0):
            print("y is evenly divisible by {0:d}".format(d,));
        # fi
        z = math_func(x, y,);
        return (z);
      # fed
      do_maths.__name__ = math_func.__name__;
      return (do_maths);
    # fed
    return (check_for_divisor_wrapper);
# fed
```

Now what do we see?

```python
print(add_special.__name__);
# "add_special"

print(sub_special.__name__);
# "sub_special"

print(add_special);
# <function check_for_divisor.<locals>.check_for_divisor_wrapper.<locals>.do_maths at 0x1019b7ee0>

print(sub_special);
# <function check_for_divisor.<locals>.check_for_divisor_wrapper.<locals>.do_maths at 0x1019da040>
```

Success! Our `__name__` values changed. However, you can see that the `__repr__` values stayed the same. This is desirable and expected, though. We still are actually calling the inner `do_maths` "instances", and thankfully this gives us our "receipt" to show that. And, we now have differently "named" functions, so we can now reliably use the `__name__` as a means of identifying a function -- giving us the best of both situations.

And that's the basics of decorators.

Obviously we can genericise the inner or outer wrappers that take specific arguments, and we could namespace our wrappers by defining them as class methods instead of just being module methods, if we wanted. As class methods, we would get access to the object alias (`self`, by convention), so there's lots of options there for instancing and containing wrappers that have unique, controllable characteristics.

Before we finish, let's try something a little "wacky" ... let's see if we can make our divisor into an accessible, manipulable element by using a class-based wrapper.

```python
class MathsChecker(object):
    d = None;
    def __init__(self, d):
        self.d = d;
        return (None);
    # fed
    def set_divisor(self, d):
        self.d = d;
        return (None);
    # fed
    def check_for_divisor(self,):
        def check_for_divisor_wrapper(math_func,):
          def do_maths(x, y,):
            if ((x % self.d) == 0):
                print("x is evenly divisible by {0:d}".format(self.d,));
            # fi
            if ((y % self.d) == 0):
                print("y is evenly divisible by {0:d}".format(self.d,));
            # fi
            z = math_func(x, y,);
            return (z);
          # fed
          do_maths.__name__ = math_func.__name__;
          return (do_maths);
        # fed
        return (check_for_divisor_wrapper);
    # fed
# ssalc
```

Now let's create an instance, and use it to decorate a module method:

```python
maths_checker_obj = MathsChecker(10,);

@maths_checker_obj.check_for_divisor()
def add_special(x, y,):
  return (x + y);
# fed

>>> w = add_special(30, 5);
"x is divisible by 10"

maths_checker_obj.set_divisor(5);

>>> z = add_special(30, 5);
"x is divisible by 5"
"y is divisible by 5"
```

_Fantastico!_ We now have a dynamically configurable, decorated version of the `add_special` function. At any time, we can call `maths_checker_obj.set_divisor()` and this will change the decorations around `add_special`.

How would this be useful?

Imagine you had a logging class that provided a logging wrapper method that you wanted to establish as a decorator, but you wanted to make the logging-level user-configurable without having to restart the interpreter (the application). This way, you could have a `logger_obj.set_logging_level(...)` method that lets the logging-level dynamically change while the app still runs.

Readability definitely runs the the risk of being lost in all of this wrapping and re-aliasing, but if you choose meaningful function names and add in docstrings (unlike what I did here) -- do as I say, not as I do -- you should be able to gain a lot of functionality while avoiding a lot of repetition in your codebase.

It's perfectly valid, if not outright encouraged, to create a wrapper if you find yourself doing the same "thing" over and over again before or after a bunch of different functions.
