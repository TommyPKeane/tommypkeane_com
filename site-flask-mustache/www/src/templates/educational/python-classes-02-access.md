If you're familiar with other Object-Oriented Programming-Languages, you may be expecting that Python would also have "access restrictions" for its member elements and functions.

By design, all members (data and functions) of classes are _public_ in Python.

One of the problems with public members in classes is that if you don't establish good practices and design patterns straight-away, you're going to run the risk of having derived classes that don't gain a lot of the polymorphic reduction in code duplication.

By design, you want to embed as much foundational functionality into the base class as possible, and then only relatively-incrementally add functionality in derived classes. The issue of using a public member instead of a public accessor-function, is that you risk missing-out on well-defined, encapsulted functionality that goes along with the accessor methods. Things like logging, scaling, and conversions all become much easier to handle through base accessor functions passed along to derived classes.

The following sub-sections talk about how to create "protected" and "private" members. This is _not necessary_ in Python, because they don't really truly do anything; but it can be good if you feel compelled to follow a C++ style approach and you want to obscure things, even just a little bit.

___Documentation is always the best way to convey a design contract___ in your software, but these stylistic conventions can of course be used in tandem with good documentation to make your code more readable and more "standardized".

## Protected Members

There is no such thing as a "protected" member in Python, though by convention it is suggested that protected elements be named with a single underscore as a prefix for the alias. Again, this does not actually "protect" the member from being accessed publicly. It's still accessible and modifiable through the dot operator on any class instance.

Here's a quick example to show this syntax convention:

```python
class Vector2D(object):
  _x = None;
  _y = None;
  def __init__(new_array):
    self._x = new_array[0];
    self._y = new_array[1];
    return (None);
  # fed
  @property.getter
  def x(self,):
    return (self._x);
  # fed
  @property.setter
  def x(self, x,):
    self._x = x;
    return (None);
  # fed
  @property.getter
  def y(self,):
    return (self._y);
  # fed
  @property.setter
  def y(self, y,):
    self._y = y;
    return (None);
  # fed
# ssalc
```

In the above design, we've created a custom class for a 2D Vector, which holds the `x` and `y` values as "protected" members `_x` and `_y`. Of course, we can still access the "protected" members however we want, but what the class design shows is a preferred "contract" for how developers should use the class. The `@property` decorators provide setter/getter access to `_x` and `_y` through the public accessors `x` and `y`. The idea should be that we leave `_x` and `_y` alone, and we really shouldn't need to touch them.

Again, they're not _actually_ "protected", but the underscore indicates that for developer purposes they should be treated as such. It's just a syntax convention, so you can follow it or not, but it tends to add extra readability by using a single underscore.

## Private Members

Now, despite the fact that all members are public by default, there is a "special" syntax that is supported by the interpreter to create "private" members.

Again, it's probably not surprising to find-out that these "private" members aren't actually private.

In this case, we prefix any alias that we want to treat as a private member by using double-underscores. Only as a prefix though. Remember, double-underscores as a prefix and suffic are specially reserved names that should only be established by the interpreter.

Once we create our "private" member-alias, the interpreter will do some alias-shuffling, similar to decorators, and actually create a new alias for us, based-on what we originally provide. In this way, if you look at the code as is, you'll see a member that starts with a double underscore but if you try to access it, it will be declared as "not found".

Let's recreate the same `Vector2D` class, and change `_x` and `_y` to "private" members `__x` and `__y`:

```python
class Vector2D(object):
  __x = None;
  __y = None;
  def __init__(self, new_array,):
    self.__x = new_array[0];
    self.__y = new_array[1];
    return (None);
  # fed
  @property
  def x(self,):
    return (self.__x);
  # fed
  @x.setter
  def x(self, new_x,):
    self.__x = new_x;
    return (None);
  # fed
  @property
  def y(self,):
    return (self.__y);
  # fed
  @y.setter
  def y(self, new_y,):
    self.__y = new_y;
    return (None);
  # fed
# ssalc
```

