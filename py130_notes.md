# First Class and Higher-Order Functions

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
