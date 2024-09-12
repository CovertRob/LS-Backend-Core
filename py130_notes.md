# PY130 Notes

## First-class object (aka first class citizen)

Meets the following conditions:

1. Can be assigned to a variable or stored in another object
2. Can be passed as an argument to a function
3. Can be returned as the return value of a function

- Includes: numbers, strings, lists, sets, all other data types, and classes, functions, and methods

## Higher-Order Functions

1. **expect** one or more functions as arguments
2. return a function

- **All Python functions are first-class functions, but only some are higher order functions**

## Callback Functions (callbacks)

- Functions that get passed to another functions, provided the called functions intends to invoke the call back under certain conditions
- If called function does not invoke the argument, then its not a callback

~~~Python
# callback
def foo(callback, my_list):
    for element in my_list:
        callback(element)

# non-callback
def foo(func, my_list):
    return {
        'func': func,
        'list': my_list.copy(),
    }
~~~

- No special name for functions returned by other functions

## Functions and Methods as First-Class Objects

### Functions as Variables

- Common practice to create aliases for long functions names:

~~~Python
def i_have_such_a_long_and_annoying_name(value):
    print(value)

too_long = i_have_such_a_long_and_annoying_name
too_long('Some text')
too_long(3.141592)
too_long('Some text' == 3.141592)
~~~

### Functions as Arguments

- transformation with the map function
- Imperative approach: (step by step)

~~~Python
numbers = [1, 2, 3, 4, 5]
transformed_numbers = []

for number in numbers:
    square = number**2
    transformed_numbers.append(square)

print(transformed_numbers)     # [1, 4, 9, 16, 25]
~~~

- with map, declarative approach:
- "We want to map (or transform) each element of the numbers list to a new collection by using the square function to transform each value."

~~~Python
def square(number):
    return number**2

numbers = [1, 2, 3, 4, 5]
transformed_numbers = map(square, numbers)
print(list(transformed_numbers))     # [1, 4, 9, 16, 25]
~~~

- same thing with filter function:

~~~Python
def even(number):
    return number % 2 == 0


numbers = [1, 2, 3, 4, 5]
even_numbers = filter(even, numbers)
print(list(even_numbers))     # [2, 4]
~~~

- Defining our own map function to demonstrate how to write a function that takes a function as an argument

~~~Python
def my_map(callback, iterable):
    return [callback(element) for element in iterable]
~~~

### Functions as return values

- Frequently used with lambda

## Lambda Functions

- Syntax: `lambda argument1...argumentN: expression`
- Several restrictions:
  - Expression is limited to a single expression
  - No assignments, loops, if statements, or any other statements allowed
  - Docstrings are not allowed
  - Difficult to debug since they don't have names that would otherwise appear in error messages
  - Don't permit `*args` and `**kwargs` parameters
- Examples:

~~~Python
square = lambda number: number**2
hello = lambda: print('hello')
add3 = lambda num1, num2, num3: num1 + num2 + num3

numbers = [1, 2, 3, 4, 5]
transformed = map(lambda number: number**2, numbers)
print(list(transformed))    # [1, 4, 9, 16, 25]

strings = ['cat', 'dog', 'bird', 'fish']
transformed = map(lambda string: string.upper(), strings)
print(list(transformed)) # ['CAT', 'DOG', 'BIRD', 'FISH']

numbers = [1, 2, 3, 4, 5]
selected = filter(lambda number: number % 2 == 0, numbers)
print(list(selected))    # [2, 4]
~~~

- using `for_each` in todo allows us to provide more encapsulation: encourage use of the interaces (public methods)

## Generators

- Generator expression: creates a generator, look like list comprehensions but they use parentehses instead of square brackets
  - Note that you can't have a tuple comprehension b/c comprehensions create mutable collections and tuples are immutable

~~~Python
[number for number in range(5)]     # list comprehension
(number for number in range(5))     # generator expresion
~~~

- Each element of a generator is created only when the program requests an element
- **Generators are single-use iterables**: meaning if you run the below it will only output squares once

~~~Python
>>> squares = (number**2 for number in [1, 3, 7, 11])
>>> for square in squares:
...     print(square)
...
1
9
49
121
~~~

