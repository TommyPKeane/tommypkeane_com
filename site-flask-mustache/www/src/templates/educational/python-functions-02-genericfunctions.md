<div class="card-header" id="id_header_genericfunctions">
  <h1>
    <button class="btn btn-link" data-toggle="collapse" data-target="#id_collapse_genericfunctions" aria-expanded="true" aria-controls="id_collapse_genericfunctions">
      Generic Functions (Overloading)
    </button>
  </h1>
</div>
<div id="id_collapse_genericfunctions" class="collapse hide" aria-labelledby="id_header_genericfunctions" data-parent="#GenericFunctions">

In compiled languages like C++, a function has a set number of arguments/parameters, known as being N-adic (or p-adic). A function of one variable would be monadic, for two variables its dyadic, and so on. This is known as the _adicity_ of a function.

In Python, there is no concept of __Function Overloading__, due to the way the interpreter was designed. In C++, for example, you can reuse a function's name and declare then define it with different sets of arguments. As long as the arguments are of distinguishable types, you can define many different "overloads" of a function, all with the same name. This has the benefit of allowing you to use the same function call but having it operate differently depending on the data-type of the arguments.

Here's a simple C++ example of an overloaded function:

```cpp
class PrettyPrinter
{
  public:
    void show_number(float const & x);
    void show_number(int const & x);
    void show_number(int const & x, int const & zeropads);
};
```

In the above example, we've declared (without defining) three methods of a PrettyPrinter class, but they all have the same name. However, since they all have different numbers/types of arguments, these are all overloaded methods for the `show_number()` method.

We could imagine that the bodies of these functions are all printing-out the `x` value differently depending on the data-type. Instead of trying to do type-matching based on coercion of a void-pointer within a single function body, this is a simple approach that lets the compiler choose which method to call. Without getting into the merits (or not) of this example, the basic takeaway should be that if we want to make a generic method in C++ (ignoring templates) we can instead create multiple overloaded versions.

In Python, we can't do the above because all elements are objects, and all objects are referenced by aliases. In essence, every "variable name" in Python is a pointer to an object (in C++ terminology). This means that any redeclaration of an alias would override all previous instances of the alias. So if we define three different versions of `show_number()` in Python, we only get the third one by the time the interpreter has finished reading the code.

The other obvious thing should be that since Python is implicitly typed, there's no need (or ability, depending on your Python version) to declare the type(s) of the argument(s) for a function. All function arguments are "passed by object-reference", which means that a "pointer" to the underlying memory instance tied to the alias is passed to the function. If the function uses object-methods to modify the aliased object, the original object will be modified out-of-scope. If non-object-methods are applied to the function argument alias, then the original object will be copied locally into the scope of the function and be modified in-place, leaving the original object untouched. This allows for passing by pointer or passing by reference (by copy), though it's much more "tacit"/implicit than in C++.

With all that said, it means that in Python, there are way fewer reasons to need to create overloaded functions in the first place. But, the remaining issue is how to deal with differing numbers of arguments and defaulted arguments. So let's go through those one-by-one.

First, we can actually call Python functions in one of 3 ways:

- Unnamed Arguments ("positional arguments")
- Named Arguments ("keyword arguments")
- Unnamed arguments followed by Named Arguments

To handle all three situations with a single alias, Python functions -- technically the `__call__()` method of all Python function-objects -- all support the following generically-innate syntax:

```python
def example_fnc(*unnamed_lst, **named_dct):
  # ...
  return (None);
# fed
```

The syntax we used above may seem unfamiliar, but the point was to highlight how the aliases themselves are inconsequential. You'll often see the same example function with this syntax:

```python
  def example_fnc(*args, **kw_args):
    # ...
    return (None);
  # fed
```

Both are exactly the same, and it's the asterisks that are doing all the work. A single asterisk collapses an iterable by one "level". Two asterisks will collapse an iterable by two-levels, essentially a dictionary (dict) object where there is a list of key-value pairs.


Note that for class-member functions, the dot-operator passes the current object as the first argument, so you can either use the above syntax and just be careful, or you can use the following syntax to make things a little simpler for yourself:

```python
class Example(object):

  def __init__(self,):
    return (None);
  # fed

  def example_fnc(self, *unnamed_lst, **named_dct):
    # ... code goes here ...
    return (None);
  # fed

# ssalc
```

Inside the body of the above function you have access to only two arguments, the unnamed_lst or the named_dct, but each of them can contain as many values as were called with the function.


