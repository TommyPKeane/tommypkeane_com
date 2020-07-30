Hiya!

On this page we provide some tutorials and examples about Object-Oriented Programming in Python, and how we can design and use classes.

Python is an interpreted language, so you can write code _"live"_ in a shell-like interface to the interpreter, or create scripts, or you can create your own well-organized modules and packages. At every "level" of complexity in the code structure, though, you're going to be highly dependent on classes and objects.

And if you want to get the most out of Python, and enhance or optimise your code for readability and reuse, you're going to want to design and create your own classes. And you're going to want to aim for terse, highly automated code.

We won't go so far as to say "no code is the best code" -- _that makes no sense_ -- but we will say that when you develop in Python, especially working with __classes__, you really _do_ want to be careful about not creating huge, huge classes.

If you find yourself doing a lot of the same thing, and typing a lot of code in Python, you really maybe should question if your design is lacking some editing.

Could a base class remove a lot of repeated functions?

Could you collect a lot of `@property` methods into sub-objects like a `dict` or `list`?

Do you have a lot of similar but unrelated classes? Could you use a "factory" class to create the code for you?

Is there something you're repeating in lots of functions? Could wrappers and decorators help? What about creating a "wrapper" class instead of passing around lots of objects to lots of functions?

Hopefully this page gives you some helpful examples and ramblings that can clarify how to get the most out of Python __classes__ as you develop your own code and software. Good luck!