- You can split the generator into two parts if you don't use all of its values at once
- Single-use also applies when passing to a list or tuple constructor
- Cannot determine the number elements to be produced by a generator

~~~Python
print(len((char.upper() for char in 'launch')))
#TypeError: object of type 'generator' has no len()
~~~

- Must parenthese close a generator expression if multiple arguments to a function

### Generator functions

- Generator functions use the `yield` keyword instead of return
  - `yield` passes a value outside of the function but instead of exiting it merely suspends the execution of the function

~~~Python
def count_up_to(max_count):
    count = 1
    while count <= max_count:
        yield count
        count += 1

counter = count_up_to(5)
for number in counter:
    print(number)
~~~

- Python knows that the above is a generator object b/c it contains yield, so it returns a generator object when invoking it
- Explanation of above process:

1. count is initialized to 1.
2. count is compared to max_count (5).
3. if count <= max_count:
  The current value of count (1) gets yielded to the for loop.
  The for loop sets number to the yielded value (1).

- On the next iteration of the for loop:

1. Execution of count_up_to resumes immediately after the yield statement.
2. count is incremented by 1 giving it a value of 2.
3. count is compared to max_count (5).
4. if count <= max_count:
  The current value of count (2) gets yielded to the for loop.
  The for loop sets number to the yielded value (2).

This process repeats until the final value represented by the generator function has been yielded to the for loop:

1. Execution of count_up_to resumes immediately after the yield statement.
2. count is incremented by 1 giving it a value of 6.
3. count is compared to max_count (5).
4. is count <= max_count: NO
5. Exit the generator.

- In short, the generator yields 1, 2, 3, 4, and, finally, 5 to the for loop. After yielding 5, the generator has run out of values to yield, so the generator exits.

### Next function

- Can use the next function to step through the values produced by a generator one at a time

~~~Python
>>> def count_up_to(max_count):
...     count = 1
...     while count <= max_count:
...         yield count
...         count += 1
...
>>> counter = count_up_to(5)
>>> next(counter)
1
>>> next(counter)
2
>>> next(counter)
3
>>> next(counter)
4
>>> next(counter)
5
>>> next(counter)
StopIteration # Python does not catch StopIteration exception when using next (it usually does otherwise)
~~~

### Why generators

- When processing large datasets: so you don't have to hold in memory all at the same time
- When integrating with functions that work with iterators, such as `sum`, `min`, `max`, `all`, and `any`

~~~Python
numbers = [1, 2, 3, 4]
sum_of_squares = sum(x**2 for x in numbers)
print(sum_of_squares)     # 30
~~~

## Files

- Files include:
  1. program files
  2. image files
  3. spreadsheets
  4. word processor documents
  5. commands you run at the command line
  6. your application

- `open` returns a file object that can be iterated over
- Can use the following methods:
  - `read()`
  - `readline()`
  - `readlines()`
- Using a for loop for each line is generally preferred over the above methods
- Always close a file when done with it to save resources

~~~Python
with open('example.txt', 'r') as file:
    for line in file:
        print(line)
~~~

- Use the above convention to open a file and automatically close it (done by with after it reads it in)
- `with` is known as a *context manager*: special kind of construct designed to allocate and release resources

