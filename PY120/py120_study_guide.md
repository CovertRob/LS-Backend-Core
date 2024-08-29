# PY129 Study Guide

## Classes and objects

- Instantiation and `__init__`
  - Instantiation is the process of creating a new object
    - Hiding data and functionality from the rest of the code base is known as encapsulation: accomplished with objects and interfaces (methods) in Python
    - init is frequently called the initializer or instance constructor
    - an object's Class() is the constructor
      - the constructor first calls the static method `__new__`
    - init is considered a dunder method

- Instance variables, class variables, scope
  - Instance variables keep track of information about the state of an object: each object's state is distinct
    - they exist as long as the object exists unless explicitly deleted
  - Class variables capture information abut a class: initialized in the main class body, NOT in an instance method
    - can be manipulated by both instance and class methods
    - want to use explicit class name to access them otherwise you get weird behavior, especially with counters
  - Object scope refers to the methods and instance variables an object can access
    - Two main components:
      - methods in the class: including inherited methods or mix-ins
      - instance variables associated with object: including those inherited

- Instance methods vs. class methods vs. static methods
  - Instance methods belong to the class: **They are not a part of the objects**, often also called behaviors
    - They are shared by the class and class instances can access those methods **Caveot: instance variables belong to the objects**
    - IOW: an object can only access its own state (instance variables)
  - Class methods use the special decorator `@classmethod`: they require at least one parameter `cls`
    - good practice is to invoke explicity with the class name
  - Static: they belong to a class but don't need access to any class or isntance attributes, provide utility services to the instance or class methods
    - uses `@staticmethod` decorator and no self or cls parameter
    - Example would be displaying a games rules to a player

- Attributes and state
  - Instance variables are variables that are tired to an instance of a class
  - Attributes include all instance variables and instance methods
  - Properties are their own special methods
  - State is defined by the data inside an object: from instance variables

- Calling and accessing instance, class, and static attributes: `self`, `cls`, `obj.__class__`
  - use the object instantiated or self internal to the class to access instance attributes
  - `GoodCat.what_am_i()    # I'm a GoodCat class!` for calling a class method
  - With an instance object that has a class object: can use `type(obj)`, `obj.__class__`, and even `obj` as the caller
    - Can also use self inside a method
    - DO NOT use `obj.classmethod()` syntax, you lose any indication it's a class method
  - For class variable use the explict class name and not the `self.__class__` or `cls.var` conventions
    - This gets tricky if you have subclasses using the same isntance variable (like counters)
  - Use class convention for calling static methods

~~~Python
  class Foo:

    @classmethod
    def bar(cls):
        print('this is bar')

    @classmethod
    def qux(cls):
        print('this is qux')
        cls.bar()

Foo.qux()
# this is qux
# this is bar
~~~

- Creating and using properties, getters, and setters

- Access control in Python: single and double underscore name conventions

- Encapsulation and polymorphism

## Inheritance

- Understanding `self` and `cls` with inheritance
- The `super()` function
- Mix-ins
- "is-a" vs. "has-a"
- The influence of inheritance on scope
- Method Resolution Order (MRO)

## The `is` operator and `id()` function

## Magic methods and attributes

- Custom comparison methods: `__eq__`, `__ne__`, `__lt__`, etc.
- Custom arithmetic methods: `__add__`, `__sub__`, `__mul__`, etc.
- Custom formatting methods: `__str__` and `__repr__`
- Attributes: `__class__` and `__name__`

## Exceptions

- What are exceptions
- Catching exceptions with `try`/`except`
- Raising exceptions
- The exception hierarchy (general; you don't need to memorize the hierarchy)
- Custom exception classes

## Working with collaborator objects

## Reading OO code

## Creating a code spike
