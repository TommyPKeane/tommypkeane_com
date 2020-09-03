Before working with, and designing, Python __Classes__, it's important to have a clear understanding about __aliases__, __objects__, and the underlying design of the Python interpreter.

Python is a Dynamically-Typed, Object-Oriented, Interpreted Programming-Language where every "construct" is an object -- with "objects" being instances of "Classes".

In Python, there are no "variables", there are __aliases__. An __alias__ is the access-handle to a stored/accessible object in memory as managed by the Interpretor.

The Python interpreter is the `python` commandline application itself -- which is manageable through the importable `sys` (Python System) module.

In a statically typed language like C++, there are primitive types, custom types (classes), function pointers, and (data) pointers as the different kinds of variables. A C++ class creates a custom data type that can be used to create new variables ("objects") that can hold and interact with other data types.

In Python, everything is an object, everything is an instance of a class. But, all the __aliases__ are "dynamic", in the sense that they're not statically connected to the underlying memory. They're __aliases__ not _variables_. An __alias__ in Python can be reassigned to objects of different types without any type-casting. So, in Python when you create a new Class, you're not really defining a new data-type, you're defining a new blueprint for objects.

All Python methods are "generic" in the sense that they operate based on object-methods, not based on the types of the objects. All dyadic (two-argument) operators function as left-hand method calls. The left-side (first) argument is checked first to see if it has a method associated with the operator. There are a few "right-hand" methods, but these are only conditionally used by the interpreter under special conditions.

The process for the interpreter is such: if a dyadic operator doesn't have a corresponding method in the Class of the left-side argument, the right-side (second) argument is checked for whether or not it has a method associated with that operator. If it does, then the method is called, if not, then an error is raised because neither argument has a method to handle the operator. At no time is the "type" of either of the objects checked -- at least not in the way that you'd expect in C++.

The other sections on this page go further in-depth with examples and tutorials about how to create, manage, and use __Classes__ in Python. Since everything in Python is an object, __Classes__ are extremely meaningful and are a huge part of creating sensible, reusable code -- so we hope this information is helpful.

One thing you've probably heard about related to Object-Oriented Programming is "encapsulation" or "compartmentalisation", where it's suggested that well-designed code tries to "hide" the inner workings in reusable, inheritable classes. This is the optimal design approach in a language like C++, where you have to write a lot of code and you want to be able to interact with a lot of different layers and "modules" of your software, so you need to have a rational approach to internal coordination in the codebase.

We're not saying that doesn't apply to Python, but an important thing to keep in mind is that nothing is every really "out of reach" in Python. As long as there's an alias, everything is public in Python. And this changes the assumptions about how and why we design __classes__ the way that we do.

In Python, it's preferable to be terse and non-repetitive, especially because it's a high-level, interpreted language. We're further removed from the CPU, so we need to truly make sure we aren't trying to do the computer's job for it. We want to be thoughtfully sparing in how much code we write, because the more repetitious work can and should be done by the computer.

So, in Python, we really want to use __classes__ to reduce duplication, not necessarily to restrict access or tacitly enforce "contracts", as we would in C++, for example. Reducing code duplication in C++ is often handled by functions and templates, and even then we're often limited in how much we can hand-off to the computer.

By design, Python does _not_ supporting Templating like C++ does. Generic functionality is built into the language because none of the function calls (innately) do any type-checking, so there's no need to create C++-style templates that would otherwise generate multi-typed versions of the same code.

Note, though, that Python does support Multiple Inheritance, similar to C++, but due to the nature of aliases, Python does not suffer from the "Diamond Inheritance Problem".

All aliases in Python support overriding, while Python does not support overloading -- there's more about this in our [Python Functions](/educational/python/functions) article. Since all aliases will innately override, the "Diamond Inheritance Problem" is irrelevant, because whatever alias was inherited last, wins. Every time you redefine an alias, you're overriding any previous versions of it, so there's never any ambiguity, as long as you finish a complete Python statement.

Python, R, and C++ are more similar in their Object-Oriented designs than other languages like C, D, Lua, JavaScript, and go. That's important to keep in mind, because what's optimal here for Python isn't going to translate to these other languages.

Hopefully this page helps provide some clarity to Python __Classes__. The other sections have concrete coding examples to help, and you can always visit our GitHub account to access free, open-source software and coding examples in Python and other languages:

[github.com/tommypkeane](https://github.com/tommypkeane)
