# Problem sets from the lessons

# Inheritance

# Create a subclass from Dog called Bulldog overriding the sleep method to return "snoring!"

# Create a new class called Cat, which can do everything a dog can except fetch. Come up with a class hierarchy.

class Animal:

    def speak():
        pass

    def sleep(self):
        return 'sleeping!'
    
    def run(self):
        return 'running!'

    def jump(self):
        return 'jumping!'

class Dog(Animal):
    def speak(self):
        return 'bark!'

    def fetch(self):
        return 'fetching!'

class Bulldog(Dog):

    def sleep(self):
        return "snoring!"
    
class Cat(Animal):
    def speak(self):
        return 'meow!'

# teddy = Dog()
# print(teddy.speak())      # bark!
# print(teddy.sleep())       # sleeping!

# karl = Bulldog()
# print(karl.speak())       # bark!
# print(karl.sleep())        # snoring!

pet = Animal()
dave = Dog()
bud = Bulldog()
kitty = Cat()

# 
# try:print(pet.run())              # running!
# # print(kitty.run())            # running!
# # print(kitty.speak())          # meow!
#     kitty.fetch()
# except Exception as exception:
#     print(exception.__class__.__name__, exception, "\n")
    # AttributeError: 'Cat' object has no attribute 'fetch'

# print(dave.speak())           # bark!

# print(bud.run())              # running!
# print(bud.sleep())             # "snoring!"

# Class hierarchy

#       Pet
#   Dog      Cat
#  Bulldog

# What is the method resolution order and why is it important?
# The MRO is the order in which Python searches through a class and its superclasses for applicable instance methods. It determines which instance method will be executed when overriding them in subclasses. AKA it is how Python traverses the class hierarchy to look for methods.

# Use the following list comprehension to pretty print MRO
# print([ cls.__name__ for cls in Bulldog.mro() ])
# ['Bulldog', 'Dog', 'Pet', 'object']

# Name the method used to customize each operator

# > uses __gt__
# * uses __mul__
# <= uses __le__
# != uses __ne__
# += uses __iadd__
# **= uses __ipow__
# // uses __floordiv__

# Consider the following class:

class Cat:
    def __init__(self, name):
        self.name = name

    def __eq__(self, value: Cat) -> bool:
        if not isinstance(value, Cat):
            return NotImplemented
        return self.name.casefold() == value.name.casefold()

    def __ne__(self, value: object) -> bool:
        if not isinstance(value, Cat):
            return NotImplemented
        return self.name.casefold() != value.name.casefold()
    
    def __lt__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented
        return self.name.casefold() < other.name.casefold()
    
    def __le__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented

        return self.name.casefold() <= other.name.casefold()

    def __gt__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented

        return self.name.casefold() > other.name.casefold()

    def __ge__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented

        return self.name.casefold() >= other.name.casefold()

# Create the methods needed so you can compare Cat objects for equality and inequality by their name value. The comparisons should ignore case and should work for the == and !=operators. If the right-hand operand is not a Cat object, the methods should return NotImplemented.

# Be sure to write test cases to demonstrate that your methods work as intended.

# bugs = Cat('Bugs')
# bugs2 = Cat('Bugs')
# elmer = Cat('Elmer')

# print(bugs == elmer)                # False
# print(bugs == bugs2)                # True

# print(bugs != elmer)                # True
# print(bugs != bugs2)                # False

# print(bugs == 'Bugs')               # False
# print(bugs != 'Bugs')               # True

# Implementation note: use casefold() because lower() does not handle certain unicode characters correctly.

# Implement the rest of the comparison operator methods

# Given the following Vector class:
# Implement addition, subtraction, and multipllication

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector({self.x}, {self.y})'
    
    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x + other.x, self.y + other.y)
    
    def __iadd__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented

        self.x += other.x
        self.y += other.y
        return self

    def __sub__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x - other.x, self.y - other.y)
    
    def __isub__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented

        self.x -= other.x
        self.y -= other.y
        return self

    def __mul__(self, other):
        if not isinstance(other, int):
            return NotImplemented
        return Vector(self.x * other, self.y * other)
    
    # Needed when the left operand is an integer
    def __rmul__(self, other):
        if not isinstance(other, int):
            return NotImplemented

        return Vector(self.x * other, self.y * other)


# print(Vector(3, 2) + Vector(5, 12))   # Vector(8, 14)
# print(Vector(5, 12) - Vector(3, 2))   # Vector(2, 10)
# print(Vector(5, 12) * 2)              # Vector(10, 24)
# print(3 * Vector(5, 12))              # Vector(15, 36)

# my_vector = Vector(5, 7)
# my_vector += Vector(3, 9)             # Vector(8, 16)
# print(my_vector)

# my_vector -= Vector(1, 7)
# print(my_vector)                      # Vector(7, 9)

# print(Vector(3, 2) + 5)
# TypeError: unsupported operand type(s) for +: 'Vector'
# and 'int'

# If both x and y can be expressed an integers, compute the sum of the integer values of x and y.
# otherwise, concatenate the string values of x and y

