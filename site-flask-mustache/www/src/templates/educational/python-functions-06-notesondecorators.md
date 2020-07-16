This last section goes through some personal advice I'd like to share about where, when, and how often (or not) to use __decorators__ in your Python software development.

As the previous sections showed, decorators and wrappers add obfuscation that results in psuedo-transparent functions. It can seem clear, but really there are layers of abstraction that can be hard to follow in the moment. The last thing you want to do is introduce a decorator into a substantial codebase, cause a bug, and be unable to trace it due to too many abstractions and wrappers and convoluted aliases.

It's a good rule-of-thumb to always explicitly justify a wrapper. If there's no justification for its use, then question it. And if it doesn't hold up under scrutiny, you're probably better off removing it.

For example, I was once tasked to update and maintain a codebase that (among other things) overused the `@classmethod` decorator. In order to implement logging, a custom logger class was created and it was backhandedly injected into all other worker classes through an alias-shuffling registration by using `@classmethod` functions. We'll come back to this example, but essentially it was a convoluted reversal of the [Observer Pattern](https://en.wikipedia.org/wiki/Observer_pattern) code-design.

To clarify this, let's look at what the `@classmethod` decorator does. This decorator modifies class-methods (member functions of a class) such that when called they get passed their class, not the current instance, as their first unnamed ("positional") parameter.

Here's an example:

```python
class ExampleClass(object):
  name = "Example";
  label = None;
  def __init__(self, name, label):
    self.name = name;
    self.label = label;
    return (None);
  # fed
  @classmethod
  def print_default_name(cls,):
    print(cls.name);
    return (None);
  # fed
# ssalc
```

Now, as you can see, the `print_default_name` method was decorated and we changed the first parameter from the conventional `self` to `cls`. This wasn't arbitrary, we're now getting the class itself, not the current instance of the class (an object) when we call this method.

Arguably, the example above is perfectly valid and useful. However, the same functionality can be achieved without the `@classmethod` decorator by simply creating another variable to hold the default name external to the class. I'd argue that such an approach would be more readable and a lot simpler to follow.

```python
DEFAULT_NAME = "Example";

class ExampleClass(object):
  name = DEFAULT_NAME;
  label = None;
  def __init__(self, name, label):
    self.name = name;
    self.label = label;
    return (None);
  # fed
  def print_default_name(self,):
    print(DEFAULT_NAME);
    return (None);
  # fed
# ssalc
```

Or another approach:

```python
class ExampleClass(object):
  name = "Example";
  label = None;
  def __init__(self, name, label):
    self.name = name;
    self.label = label;
    return (None);
  # fed
  def print_default_name(self,):
    print(ExampleClass.name);
    return (None);
  # fed
# ssalc
```

Again, it's all a matter of preference and intention, but I'd suggest that the above two approaches are a lot easier to read/follow than the `@classmethod` version. These approaches also pass the current instance to the `print_default_name` method, which allows this code to be more easily extensible, and could arguably do more than the `@classmethod` version. For example, say that we wanted to reset the name to the default value instead of just printing it. That can't be done with the `@classmethod` version, but we can easily change the third version:

```python
class ExampleClass(object):
  name = "Example";
  label = None;
  def __init__(self, name, label):
    self.name = name;
    self.label = label;
    return (None);
  # fed
  def reset_name(self,):
    self.name = ExampleClass.name;
    return (None);
  # fed
# ssalc
```

Using `@classmethod` would have put the code into a design that would've required more redesign and may have been harder for someone unfamiliar with the code to figure how to get from there to here. There's often an overt implication among Software Engineers that can make others fearful to change the original code too much, even when adding a new feature or fundamentally changing the design. Especially when code is undocumented, it makes it harder for someone who comes along and needs to maintain or edit it. In the absence of any explanation, people may tend to err on the side of assuming that the original writer of the code knew what they were doing -- which isn't always true.

The goal should certainly be minimal code and minimal changes, but that should also measured by whatever is _most_ readable. The arguments for minimal code and minimal changes exist because if there's less code, it's easier to read, and if the changes between version-commits are minimal, it's easier to follow the evolution of the design. These things all exist _under_ the goal of __readability__, which should be first and foremost.

So, in this case, `@classmethod` is a roundabout (and possibly misleading) solution to a simple problem.

Getting back to the example I originally mentioned: in my circumstance, the code I was working on was originally written using `@classmethod` all over the place to avoid module-level logger singletons (single instance objects of a class), all in a convoluted design to share a logger across worker objects.

In this situation, it felt like a design that was copied from a simple online example that had all gotten a little out of hand. It certainly worked, _but_ not only was it difficult to read, it also led to some overzealous "consistency" where `@classmethod` got added where it wasn't even used or needed. And, in trying to create new worker classes that needed logging functionality, the ability to register a new class with a logger required a deep, esoteric understanding of the `@classmethod` convention _in situ_ that didn't really naturally lend itself to reusing shared-code by creating derived classes.

Obviously, every situation is going to be unique and different. I'm not saying _never_ use decorators, I'm just saying don't _always_ use decorators.

In one-off examples you'll find online you may notice people like using the `@property` decorator, since it collapses two methods into one, and reinforces encapsulation by using a get/set dual-purpose method instead of just "publicly" accessing and modifying class elements.

However, take that with a grain of salt, understanding a few key facts:

- There are no actual `public`, `private`, or `protected` attributes in Python classes.
- Getter and Setter methods are helpful when doing complex updates, but arguably direct access requires much less code.
- People giving code examples online are trying to be abstract, generic, and terse. A quick and simple example is more readable, but that inherently makes it unlikely to be ubiquitously practical. Your codebase is going to be specific and contrived to your purposes, and your two goals should be functionality and readability. If `@property` isn't helping really enhance either of those, then what benefit do you get from just copying it because it's what's shown everywhere online?

So, again, just because Python offers these decorators, that doesn't mean you _have_ to use them. In fact, I would say to err on the safe side and avoid them until you can do your own R&D and test them out and see what works for you and what doesn't.

___It's much easier to add decorators to extant code to gain functionality, than it is to remove decorators and maintain the same functionality.___

Lastly, I think it's fair to say that the decorator syntax is arguably unreadable without esoteric knowledge of Python. So, as soon as you start decorating your functions, you're going to need to document and justify why you're doing it. Otherwise, your code may end up being so terse that it becomes unreadable without consulting documentation and tracing the runtime, which kinda defeats half of the purpose of the code.

__Computers read and write binary numbers, _people_ read and write code__ -- so write your code to be read by a person, and don't try to outsmart the computer, or you're gonna have a bad time.

I hope this helps! Good luck!
