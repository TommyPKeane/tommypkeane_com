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
