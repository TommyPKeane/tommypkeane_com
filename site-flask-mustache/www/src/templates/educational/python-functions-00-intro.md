In Python, all elements are objects, such that functions are sometimes referred to as "first-class functions" or "first-class objects", indicating that they have a kind of primitive nature with respect to the interpreter (similar to numerical values).

Practically speaking, this just means that, as objects, functions are instances of a base Function class that has a `__call__()` method which overrides the parentheses operators. This means that functions can be managed by their alias (their "name") and can be selectively called.

Since a function can be selectively called, and the functions are objects themselves, then that means that the alias can be passed to other functions which can manipulate or call the functions through their base-class methods.

In Python, these functions that call other functions are known as "wrappers" or "decorators", with the `@` symbol being the short-hand decorator syntax supported by the interpreter. The short-hand notation saves a few lines of code, but it is extremely esoteric and hard to read when you're unfamiliar with the code.

This page gives some examples about how to read and write wrappers, decorators, and different kinds of functions. Feel free to contact us by email or on GitHub if you notice any issues, typos, or accidental misinformation. This page gives no guarantees, but is free to use for personal or professional education.