class Silly:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'Silly({repr(self.value)})'

    def _is_numeric(self, value):
        if isinstance(value, int):
            return True

        return value.isdigit()

    def __add__(self, other):
        if not isinstance(other, int):
            if not isinstance(other, str):
                return NotImplemented

        both_numeric = (self._is_numeric(self.value) and
                        self._is_numeric(other))
        if both_numeric:
            return Silly(int(self.value) + int(other))
        else:
            return Silly(str(self.value) + str(other))
        
# Properties problem set

# 1. Create a Person class with a "private" attribute _name. Use properties to create a getter and setter for the _name attribute. The _name attribute must be a string. Test code

class Person:
    def __init__(self, name) -> None:
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not isinstance(name, str):
           raise TypeError('Name must be a string')
        if name.strip() == '':
            raise ValueError('Name must not be empty')
        self._name = name

# rob = Person('Rob')
# print(rob.name)
# rob.name = 'mike'
# print(rob.name)
#rob.name = 123

# Update to disallow empty strings. Raise a ValueError

# rob.name = '    '
# print(rob.name)

# 3. Create a Rectangle class with attributes _width and _height. Add properties to get the width and height but to disallow modification after the object is created (i.e. no setters)

class Rectangle:
    def __init__(self, width, height) -> None:
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width
    
    @property
    def height(self):
        return self._height
    
# rec = Rectangle(3, 7)
# rec.width = 8

# Write a brightness property for the class

class SmartLamp:
    def __init__(self, color, brightness):
        self.color = color
        self.brightness = brightness

    def glow(self):
        return (f'The lamp glows {self.color} with '
                f'brightness {self.brightness}%.')

    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, color):
        if not isinstance(color, str):
            raise TypeError('Color must be a color name.')
        self._color = color

    @property
    def brightness(self):
        return self._brightness

    @brightness.setter
    def brightness(self, brightness):
        if isinstance(brightness, int):
            if 0 <= brightness <= 100: # This expression shorthand is unique to Python, Fortran, Julia, and Perl 6
                self._brightness = brightness
                return

        raise ValueError('Brightness must be between 0 and 100.')
    
# Problem Sets Exceptions:

# 1. Write a program that asks the user for two numbers and divides the first number by the second number. Handle any potential ZeroDivisionError or ValueError exceptions

def divide_nums():
    print('Enter two numbers')
    try:
        num1 = int(input('Enter number 1: '))
        num2 = int(input('Enter number 2: '))
        divide = num1 / num2
    except ZeroDivisionError:
        print('Cannot divide by 0')
    except ValueError:
        print('Value must be an integer')
    else:
        print(divide)
    finally:
        print('End of program')

# divide_nums()

# Print only when no exceptions raised

# Modify to  handle on single exception line

def divide_nums():
    print('Enter two numbers')
    try:
        num1 = int(input('Enter number 1: '))
        num2 = int(input('Enter number 2: '))
        divide = num1 / num2
    except (ZeroDivisionError, ValueError) as e:
        print(e)
    else:
        print(divide)
    finally:
        print('End of program')

# divide_nums()

# Write a program that asks the user for a number. If the input isn't a number, let Python raise an appropriate exception. If the number is negative, raise a ValueError with an appropriate error message. If the number isn't negative, print a message that shows its value.

def prob_3():
    num = float(input('Enter a number: '))
    if num < 0:
        raise ValueError('Negative numbers are not allowed!')
    print(f'You entered {num}')

# prob_3()

# 5. Modify your answer from the previous problem to raise a custom exception named NegativeNumberError instead of an ordinary ValueError exception.

class NegativeNumberError(ValueError):
    pass

def prob_5():
    num = float(input('Enter a number: '))
    if num < 0:
        raise NegativeNumberError('Negative numbers are not allowed!')
    print(f'You entered {num}')

def inverse(numbers):
    result = []
    for num in numbers:
        try:
            result.append(1 / num)
        except ZeroDivisionError:
            result.append(float('inf'))
    return result

# In some cases, a floating point number divided by 0 can be treated as infinity. In Python, infinity is represented by the name inf. This name can't be access directly; if you want an infinite value, you need to use float('inf') or float('infinity'). That's one possible solution to what happens when you divide by 0.

#print(inverse([1, 2, 0, 3, 4]))

# Write two functions to fetch the sixth element from the list: one using the LBYL approach and another using the AFNP approach. In both cases, the function should return None when the element isn't found.

numbers = [1, 2, 3, 4, 5]

# LBYL approach
def get_sixth_element_lbyl():
    if len(numbers) > 5:
        return numbers[5]

    return None

# AFNP approach
def get_sixth_element_afnp():
    try:
        return numbers[5]
    except IndexError:
        return None

# 'hello'.upper()
# #[1, 2, 3].push(4)
# {'key': 'value'}.get('key')
# (12345).length()

class Point:
    def __init__(self, x, y):
        self.coordinates = {'x': x, 'y': y}

    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        print(self.coordinates)
        print(other.coordinates)
        return self.coordinates == other.coordinates

point1 = Point(5, 10)
point2 = Point(5, 10)
point3 = point1
point1.coordinates['x'] = 4

print(point1 == point2)
print(point2 == point3)
print(point1 == point3)
print(point3 is point1)