~~~Python
try:
    with open('example.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print('The file does not exist')
~~~

- Best to use try/accept blocks such as above when opening files

## Keyword arguments

- All positional arguments must be specified before the first keyword argument
- If all arguments passed as keyword arguments, order does not matter
- You can ensure arguments are positional-only by using a slash:

~~~Python
def greet(name, /, color=None):
    if color:
        print(f"Hello {name}. Your favorite color is {color}.")
    else:
        print(f"Hello {name}. You don't have a favorite color.")

greet("Pete") # Hello Pete. You don't have a favorite color.
greet("Max", color="blue") # Hello Max. Your favorite color is blue.
greet(color="blue", name="Max") # TypeError
greet(name="Srdjan") # TypeError
~~~

- The slash says that all arguments before this slash must be "positional"
- Add an asterisk before the first parameter we want to be keyword only to achieve the same for keywords:

~~~Python
def greet(name, /, *, color=None):
    if color:
        print(f"Hello {name}. Your favorite color is {color}.")
    else:
        print(f"Hello {name}. You don't have a favorite color.")

greet("Pete") # Hello Pete. You don't have a favorite color.
greet("Max", color="blue") # Hello Max. Your favorite color is blue.
greet("Max", "blue") # TypeError
~~~

- This declares all arguments following color must be named
- Place * at beginning to make function accept only keyword arguments

### Any number of positional arguments

~~~Python
def greet_all(*names):
    for name in names:
        print(f"Hello, {name}.")

greet_all("Chris", "Pete", "Nick")
# Hello, Chris.
# Hello, Pete.
# Hello, Nick.
~~~

- The asterisk before it means `names` becomes a tuple containing all the arguments passed to the function
  - Often named *args

~~~Python
def say_pets(name, **pets):
    print(f"{name} pets are...:")
    for name, animal in pets.items():
        print(f"{name}, a lovely {animal}.")

say_pets("Pete", Cocoa="cat", Cheddar="cat")
# Pete pets are...:
# Cocoa, a lovely cat.
# Cheddar, a lovely cat.
~~~

- You can do the same with `**kwargs` for keyword arguments
- `**pets` tells Python to accept any keyword argument given and to store them in a dictionary
- `*args` must come after all positional arguments

~~~Python
def custom_func(x, y, *args):
    pass

custom_func(1, 2)          # args points to an empty tuple
custom_func(1, 2, 3, 4, 5) # args points to a tuple (3, 4, 5)
custom_func(1)             # raises a TypeError
~~~

- You can place an argument after `*args`, but it must be a keyword argument
- This means `**kwargs` must come after `*args`
  - Cannot define any parameters after `**kwargs`

## Unpacking iterables

- The `*` operator tells Python that the element following it is an iterable
  - Python then iterates over this iterable, passing each element as a separate argument to the function
- You can also unpack into variables like so:
`names = ("Chris", "Pete", "Nick")`
`chris, pete, nick = names`
- Can also do nested unpacking

~~~Python
data = ["apple", (8, 3, 7), 42]
fruit, (x, y, z), answer = data
print(fruit, x, y, z, answer)      # Outputs: apple 8 3 7 42
~~~

- **You get an error if too many or not enough matched variables to unpack all items**
- The fix is extended unpacking: use an asterisk * to assign a list with an arbitrary number of elements

~~~Python
names = ("Chris", "Pete", "Nick", "Brandi", "Clare")
chris, pete, *remaining_names = names
print(remaining_names)        # ['Nick', 'Brandi', 'Clare']
~~~

- Can do extended unpacking instead of slicing as well

~~~Python
numbers = [10, 50, 20, 30, 40, 60, 70]
start = numbers[0:-1]
last = numbers[-1]
#or
numbers = [10, 50, 20, 30, 40, 60, 70]
*start, final = numbers
print(start)        # [10, 50, 20, 30, 40, 60]
print(final)        # 70
#and...
numbers = [10, 50, 20, 30, 40, 60, 70]
first, second, *middle, last = numbers
print(first)        # 10
print(second)       # 50
print(middle)       # [20, 30, 40, 60]
print(last)         # 70
~~~

- You cannot use multiple *variables in an assignment

## Closures

- Variables that  are used within the inner function but are not local to it are known as free variables
  - Free variables are bound to the objects that were assigned those variables when closure was created - even after the outer function finished execution

~~~Python
def create_greeting():
    greeting = 'Hello'

    def display_greeting():
        print(greeting)

    return display_greeting

greet = create_greeting()
greet()  # Output: Hello
~~~

- The crucial point here happens when create_greeting returns display_greeting
- Usually, when a function completes execution, its local variables are discarded
  - However, since display_greeting is a closure, it captures and retains a reference to the object assigned to the greeting variable from the create_greeting environment
  - Thus when `greet` is called, it still has access to `greeting`
- Python uses a mechnism called a cell to store the values of variables that are used by closures
  - You can access the memory address of this cell object (an intermediary object) using the `__closure__` property

~~~Python
def create_greeting():
    greeting = 'Hello'
    print(hex(id(greeting))) # 0x1010114b0

    def display_greeting():
        print(greeting)

    return display_greeting

greet = create_greeting()
print(greet.__closure__)
# (<cell at 0x100feb070: str object at 0x1010114b0>,)
~~~

- The second print the first value is the memory address of the cell object and the second value is the address of the string object this cell references
- Python does a "double-hop" to get the value:
  - First hop: When the closure tries to access `greeting`, it first looks in its own local scope
  - Second hop: if not found, it then looks in the environment that was active when the closure was created (a cell, which contains variables that are referenced by closures)
- **Closures consist of an associated extended environment of the non-local variables it references (free variables)**
  - These free variables are bound to the context in which the closure was created, not the closure itself
- **Closures are lexical. They are created based on the structure of a program, not on anything that happens at execution time.**

### Partial function application (PFA)

- Involves the process of fixing a number of arguments to a function: closures are easy way to do this

~~~Python
def adder(x):
    def add(y):
        return x + y
    return add

add1 = adder(1)
add2 = adder(2)
add3 = adder(3)

print(add1(10))     # prints 11, since it remembers x as 1
print(add2(10))     # prints 12, since it remembers x as 2
print(add3(10))     # prints 13, since it remembers x as 3
~~~

- When `adder` is called with an argument, it returns a new function `add` that "remembers" the value of `x`
- Each closure is a distinct instance with its own enclosed environment
- PFA benefits:
  1. Ease of use: by setting some arguments of a function in advance, it streamlines the function for end users who then have fewer parameters to worry about
  2. Enhanced Reusability: it enables the generation of specific-use functions from a broader fu nction without the necessity for duplication of code
  3. Improved readability: by decomposing complex functions with multiple parameters into simpler function calls with fewer parameters, it enhances readability and intent of the code
- Can also use `functools.partial` to acheive the same effect as the closure example above

~~~Python
from functools import partial

def add(x, y):
    return x + y

add1 = partial(add, 1)
print(add1(5))  # Outputs: 6
~~~

- Must be careful with lambda functions

~~~Python
adders = []
for n in range(1, 4):
    adders.append(lambda x: n + x)
~~~

- In the above, all 3 lambda functions are binded to `n=3` because closures have a late binding nature
  - `n` is bound at the time the function is called, not when it is created
- Can fix this by passing it as a defualt value:

~~~Python
adders = []
for n in range(1, 4):
    adders.append(lambda x, n=n: n + x)

add1, add2, add3 = adders

print(add1(10))  # Output: 11
print(add2(10))  # Output: 12
print(add3(10))  # Output: 13
~~~

- The defualt trick works because you are performing an assignment which is remembered instead
- Without `n=n` `n` is taken "by reference" instead of "by value"

~~~Python
def adder(n):
    def add(x):
        return n + x

    return add

adders = [adder(n) for n in range(1, 4)]

add1, add2, add3 = adders

print(add1(10))  # Output: 11
print(add2(10))  # Output: 12
print(add3(10))  # Output: 13
~~~

- Could also do the above to define an `adder` factory function that explicity captures the value of `n`
- Factory function: describes a function that returns a new specilized function when called
  - The last example of `adder` acts as a factory function since it is designed to create and return new functions each time it is called

- Again: **A closure is a function that retains the bindings of the free variables that exist when the function is defined, allowing the function to access those variables even after their original scope has ended**

## Decorators

- A decorator is a function that accepts a function and returns a function. Can also accept a class and return a new class
- Example of one that prints a message before and after it executes the original function:

~~~Python
def my_decorator(func):
    def wrapper():
        print("Before the function call")
        func()
        print("After the function call")

    return wrapper

def say_hello():
    print("Hello!")

decorated_hello = my_decorator(say_hello)
decorated_hello()
# Before the function call
# Hello!
# After the function call

@my_decorator
def say_hello():
    print("Hello!")
~~~

- Can use the wrapper to get the same thing
- Example: `lru_cache` from `functools` for remembering ccalculated values
  - `dataclass` wrapper for classes to add an initializer and other methods, simplifying it

## Callables

- Anything you can call - aka that can be used with () - is a callable in Python
  - classes are callables
  - Also some built in functions like `enumerate`

- Duck typing for callables
  - If something can be called like a function, it can be treated as a function even if it is a class or other type of object
- Can define the `__call__` duner method to define callable behavior
  - Example: in a custom class
  - Any object that implements this dunder is a callable

## Modules

- Avoid wild card imorts to prevent namespace pollution
- This happens since each module in Python operates in its own namespace -- a kind of container for variables, functions, and classes.
- When you import names from a module traditionally (using import module_name), you maintain the separation of namespaces, which avoids name clashes
  - Wildcard imports merge the imported module's namespace with your own, potentially overwriting existing names and leading to conflicts
- Scripts vs  modules
  - Script: A Python file meant to be run directly. It performs actions, prints output, and may use functions or classes defined within it or imported from other modules.
  - Module: A Python file meant to be imported into other Python scripts or modules. It's a toolset of sorts, providing resources like functions, classes, and variables to enhance and extend the functionality of the script that imports it.
- Can use the `__name__ == '__main__'` to run as script and module

## Side Effects and Pure Functions

- A function that performs any of the following is said to have side-effects:
  1. It reassigns any non-local variable
  2. It mutates the value of any object referened by a non-local variable
  3. It reads from or writes to any data entity (files, network connections, etc) that is non-local to your program
  4. It raises an exception
  5. It calls another function that has any side effects that are not confined to the current function. For instance, you call a function that mutates an argument, but that argument is local to the calling function, then it isn't a side effect.
- **It is more proper to ask if a specific function call has side effects**
- **Unexpected function side effects are a major source of bugs**
- Pure Functions:
  1. Have no side effects
  2. Given the same set of arguments, the function always returns the same value during the function's lifetime. This rule implies that the return value of a pure function depends solely on its arguments

## Assertions

- A programming statement that specifies a condition that must hold true at a certain point in a program
- Scenarios:
  1. Equality assertions: typically with `==` to verify return values
  2. Boolean assertions: test truthiness
  3. Comparison Assertions: use comparison operators to rest whether a value meets certain relational conditions
  4. Containment assertions: verify item present in collection
  5. Exception assertions: when expecting certain code to raise an exception due to erroneous inputs or states
- `assert` raises an `AssertionError` if given condition is falsy
- Syntax: `assert condition, message`
  - condition is what you are testing
  - `assert` is not a function or callable object, don't use parentheses

~~~Python
# Equality
def add(a, b):
    return a + b

assert add(3, 4) == 7, "Add function failed"

# Boolean
is_active = True
assert is_active, "Boolean check failed"

# Comparison
def get_max(a, b):
    return max(a, b)

assert get_max(10, 20) > 15, "Comparison check failed"

#Containment
numbers = [1, 2, 3]
assert 2 in numbers, "Containment check failed"

# Exceptions
try:
    x = 1 / 0
    assert False, "Exception check failed, no exception raised"
except ZeroDivisionError:
    pass  # The assertion is passed implicitly if the exception is raised because it should never reach the statement
~~~

## Unittest

- Test suite: the entier set of tests that accompanies your program or application
- Test: describes a situation or context in which tests are run, can contain multiple assertions
- Assertion: The verification step that confirms your program is producing the results you expect
- 4 steps to writing tests (SEAT):
  1. Set up the necessary objectgs
  2. Execute the code against the object we're testing
  3. Assert that the executed code did the right thing
  4. Tear down and clean up any lingering artifacts

~~~Python
import unittest
from car import Car

class CarTest(unittest.TestCase):
    def setUp(self):
        self.car = Car()

    def test_wheels(self):
        self.assertEqual(4, self.car.wheels)

    def test_car_exists(self):
        self.assertTrue(self.car is not None)

    def test_name_is_none(self):
        self.assertIsNone(self.car.name)

    def test_instance_of_car(self):
        self.assertIsInstance(self.car, Car)

    def test_includes_car(self):
        arr = [1, 2, 3]
        arr.append(self.car)
        self.assertIn(self.car, arr)

    def test_raise_initialize_with_arg(self):
        with self.assertRaises(TypeError):
            car = Car(name="Joey")

    def test_set_name_raises(self):
        self.assertRaises(ValueError, setattr, self.car, "name", 1234)

if __name__ == "__main__":
    unittest.main()
~~~

- Not included here but also an option to include a tearDown() method that will run after each test: helpful for cleaning up files or logging some information
- setup() runs before each test
- **`assertEqual` is testing for value equality, need to use `assertIs` for object equality**
- Have to define `__eq__` method in our class to compare custom objects in tests