Here's a simple example that you can use to print these collapsed containers to see what happens with the different calls below:

```python
def generic_test(*unnamed_lst, **named_dct):
  print("unnamed_lst:", unnamed_lst);
  print("named_dct:", named_dct);
  return (None);
# fed

generic_test();
generic_test(1, "hi", x=7);
generic_test(x=1, y="hi", z=7);
generic_test(1, "hi", 7);

generic_test(x=1, "hi", y=7); # SYNTAX ERROR
  # (Unnamed argument after a named argument.)
```

Here's an example of the output, so you can verify on your own:

```python
  >>> generic_test(1, "hi", x=7);
  unnamed_lst: (1, 'hi')
  named_dct: {'x': 7}
```

Now, a terrible way to use this functionality would be to never use named arguments, and just let anyone who calls your functions use whatever arguments they want, and then your function tries to suss-out what was given and why. That would be a nightmare for you and for anyone (including yourself) trying to use your function(s) later on. Beyond being just arguably unreadable, it would also mean that you're writing low-level C/Assembly-style code where you're recreating the concept of a function by trying to create a generic routine that _ad hoc_ determines its purpose. Possibly interesting as a dynamic programming problem, but it's gonna be a nightmare.


The real benefit to this syntax is that under certain circumstances, it allows for your code to accept arguments into a function when you won't know what those arguments are, because maybe you don't care.


Imagine writing the code for a "worker", a worker being someone who uses tools. Let's say the worker instance is somehow handed a tool and all tool instances have a `.use()` method. Now, what if all your workers are beholden to a Technical Manual, which describes the arguments to give to the `.use()` method for whichever tool is currently needed for the current step in the build process. Seems like in that situation, you could have a worker method like `.use_tool()` that's defined as such:

```python
  class Worker(object):

    toolkit = None;
    manual = None;
    cur_step = None;
    cur_tool = None;

    def __init__(self, toolkit,):
      self.toolkit = toolkit;
      return (None);
    # fed

    def set_manual(self, new_manual,):
      self.manual = new_manual;
      return (None);
    # fed

    def goto_next_step(self,):
      self.cur_step = self.manual.get_next_step();
      self.cur_tool = self.manual.get_tool(self.cur_step);
      return (None);
    # fed

    def use_tool(self, *args, **kwargs):
      self.cur_tool.use(**kwargs);
      return;
    # fed

    def do_task(self,):
      params_dct = self.manual.get_tool_params(self.cur_step);
      self.use_tool(**params_dct);
      return (None);
    # fed

  # ssalc
```

In the above, `params_dct` is a dictionary of key-value pairs, so by using the double-asterisk in a call, we're expanding the dictionary to a tuple of key-value paired arguments. In the `use_tool(*args, **kwargs)` definition, kwargs will be a dictionary that collapses (contains) any of the key-value paired arguments passed to the function. So then, to call the `.use()` method with the proper key-value paired arguments, we need to again use the double-asterisk to unpack/unzip the dictionary into the key-value paired arguments.


Yes, we took a dictionary, unzipped it, rezipped it, and then unzipped it again ... but not really. It's all just iterations and it's all being handled by the interpreter as optimized as possible. Arguably in this design the `use_tool()` method adds an extra step, but it also allows for use of tools handed to the worker instead of just those available through the internal manual. So in the example, we gain generic functionality by adding a couple extra lines that don't really affect the readability that much more.


The real benefit here is how simple/terse the code is but how generically it can be applied. We don't need to know what the arguments of the current tool are, we rely on the current step of the current manual to pass along that information through the `.get_tool_params()` method. This method could return a list or a dictionary and our method would still work as defined. The onus of coordination then becomes a burden only on the tools and the manuals. The worker is just the go-between.


This reduces redundancy, it tries to mitigate possible mismatches, and it will likely make the code much easier to read and to follow if there's a bug. Worst case scenario is that the tool parameters don't match the functionality of the tools usage method, so then that becomes a developer problem to figure out if they made a mistake in the tool or in the manual. If the worker has no say in the matter, then that eliminates them from the list of possible culprits for the bug.


This also means that tools and manuals can be updated and the worker(s) will always be able to keep up with the latest iterations. The workers themselves won't ever need to be "upgraded" so long as the manual is aligned with the tools.


Arguably, this syntax (while esoteric at first) can lead to a lot of really useful, generic, simple code like the above example. In the next sections you'll also see that this can be expanded further into wrapper-functions and decorators, doing essentially the same job of calling a function from inside another function _via_ pass-through of the alias.

</div>