This new class is still valid because `__x` and `__y` can be used in our code within the definition(s) of the class, and it's only after the class is finalized by the interpreter, that the aliases are modified. This avoids and reference issues, but there's the esoteric nature of how "private" members are created.

As written we can actually call the following:

```python
vec = Vector2D([9, 3,],);

print("x:", vec._Vector2D__x)
# x: 9

print("x:", vec.__x)
# AttributeError: 'Vector2D' object has no attribute '__x'
```

As you can see, we actually have public access to a `_Vector2D__x` member, but when we try to access the `__x` member, per how we had originally written the class, it doesn't work.

What the interpreter did was take the original name `__x` and delete the original alias after re-assigning the member object to a new alias with a prefixed underscore followed by the name of the class.

The new alias format is created essentially with this code:

```python
exec(
  "vec" + "." + "_" + vec.__class__.__name__ + "__x"
  + " = vec.__x;"
);
```

If you wanted to undo the privatizing, you could call the following:

```python
exec(
  "vec.__x = "
  + "vec." + "_" + vec.__class__.__name__ + "__x;"
);
````

Note that we're using `exec`, not `eval`, because we are doing an assignment _statement_, not providing a standalone _expression_.

While this may not be useful, let's just go one step further and create a `deprivatize()` method that uses the object `__dict__` to find all members matching the "private" member alias pattern, and recreate their original aliases.

```python
import copy;

def deprivatize(obj):
  """Deprivatize the implicitly private member aliases of a class instance.
  We need to deep-copy the original object's member dictionary so that we
  don't step on our toes by trying to iterate through a dictionary that
  we are modifying in each iteration.
  """
  classname = obj.__class__.__name__;
  obj_dict = copy.deepcopy(obj.__dict__);
  for key in obj_dict:
    if (key.startswith("_" + classname + "__")):
      exec(
        "obj." + key[len("_" + classname)::1]
        + " = obj." + key + ";"
      );
    # fi
  # rof
  return (None);
# fed
```

And here's what you'll see if you use this method:

```python
vec = Vector2D([9, 3,],);

print(vec.__dict__)
# {'_Vector2D__x': 9, '_Vector2D__y': 3}

deprivatize(vec)

print(vec.__dict__)
# {'_Vector2D__x': 9, '_Vector2D__y': 3, '__x': 9, '__y': 3}
```

We  could update the `deprivatize()` method to be fancy and delete the "mangled" aliases as we go, to entirely undo the interpreter's alias-shuffling that's gone on, but this whole thing was just an illustrative example.

You should really have a reason to do this. If you don't like this aspect of Python, then the easiest option is to avoid using aliases in classes that start with double-underscore, and then you'll have really explicit code.

Personally, we find this whole alias shuffling thing to be a bit too much, and definitely too esoteric. For readability's sake, we would _not_ suggest using the double-underscore "private" aliases. It's probably going to cause more trouble than it's worth, especially since nothing really ends-up private anyways.

We would suggest you be explicit and document well. If you want to impose a design contract on your class, don't rely on the code to be "self-explanatory" -- it rarely ever is. You should always document any expectations for usage of the class, its members, and its methods, especially if you have certain design expectations. Even the `@property` decorator can be seen as optional by someone who doesn't like using it. So, it's good to establish a pattern, to show the usage explicitly, but also to document it.

Worst case scenario, someone doesn't read any of the documentation and they mess it all up. And if they complain that your code is broken, you can point to the documentation and provide the Manager's Mantra: "read the friggin' manual". No need to worry about what you know, as long as you know how to read, and it's been written down, then you're all set. So never skimp on the documentation.

_(Again, our code here is very very lacking in documentation, but that's only because there's so much rambling all around it, we need to make it clear and concise and so you're able to just copy-paste it into your interpreter and run it as is. The "production" version of this code would all be heavily documented, and should also have unit-tests to prevent feature regressions with any future development.)_
