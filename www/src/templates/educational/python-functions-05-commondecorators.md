The Python Standard Library (PSL) actually has a few built-in, commonly-available decorators that are predefined without needing any imports.

Arguably, not all of these are generally useful, and you shouldn't just use a decorator for the sake of using it (see the next section). So, you may see code that overuses `@private` or `@property` or `@classmethod`, and you should ask yourself if it really was a good pattern and whether you should continue it or cull it.

That said, you can't make informed decisions without being informed, so let's introduce some common PSL decorators and some used by popular Python packages.

### Python Standard Library Decorators

These decorators don't require any imports and can be used in any of your code at any time. You can find the official documentation here in the [Built-in Functions](https://docs.python.org/3/library/functions.html) page.

#### `@classmethod`

The [`@classmethod`](https://docs.python.org/3/library/functions.html#classmethod) decorator modifies a method of a class so that the first "positional" (unnamed) argument is always the Class not the instance of the class, when called.

Conventional class methods look like this:

```python
class Example(object):
  name = "Example";
  def set_name(self, new_name,):
    self.name = new_name;
    return (None);
  # fed
  def show_name(self,):
    print(self.name);
    return (None);
  # fed
  def reset_name(self,):
    self.name = Example.name;
    return (None);
  # fed
# ssalc
```

As you can see, they all use (by convention) the `self` alias for their first argument, to indicate that they are accepting the instance of the class when called.

With `@classmethod` you could add a function print the default name (though this isn't the only way to do it):

```python
class Example(object):
  name = "Example";
  def set_name(self, new_name,):
    self.name = new_name;
    return (None);
  # fed
  def show_name(self,):
    print(self.name);
    return (None);
  # fed
  def reset_name(self,):
    self.name = Example.name;
    return (None);
  # fed
  @classmethod
  def show_default_name(cls,):
    print(cls.name);
    return (None);
  # fed
# ssalc
```

If you're familiar with C++, this is similar to a `static` method, such that it has access to the class instead of the instance -- as if it were shared "statically" between all instances. Arguably, the interpreter would only need to register one "instance" of the `show_default_name` method in memory and just let all instances of the `Example` class use it, because it's always the same definition no matter what the state of the `Example` instance is.

Because of that, you may see arguments for using `@classmethod` if you want/need to save memory. But be very careful that you don't over-zealously try to pre-emptively optimise by using `@classmethod`, because it's creating a fundamentally different kind of function. This is discussed more in the [Advice on Decorators](#DecoratorAdvice) section, on this page.

Without getting too far into it right now, just consider: in what way you could implement `reset_name` as an `@classmethod` decorated function?

Here's one way to do it, that you might agree is pretty gross to look at:

```python
class Example(object):
  name = "Example";
  def set_name(self, new_name,):
    self.name = new_name;
    return (None);
  # fed
  def show_name(self,):
    print(self.name);
    return (None);
  # fed
  @classmethod
  def reset_name(cls, obj,):
    obj.name = cls.name;
    return (None);
  # fed
  @classmethod
  def show_default_name(cls,):
    print(cls.name);
    return (None);
  # fed
# ssalc

a_obj = Example();
a_obj.show_name();          # "Example"
a_obj.set_name("A",);
a_obj.show_name();          # "A"
a_obj.reset_name(a_obj,);
a_obj.show_name();          # "Example"
```

Using `@classmethod` required us to write `a_obj.reset_name(a_obj,);` instead of just writing `a_obj.reset_name();`. This also made it so that we could do `a_obj.reset_name(b_obj,);`, which seems like a strange division of labor. True, this made each `Example` instance smaller in its memory footprint, but we run the risk of resetting the name of a different object than we intended.

Arguably, it leads to risky, hard-to-read code. So, it has its benefits, but since this is Python and not C++, we should probably be writing code differently, so that it's most functional and most readable, understanding that we're at the mercy of an interpreter, not a compiler, so there's only so much optimization to be gained.

Lastly, an important note from the official documentation:

_"If a[n `@classmethod` function] is called for a derived class, the derived class object is passed as the implied first argument."_

#### `@staticmethod`

The `@classmethod` decorator doesn't really provide the same functionality as a `static` method that you may be familiar with from C++ or Java. If you want a truly "static" method, the Python Standard Library provides the [`@staticmethod`](https://docs.python.org/3/library/functions.html#staticmethod) decorator.

Everything said about the `@classmethod` is still relevant, the only difference is that the `@staticmethod` does not provide any implicit "positional" (unnamed) argument when it's called.

Here's our `@classmethod` example:

```python
class Example(object):
  name = "Example";
  def set_name(self, new_name,):
    self.name = new_name;
    return (None);
  # fed
  def show_name(self,):
    print(self.name);
    return (None);
  # fed
  def reset_name(self,):
    self.name = Example.name;
    return (None);
  # fed
  @classmethod
  def show_default_name(cls,):
    print(cls.name);
    return (None);
  # fed
# ssalc
```

Here's how that would look if we changed `show_default_name` to be decorated as an `@staticmethod` function:

```python
class Example(object):
  name = "Example";
  def set_name(self, new_name,):
    self.name = new_name;
    return (None);
  # fed
  def show_name(self,):
    print(self.name);
    return (None);
  # fed
  def reset_name(self,):
    self.name = Example.name;
    return (None);
  # fed
  @staticmethod
  def show_default_name():
    print(Example.name);
    return (None);
  # fed
# ssalc
```

Again, this is basically the same as `@classmethod`, it's just that there's no implicit first argument.

As advice, we'd suggest you carefully consider if you really need an `@staticmethod` decorated class-method, or if your readability and extensibility would be helped by having a top-level module method instead. An `@staticmethod` can't manipulate an object or class unless they're passed to it explicitly, or are closure-scoped to it, so their functionality is arguably limited.

A benefit, though, would be if you want to provide a kind of namespace-scoped function that's available through access to a class or its instances. In this case, it'd make more sense (if possible) to use an `@staticmethod` on a base class, so it's available through all derived classes ("subclasses") and instances.

#### `@property`

There are actually two versions/approaches here. From [this documentation](https://docs.python.org/3/library/functions.html#property), you'll see that there is a built-in class called `property` whose `__init__` method takes four optional arguments: `fget` (function), `fset` (function), `fdel` (function), and `fdoc` (string).

So, not really as a classic decorator, but as an internal wrapper class for creating new member-object instances, we can do the following:

```python
class Vector(object):
  val_lst = [];
  def get_values(self,):
    return (self.val_lst);
  # fed
  def set_values(self, new_lst,):
    self.val_lst = new_lst;
    return (None);
  # fed
  def del_values(self,):
    del self.val_lst;
    return (None);
  # fed

  value = property(
    get_values,
    set_values,
    del_values,
    "This is the vector value array.",
  );
# ssalc
```

First, be sure to notice that `value` as created by `property` is a member-element of `Vector`.

Why not just use `val_lst`? Well, here's what the above syntax provides you the ability to do. First, you can now access the internal `val_lst` through the `get_values()` accessor method by simply calling:

```python
x = Vector();
x_value = x.value;
```

If you want to update the `val_lst` by using the setter, you can simply do the following:

```Python
x = Vector();
x.value = [1, 2, 3];
```

And if you wanted to permanently remove the `val_lst` from your instance, you just need to do:

```Python
x = Vector();
del x.value;
```

But, you might wonder, isn't this all the same as just doing:

```Python
x = Vector();
x.val_lst = [1, 2, 3];  # Set
x_value = x.val_lst;    # Get
del x.val_lst;          # Delete
```

Yup! You're right! It's exactly the same, _but_ through an extra couple layers of abstraction.

So, why would we want that?

Well, if you're familiar with Software Design from C++, you'll know that _encapsulation_ is a wonderful rule-of-thumb to follow to err on the side of safety and conformance for dealing with multiple-access issues and code-base coordination.

Accessing `val_lst` directly is arguably unsafe, because what if other methods are changing it or using it in ways that are specific to the class? You're basically circumventing the design of the class to reach in directly and change something willy-nilly.

If the class is designed really well and is substantially complex enough, it's likely that there's extra coordination and/or state-management that's happening through the accessor methods that you wouldn't be getting if you avoid using them.

Imagine a `Counter` class that keeps track of previously set values. Every time you `set` ("update") the count, its setter method could log the previous count before updating to the new one. This would provide you with a history, that could be great for graphing/plotting or using for statistical analyses. Logging data is hugely important in scientific, engineering, and computing applications, and by not using the designed code as intended, you risk circumventing (if not outright eliminating) that functionality.

So, creating the `set_...`, `get_...`, and `del_...` methods for elements in a class can be a great way to indicate an implicit "contract" of how to interact with instances of the class (the objects).

_But_, that's 2 or 3 functions (with/out `del`) for every publically accessible element, which can get pretty verbose pretty fast ... though that should be recognizable from C++.

So, that's often why you'll see lots of classes or derived classes, and lots of nuanced design in well-thought-out C++ codebases to try to make sure that you're not repeating yourself any more than is necessary, because the desirable functionality is already verbose enough as it is.

As the first example showed, the `property` constructor doesn't really save you anything in code you're writing when creating a class, but it certainly saves a lot of code for all the objects that use the new `value` element as an indirect accessor to the `val_lst` element.

But, we can also go one step further and use `@property` to save some code in the class, as well.

Here's that same example but a little less verbose:

```python
class Vector(object):
  val_lst = [];
  @property
  def value(self,):
    """Access this vector's value array."""
    return (self.val_lst);
  # fed
  @value.setter
  def value(self, new_lst,):
    """Update this vector's value array."""
    self.val_lst = new_lst;
    return (None);
  # fed
  @value.deleter
  def value(self,):
    """Delete this vector's value array."""
    del self.val_lst;
    return (None);
  # fed
# ssalc
```

We've made the code a little longer by adding documentation, but there's a few shortcuts you should notice. We've eliminated the need to call the `property` constructor, we don't need to create (perhaps convoluted) new names for each method, and we now have standardized `.setter` and `.deleter` syntax that may arguably be easier to follow than `fset`, `fget`, and `fdel`, for anyone new to this code.

It's honestly just a matter of preference in terms of which approach you'd use for defining class `property` instances, but there's a lot of readability benefit (in this case) to the `@<property_name>.<type>` syntax. Personally, I'd go with the decorator syntax, because I do find it much more readable and easier to maintain.

Be aware, though, that in terms of the naming, it's a shortcut and a _necessity_ to use the same function name for accessor-abstraction methods.

All the methods are now named `value` -- they're all the same. This is necessary to make the code work. Since we're no longer establishing a new element of the class to use as our public interface to adhere to our internal design "contract", we need all the function names to "represent" that public element. We'll usually have multiple `property` instances inside a class, so the only way to coordinate them with the `@` (decorator) syntax is to make sure the methods all have the same name.

Here's a class with two public accessor abstractions, to clarify that point (with a `Point`):

```python
class Point(object):
  e0 = None;
  e1 = None;
  @property
  def x(self,):
    """Access this point's x-value (e0)."""
    return (self.e0);
  # fed
  @x.setter
  def x(self, new_x,):
    """Update this point's x-value (e0)."""
    self.e0 = new_x;
    return (None);
  # fed
  @x.deleter
  def x(self,):
    """Delete this point's x-value (e0) by setting it back to `None`."""
    del self.e0;
    return (None);
  # fed
  @property
  def y(self,):
    """Access this point's y-value (e1)."""
    return (self.e1);
  # fed
  @y.setter
  def y(self, new_y,):
    """Update this point's y-value (e1)."""
    self.e1 = new_y;
    return (None);
  # fed
  @y.deleter
  def y(self,):
    """Delete this point's y-value (e1) by setting it back to `None`."""
    del self.e1;
    return (None);
  # fed
# ssalc
```

We could now, using some Python `tuple`-unwrapping syntax, do the following:

```Python
p0 = Point();

(p0.x, p0.y,) = (3, 7,);
```

Again, this is a trivial example that doesn't do anything special that you wouldn't get from just doing this instead:

```python
class Point():
  x = None;
  y = None;
# ssalc
```

That class has the exact same functionality, even without any methods, and this is still valid:

```Python
p0 = Point();

(p0.x, p0.y,) = (3, 7,);
```

So, the real deciding factor in using the `property` syntax should be if it's necessary or useful to your code. You get the functionality innately since all members of all classes are public.
