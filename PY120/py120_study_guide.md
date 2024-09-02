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
  - Provides controlled access to an object's data
  - They fetch attribute values and setters update them
  - Can have a getter without a setter but can't have a setter without a getter
  - Properties decorators for getters and setters is a more pythonic way
  - Uses:
    1. access control and validation: prevent users from putting invalid data in the instance variables
    2. Computed attributes: computer attribute values on the fly based on other attribute values. Ex: radius, diameter, circumference, area
    3. Logging and other side effects: use side effects to alert a system administrator for example
    4. Refactoring: provide a property that is compatibly with old code, dollars and cents example
    <https://powerfulpython.com/blog/python-properties-refactoring/>
    5. Lazy evaluation: delay the computation of an attributes value until it's accessed. Ex: making a database query to retrieve a value
- Access control in Python: single and double underscore name conventions
  - Single leading underscore: marks instance variables and methods for internal use only
  - Two leading underscores causes name mangling: mangled names are formed by prepending an underscore and the class name to the unmangled name
- Encapsulation and polymorphism
  - Encapsulation: hiding data and functionality from the rest of the code base, defined above
  - Polymorphism (many - form): examples include the list function: it can take any iterable object as an argument. Tuples, ranges, sets, dictionaries, and even other lists

## Inheritance

- Understanding `self` and `cls` with inheritance
  - The name self is a convention: the first parameter for any instance method always represents the calling object, no matter what name you use
  - Same for cls: first parameter of a class method will always represent a class
  - Below we can see that because of inheritiance in `self.name`, `self` is still a Cat object

~~~Python
class Pet:

    def __init__(self, name):
        self.name = name

    def speak(self, sound):
        print(f'{self.name} says {sound}!')

class Cat(Pet):

    def speak(self):
        super().speak('meow')

cheddar = Cat('Cheddar')
cheddar.speak()
~~~

- The `super()` function: returns a placeholder object that acts like an instance of the current object's superclass (called a proxy object)
  - Super is actually a constructor for a class named super
  - Allows methods that override a superclass method to call the overidden method as part of its processing
  - Most common use is with `init` methods in subclasses
- Mix-ins: another way to achieve polymorphism
  - classes that are never instantiated
  - provide common behavior to classes that have no apparent hierarchy: an interface only -- a standard set of m ethods that can be used whenever needed
  - Key here is they are behavior based
  - They do not have `init` methods
  - It is polymorhpism because the classes that use the mixins can customize them to  how they need it by using way of multiple-inheritance
- "is-a" vs. "has-a"
  - "is-a" is shorthand for saying that the object referenced by var is an instance of the var's class
    - can subclass something: inheritance relationships should have an "is-a" relationship
    - If class A subclasses class B, then objects of type A must allso be usable as objects of type B
  - "has-a" is more suited for mix-ins and composition
    - composition: design principle where a class uses one or more objects of other classes to provide some of the composing class's functionality
      - also a form of collaboration: merely having an object inside the class isn't collaboration: at least one of the class's instance methods must use that object to aid the containign class's behavior
  - The idea of "has-a" over "is-a" is refered to as **Composition Over Inheritance**
- The influence of inheritance on scope: aids in what methods and instance variables an object can access
- Method Resolution Order (MRO)  : how python resolves where to look for a method
  - depth first search from left to right
  - if doesn't find the needed method, returns an `AttributeError`

## The `is` operator and `id()` function

- `is` checks for identity using the `id` function
- `is` and `id` determine whether the two variables point to the same object
- interning can affect these comparisons

## Magic methods and attributes

- Custom comparison methods: `__eq__`, `__ne__`, `__lt__`, etc.
- Custom arithmetic methods: `__add__`, `__sub__`, `__mul__`, etc.
  - define in pairs with arithmetic and augmented assignment operators
  - Limit the behaviors to those that are consistent with how the operators work with built-in classes
  - good practice to always define the pairsed `r` versions of the dunder methods
- Custom formatting methods: `__str__` and `__repr__`
  - see below for an example
  - When searching for `str` it searches for `str` first and then `repr` if it doesn't find `str`
    - Not the same for `repr`, it only searches for itself and won't defualt to `str`
  - both will default to `object.__str__` or `object.__repr__` if none defined
  
~~~Python
class Cat:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'Cat({repr(self.name)})'

cat = Cat('Fuzzy')
print(str(cat))  # Fuzzy
print(repr(cat)) # Cat('Fuzzy')
~~~

- Attributes: `__class__` and `__name__`
  - `name` returns the current module's name as a string
    - If current module is the program being run, `name` returns `main`
  - `__class__` is used to access a calling objects class

## Exceptions

- What are exceptions: an event that occurs during the execution of a program, disrupting its normal flow.
  - Can be caused by logical errors, invalid inputs, file not found, etc.
  - Built-in hierarchy of exceptions exists in Python

