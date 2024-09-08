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
- `with` is known as a *context manager*: special kind of ocnstruct designed to allocate and release resources

~~~Python
try:
    with open('example.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print('The file does not exist')
~~~

- Best to use try/accept blocks such as above when opening files
