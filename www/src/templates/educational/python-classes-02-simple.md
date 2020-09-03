First, let's just make some simple, operational classes that provide generic functionality and show how the syntax works.

These aren't going to be great designs, and they aren't going to necessarily be super useful. But, sometimes, when you're just trying to do some prototyping or play around with the features of the language, it can be good to make simple, "ugly" classes that help you get the job done.

So first, let's just make a simple example of a `NameTag` class, where we construct it with a given name and then when we print the class, we use its `__str__` method to show the name.

```python
class NameTag(object):
  name = None;
  def __init__(self, myname):
    self.name = myname;
    return (None);
  # fed
  def __str__(self,):
    return (str(self.name));
  # fed
# ssalc
```

Super simple.

All classes in Python derive (implicitly) from the base-class called `object`, so, personally, out of explicitness, we like to just put this in the declaration to show what the base class is. You can leave it out, and nothing will change, because it will be added-in for you, by the interpreter.

We argue that the benefit of showing the base-class name is that it clarifies where a lot of the functionality of a Python class is coming from. It could help clarify what to search for in the documentation for anyone new to Python, and being implicit in Software Engineering just always feels like being on the wrong side of history. Someone's gonna look back on your code, including yourself, and if your crime is that it's overly-explicit and overly-well-documented, then that's probably not a bad thing.

_(Ignoring the fact that we didn't document this class ... for the sake of this article's already obliterated brevity.)_

Ok, so now our `NameTag` class exists, we have the pre-construction method (`__init__()`) and the string "conversion" method `__str__()`.

So let's put those two to use and make a couple objects and show what would happen if we pass them to the `print()` method:

```python
nametag_a = NameTag("What");
nametag_b = NameTag("Who");

name_intro = "Hi, my is";

print(name_intro, nametag_a);
# Hi, my name is What

print(name_intro, nametag_b);
# Hi, my name is Who
```

Perfect! Exactly what we said. We made a class, we used it to construct two new objects that we assigned aliases to, and then we used those aliases in some `print()` statements which called `str()` on each instance (object), which in turn called the internal `__str__()` method to do the conversion.

Let's just clarify a few things, to show what we've done.

What if we redefine the class and take away the `__str__()` method? 

```python
class NameTag(object):
  name = None;
  def __init__(self, myname):
    self.name = myname;
    return (None);
  # fed
# ssalc
```

What happens if we made the same objects and printed them all the same?

```python
nametag_a = NameTag("What");
nametag_b = NameTag("Who");

name_intro = "Hi, my is";

print(name_intro, nametag_a);
# Hi, my is <__main__.NameTag object at 0x11028e880>

print(name_intro, nametag_b);
# Hi, my is <__main__.NameTag object at 0x11023d970>
```

Blorp! What's all that??

So, `object`-derived classes __do not__ (by default) have a `__str__()` method, but they do have a `__repr__()` method.

The special method `__repr__()` refers to the object "representation", which is meant to be used to indicate the "unique" representation of the instance -- the object.

When there's no `__str__()` method, the fallback call is to use the result of the `__repr__()` method, to convert any object to a printable string. Since that method is defined in the `object` class, which is an implicit base-class to every custom and built-in class in Python, then every object has a `__repr__()` method, unless it's been explicitly deleted by you.

That's good, because that means everything can be printed.

The problem is that for most class, `__repr__()` isn't overridden, and the default version is used. The default, as you can see in the code listing above, just prints out the name of the class, scoped to wherever it resides, and then the hexadecimal memory address for the start of the object. That address makes it so that every representation will be unique for differing objects, and so that you as the developer can tell if your aliases are pointing at the same object or different ones. This is a very useful debugging tool.

However, a lot of people came to realize that since all Python class methods and members are public, we can override the `__repr__()` method, and actually a conventional way to override it has come-up.

Now, this isn't prescriptive -- you don't _have_ to do this, and there are reasons not to -- but, a common use for the `__repr__()` method is to construct and return a string that equates to the `__init__()` call that would reconstruct the current object.

Let's show an example with our `NameTag` class. So instead of creating a `__str__()` method, we're going to override `__repr__()` from `object` -- and remember that there's no special syntax for an override or reassingment of an alias (the last one to be defined wins!).

```python
class NameTag(object):
  name = None;
  def __init__(self, myname):
    self.name = myname;
    return (None);
  # fed
  def __repr__(self,):
    return (
      self.__class__.__name__
      + "(\""
      + self.name
      + "\")"
    );
  # fed
# ssalc
```

So now, let's just print just the objects, to see what `__repr__()` provides:

```python
nametag_a = NameTag("What");
nametag_b = NameTag("Who");

print(nametag_a);
# NameTag("What")

print(nametag_b);
# NameTag("Who")
```

Cool! As we said, this is a convention (not a rule) that you'll see a lot of code follow, where we use the `__repr__()` method to basically print out the valid Python code needed to recreate the current object.

The downside to this approach, is that now we can't see the memory address and find-out if we're looking at the same object or just multiple deep-copies of it. For debugging purposes, it would require extra work to find out something that we could've known explicitly.

So, again, this is a convention that some people use, but you don't have to copy the approach. If you're debugging issues of copied objects or losing track of your aliases, this could actually make things worse for you. But, if you're trying to provide a class that gives you a handy reference on how to recreate it, this can be a great way to do that. You could even go a few steps further and use keyword arguments in the printed-out "constructor" call to show what each argument means, and give yourself a bit of referential documentation in the process. There's a lot that could be done here. But that's the basics of how to construct and print a class.

Again, `__str__()` is called if it exists, but if not, then `__repr__()` will be called. Note that if you put objects into a primitive iterable like a `list` object, then call `str()` (or `print()`) on that list, the list's default behavior is to call `repr()` on the inner objects (which calls their `__repr__()` method, even if they have a `__str__()` method).
