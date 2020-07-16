Python treats everything as an object, but the interpreter has several short-hand keywords. For functions there is only one "kind" of function, so unlike C++ module-methods and class-methods are identically formed in Python. The scope of a function is what defines its accessibility, which means that there's also no such thing as "public", "private", or "protected" functions. All scoped elements are publicly accessible through the outer scope container.


So, as a short-hand (but the most common) syntax for creating a function, we use the `def` keyword and the colon (:) punctuation to establish a new scope (the function-body). All functions have at least one `return` statement, and if there is no explicitly written `return` statement then the interpreter will return a `None` whenever the function reaches the end of its scope.

Here's a simple function that prints "hello" and returns nothing:

```python
def say_hello():
   print("hello");
   return (None);
# fed
```

As mentioned, there's an implicit `NoneType` return, so here's an equivalent definition:

```python
def say_hello():
  print("hello");
# fed
```

Maybe instead of "hello" we want to print whatever string is given to the function, so let's change the first example to now take an argument:

```python
def say_something(msg_str):
   print(msg_str);
   return (None);
# fed

say_something("i'm giving up on you");
say_something("anywhere, i would've followed you");
```

Functions allow for two kinds of arguments:

- Unnamed ("positional")
- Named ("keyword")

The main usage restriction is:

___Unnamed arguments can not follow named arguments.___

Here's a function using several unnamed ("positional") arguments in the caller:

```python
def triple_add(x, y, z,):
   return (x + y + z);
# fed

w = triple_add(1, 2, 3,);
```

Here's that same function using named ("keyword") arguments in the caller:

```python
def triple_add(x, y, z,):
   return (x + y + z);
# fed

w = triple_add(
   x= 1,
   y= 2,
   z= 3,
);
```

Beyond readability, there are a few added benefits to using meaningful keywords for arguments in function definitions and calls.

One thing to note is that we can use the keyword syntax in the definition to establish a __default argument__, which simultaneously makes that argument optional (meaning that the default will be used unless the caller provides a new value):

```python
def triple_add(x, y, z=10,):
   return (x + y + z);
# fed

w = triple_add(
   x= 1,
   y= 2,
);

print("W:", w);
# W: 13
```

Another thing we can do is that since we're using named arguments, we don't need to put them in the same order as the definition when we call the function, because there's no ambiguity of which is which since we've explicitly used their names:

```python
def triple_add(x, y, z=10,):
   return (x + y + z);
# fed

w = triple_add(
   z= 20,
   y= 1,
   x= 2,
);

print("W:", w);
# W: 23
```

While this may not be entirely recommended all the time, we can also mix unnamed ("positional") and named ("keyword") arguments in the caller:

```python
def triple_add(x, y, z=10,):
   return (x + y + z);
# fed

w = triple_add(1, 2, z= 20,);

print("W:", w);
# W: 23
```

Usually, the above kind of mixed syntax is used when most of the arguments are meant to be unnamed but the final argument is some kind of flag or modifier that has a default and is being explicitly overwritten with the function call.

Again, the only restriction is that we can't put named arguments ___before___ unnamed arguments. This syntax is _invalid_ and will throw a `SyntaxError` (`positional argument follows keyword argument` will be the details).

```python
def triple_add(x, y, z=10,):
   return (x + y + z);
# fed

w = triple_add(x= 1, 2, z= 20,); # SyntaxError
```

Note that functions are generally scoped to a module, while "methods" are the name used for functions scoped to a class.

In a class, there's an implicit first argument that is unnamed and is colloquially called `self` by convention. Classes are often written as:

```python
class Calculator(object):
   def add(self, x, y,):
      return (x + y);
   # fed
   def subtract(self, x, y,):
      return (x - y);
   # fed
# ssalc
```

Again, `self` is just a convention and while it is generally recommended to use it for readability, you can name it whatever you like. Here's the same example, completely valid, but using `this` instead of `self`:

```python
class Calculator(object):
   def add(this, x, y,):
      return (x + y);
   # fed
   def subtract(this, x, y,):
      return (x - y);
   # fed
# ssalc
```

The `self` (implicit) argument is used to reference the _instance_ of the class that called the method. In that respect, it represents the current "state" of the object that called the method. As such, it's used to coordinate shared values across functions. This can be data that's common to the methods or something that is meant to be used in every method.

Given our above example, here's how you would create a `Calculator` instance and call the `subtract` method:


```python
class Calculator(object):
   def add(self, x, y,):
      return (x + y);
   # fed
   def subtract(self, x, y,):
      return (x - y);
   # fed
# ssalc

ti89 = Calculator();
z = ti89.subtract(3, 5,);

print(z);
# -2
```

If you create a module that has a function in it, you can import that module and then call that function using the `.` (dot) operator just like in the class example above.

Modules and Classes, in this respect, are like "Namespaces" used in C++.
