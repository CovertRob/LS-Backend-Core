# Object Oriented Programming Notes

## States and Behaviors

- Instance varialbes keep track of state
- Instance methods expose behavior for objects

## Object Scope

- Object scope refers to the methods and instance variables an object can access
  - Methods - includes those acquired by the class via inheritance or minx-ins
  - Instance varialbles - includes variables acquired via inheritance
- The instance methods to NOT belong to the object, they belong to the Class (the object can access them)
- Instance variables belong to the objects
  - An object can only access its own state

## Object Instantiation

- **For Launch School, instantiating a new class is considered it's constructor and the `__init__` method inside the class is the initializer (instance constructor) *** - remember bc different naming convention than what I am used to with Java

## Instance Variables

- Keep track of information about the state of an object
- Must assign each one in the initializer method
- Instance variables exist as long as the object exists unless explicitly deleted

## Instance Methods

- All instance methods must have a `self` parameter, see example below

~~~Python
class GoodDog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        return 'Arf!'

sparky = GoodDog('Sparky', 5)
print(sparky.speak())
~~~

- **All instances of a class have the same behavior, though they may contain different states**

## Privacy

- You can access and re-assign instance variables if they are mutable
- This is a big issue and requires users of the class to be responsible
- Rely on the convention of marking instance variables and methods for internal use by naming them with single leading underscore:

~~~Python
class GoodDog:

    def __init__(self, name, age):
        self._name = name
        self._age = age

    def speak(self):
        return f'{self._name} says arf!'

    def _dog_years(self):
        return self._age * 7

    def show_age(self):
        print(f'My age in dog years is {self._dog_years()}')

# Omitted code
~~~

- Name mangling is when Python automatically adds the class name to the front of the variables.
  - This is trigged by using `__variable`. Only two leading underscores triggers this convention in Python.
  - Often useful for inheritance situations where you don't want things overridden

## Getters and Setters

- See example below for use:

~~~Python
class GoodDog:

    def __init__(self, name, age):
        self._name = name
        self._age = age

    def speak(self):
        return f'{self._name} says arf!'
    
    def name(self):
        return self._name

    def set_name(self, new_name):
        if not isinstance(new_name, str):
            raise TypeError('Name must be a string')
        self._name = new_name

    def age(self):
        return self._age

    def set_age(self, new_age):
        if not isinstance(new_age, int):
            raise TypeError('Age must be an integer')
        if new_age < 0:
            raise ValueError("Age can't be negative")
        self._age = new_age

sparky = GoodDog('Sparky', 5)
print(sparky.name())          # Sparky
print(sparky.age())           # 5
sparky.set_name('Fireplug')
print(sparky.name())          # Fireplug
sparky.set_age(6)
print(sparky.age())           # 6

sparky.set_name(42)
# TypeError: Name must be a string

sparky.set_age(-1)
# ValueError: Age can't be negative
~~~

- Getter conventionally have same name as associated instance varible without the leading underscores
- Setters conventionally prefix the same name with set_

## Properties

- Python way to create getters and setters is to use the `@property` *decorator*
- Getters created with the `@property` decorator are known as **properties**
  - A setter is simply a property whose value can be reassigned
- Use properties for the following reasons:
  - strongly discourage misuse of instance variables
  - vaidate data when your instance variables receive new values
  - have dynamically computed attributes
  - need to refactor your code in a manner incompatible with the existing interface
  - want to improve your code readability

~~~Python
class GoodDog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        return f'{self.name} says arf!'

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError('Name must be a string')

        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if not isinstance(age, int):
            raise TypeError('Age must be an integer')

        if age < 0:
            raise ValueError("Age can't be negative")

        self._age = age

sparky = GoodDog('Sparky', 5)
print(sparky.name)          # Sparky
print(sparky.age)           # 5
sparky.name = 'Fireplug'

print(sparky.name)          # Fireplug
sparky.age = 6

print(sparky.age)           # 6

sparky.name = 42  # TypeError: Name must be a string

sparky.age = -1   # ValueError: Age can't be negative
~~~

## Class Methods

- Class methods require at least one parameter: the class itself

~~~Python
class GoodCat():

    @classmethod
    def what_am_i(cls):
        print("I'm a GoodCat class!")
~~~

- This is where we usually put functionality that doesn't deal with class instances
- All of the below are valid ways for accessing a class m ethod:

~~~Python
class Foo1:

    @classmethod
    def bar(cls):
        print('this is bar in Foo1')

    def qux(self):
        type(self).bar()
        self.__class__.bar()
        self.bar()
        Foo1.bar()

class Foo2(Foo1):

    @classmethod
    def bar(cls):
        print('this is bar in Foo2')

foo1 = Foo1()
foo1.qux()
# this is bar in Foo1
# this is bar in Foo1
# this is bar in Foo1
# this is bar in Foo1

foo2 = Foo2()
foo2.qux()
# this is bar in Foo2
# this is bar in Foo2
# this is bar in Foo2
# this is bar in Foo1
~~~

- **Do not use the obj.bar() syntax for class methods, you lose any indication that you're calling a class method**

## Class Variables

- Can set variables in the scope of the class
- Use the explicit class name because otherwise you get weird results like below:

~~~Python
class GoodCat:

    counter = 0                  # class variable

    def __init__(self):
        self.__class__.counter += 1

    @classmethod
    def number_of_cats(cls):
        return cls.counter

class ReallyGoodCat(GoodCat):
    pass

cat1 = GoodCat()
cat2 = GoodCat()
cat3 = ReallyGoodCat()

print(GoodCat.number_of_cats())        # 2
print(GoodCat.counter)                 # 2
print(ReallyGoodCat.number_of_cats())  # 3
print(ReallyGoodCat.counter)           # 3
~~~

- Above we see that because of inheritance, using the `self.__class__.counter` call increments a counter in the subclass (not the behavior we intended)

## Class Constants

- Follows the same convention as constants in the rest of python
  - Use SCREAMING_SNAKE_CASE convention

## Self

- **The name `self` is a convention, the first parameter defined for any instance method always represents the calling object, no matter what name you use**

## More about cls

- The first parameter of af class method, conventionally cls, always represents a class
- cls is nearly identical to self
  - however it conventionally referendces a class rather than an ordinary object (although in Python classes are instance objects too)
  - Theoretically, there is no difference between cls and self
  - Use cls when defining a class method and self for instance methods

## Static Methods

- Use a @staticmethod decorator to define a static methods
  - These do not have any arguments
  - Use a static method when you want to be clear that the method doesn't use or modify the object or class state