~~~Python
number = None
while True:
    number = input('Please enter a number: ')
    try:
        number = float(number)
        break
    except ValueError:
        print("Oops! That's not a valid number. Try again.\n")

print(f'Thanks! You entered {number}')
~~~

- Catching exceptions with `try`/`except`: see above example

~~~Python
try:
    foo()
except (AttributeError, ValueError, ZeroDivisionError):
    print('Got AttributeError, ValueError, or ZeroDivisionError')
~~~

- To access the exception object so you can use it or its attributes in the handler: add an `as` clause to the except statement

~~~Python
for value in ['abc', '0']:
    try:
        number = float(value)
        quotient = 3.0 / number
        break
    except ValueError as e:
        print("Oops! That's not a valid number.", e, '', sep='\n')
    except ZeroDivisionError as e:
        print('Oops! You tried to divide by zero!', e, '', sep='\n')
# Oops! That's not a valid number.
# could not convert string to float: 'abc'
#
# Oops! You tried to divide by zero!
# float division by zero
~~~

- `else` only runs when no exceptions have occurred
  - separating code into an `else` clause helps avoid catching unintended exceptions
- `finally` is used for cleanp actions that are performed regardless of whether an exception was raised or not
  - runs after the `try` clause or after any of the exception handlers
- Raising exceptions: used to throw exceptions in code
  - indicate error conditions that can't be easily corrected or with your own custom exceptions
  - use `from e` when chaining exceptions with `raise`

~~~Python
def convert_to_integer(value):
    try:
        return int(value)
    except ValueError as e:
        raise TypeError('Expected a numeric string') from e

try:
    convert_to_integer('abc')
except TypeError as error:
    print(f'Error: {error}')
    print(f'Original error: {error.__cause__}')
# Error: Expected a numeric string
# Original error: invalid literal for int() with base 10: 'abc'
~~~

- The exception hierarchy (general; you don't need to memorize the hierarchy)
  - At the top is `BaseException`
  - Then `Exception`: all the error and warning type exceptions inherit from `Exception`
    - `ArithmeticError`: OverflowError and ZeroDivisionError
    - `AttributeError`: eg mispelling an attribute name
    - `LookupError`: IndexError and KeyError
    - `OSError`: operating system related errors
    - `TypeError`
    - `ValueError`
- Custom exception classes
  - When creating custom exception types:
    - Always subclass from `Exception` or one of its subclasses
    - Name your exception class descriptively, with `Error` suffixing the name
    - Make sure the error messages are useful and clear, but let users override the message with their own
    - Example below
  
~~~Python
class ValidationError(Exception):
    def __init__(self, message="Invalid data"):
        super().__init__(message)
~~~

## Working with collaborator objects

## Reading OO code

## Creating a code spike

- Basically throw away code that serves as a framework until you fill it in

## 29AUG SPOT Session w/ Deepak

- Syntactical sugar on line 121
- super() is both a function and a location: it returns a proxy object which are used to call methods on the class

~~~Python
class Pet:
    _total_pets = 0

    @classmethod
    def total_pets(cls):
        return cls._total_pets

class Cat(Pet):

    
    def __init__(self, name):
        self.__class__._total_pets += 1
        # a_cat.__class__._total_pets += 1
        # Cat._total_pets += 1
        # Cat._total_pets = Cat._total_pets + 1
        # Cat._total_pets = Pet._total_pets + 1 (goes to Pet bc subclass relationship)
        # Cat._total_pets = 0 + 1
        Pet._total_pets += 1
        self._name = name
        print(super().total_pets())

class Dog(Pet):
    def __init__(self, name):
        self.__class__._total_pets += 1
        Pet._total_pets += 1
        self._name = name
        print(super().total_pets())

# what does this code output and why
a_cat = Cat('Cat1')         # 1

print(Cat._total_pets)      # 1
print(Pet._total_pets)      # 1

# a += 1
# a = a + 1

# b_cat = Cat('Cat2')      
# a_dog = Dog('Dog1')       
# b_dog = Dog('Dog2')       
# print(Pet.total_pets())   
# print(Pet._total_pets)     
# print(a_cat._total_pets)  
# print(a_cat.total_pets()) 
# print(b_cat._total_pets)  
# print(b_cat.total_pets()) 
# print(a_dog._total_pets)  
# print(a_dog.total_pets()) 
# instance object calls a class method, the CLASS OF THE INSTANCE gets passed in as the first argument, EVEN THOUGH the class method might be on a superclass.
~~~

- Instance Variable Access
- Class Variable Access
- Inheritance
- Mix-ins
- Collaboration
- Is-a vs Has-a
- MRO
- Polymorphism
- Encapsulation
- Magic methods
  - For Built-In Functions
  - For Comparison Operators
  - For Arithmetic Operators
- Exceptions
  - LBYL vs AFNP
