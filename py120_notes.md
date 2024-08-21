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

## Magic Methods

- Python has over 100 of them, also called duner methods: dunder stands for double underscore
- Also magic variables and magic functions
- Pronounce it as "dunder something"

### `__str__` and `__repr__` Methods

- str: return sa human-readable representation of an object
- repr: depicts how you would recreate an object
  - often time these two return the same  value but not always
- You can re-define these in a class, otherwise inherits and use defaults from the overall object superclass
- Python implicitly uses in a variety of places:
  - calls str on each positional argument passed to print function
  - calls str when performing string interpolation, as in an f-string
  - calls repr when printing elements of a container object
- When calling str, it looks for a defined str method and then a defined repr method
  - repr does not look for a str method after not finding a defined repr method

### Comparison Methods

|Operator| Method| description|
|---------|---------|------------|
|==|`__eq__`|Equal to |
|!=|`__ne__`| Not equal to|
|<|`_lt__`| Less than|
|<=|`__le__`| Less than or equal to|
|>|`__gt__`| Greater than|
|>=|`__ge__`| Greater than or equal to|

- **By default, Python assumes that two custom objects are only equal when they are the same object**

- When using `eq` and `ne` you need to be careful in your method definitions:
  - Make sure to use NotImplemented when needed otherwise it'll default to the object comparison method
- You can avoid these checks when using nested class for internal use

~~~Python
class Cat:

    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented

        return self.name == other.name

    def __ne__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented

        return self.name != other.name
~~~

- When defining `__iadd__` you should also define `__add__`
- When defining arithmetic operators, they should obey the commutative and associative laws of arithmetic

### Magic Variables

- `__name__` variables returns teh current module's name as a string
  - often used as a main() function, refer to previous code files
- `__file__` variable returns teh full path name of the current running program
  - helpful for finding various assets and other resources needed by a program
  - sing `__file__` can be a little tricky until you get comfortable with it. You might think it'll be easier to just hardcode the file and folder names in your program. However, that's not a good idea. Once you start distributing the program, you'll lost control over where people will put the project files. By using `__file__`, relative path names, and os.path.abspath, you'll won't need to care about where people install your software. So long as they don't mess with the folder structure of the project, the program will work.

- The `__dict__` variable returns a dictionary of all the instance variables defined by an object

## Inheritance

### Class Inheritance

- Use inheritance to enable the DRY paradigm: "don't repeat yourself"
- Can redefine methods in the subclasses for specific functions

### Super Function

- super() retunrs a placeholder object that acts like an instance of the current object's superclass: **called a proxy object**
  - super function is actually a constructor for a class named super.
- The most common way to use `super` is with the `__init__` method:

~~~Python
class Vehicle:

    def __init__(self, wheels):
        self._wheels = wheels
        print(f'I have {self._wheels} wheels.')

    def drive(self):
        print('I am driving.')

class Car(Vehicle):

    def __init__(self):
        print('Creating a car.')
        super().__init__(4)

class Truck(Vehicle):

    def __init__(self):
        print('Creating a truck.')
        super().__init__(18)

class Motorcycle(Vehicle):

    def __init__(self):
        print('Creating a motorcycle.')
        super().__init__(2)

    def drive(self):
        super().drive()
        print('No! I am riding!')

car = Car()         # A car has been created.
                    # I have 4 wheels
car.drive()         # I am driving.
print()

truck = Truck()     # A truck has been created.
                    # I have 18 wheels
truck.drive()       # I am driving.
print()

motorcycle = Motorcycle()
# A motorcycle has been created.
# I have 2 wheels

motorcycle.drive()  # I am driving.
                    # No! I am riding!
~~~

- **A subclass's `__init__` method, if it exists, should almost always call `super().__init__` before it does anything else
  - The parent class usually needs to complete initializing the superclass part of the object before the subclass does anything that might rely on it

## Multiple inheritance

- Ability of a class to inherit from multiple superclasses: inherits attributes from each of those classes
  - creates a new class that combines multiple classes
- MI is tricky...stay away until you have a lot of experience...has many pitfalls

## Mix-Ins

- Classes that are never instantiated providing common behaviors to classes that have no apparent hierarchy
  - provides behaviors to other classes
  - interface only -- a standard set of methods that can be used wherever needed
  - typically small and focused on providing specific functionality
- typically class named with a `Mixin` suffix

## Is-a and has-a relationship

- Think back to the square vs rectangle problem from book
- Inheritance relationshps should have an "is-a" relationship:
  - If class A subclasses class B, then objects of type A must also be usable as objects of type B
- Be careful about inheriting from classes with incompatible API's

- If you wish to inherit from a class that doesn't have an is-a relationship, explor using a mix-in or composition
- Composition: a class uses one or more objects of other classes to provide soem of the composing classes functionality
  - Often refered to as collaboration (collaborators are objects a class interacts with to perform its responsibilities and functionality)
- **Colaboration uses other classes inside of the clas** - not in the class definition, that is inheritance
- Many dev's prefer has-a over is-a: called **Composition Over Inheritance** (COI)

## Method Resolution Order (MRO)

- modified version of a depth first search from left to right of the classes in the class definition to resolve what method to use

## Attributes and Properties

- Attribute: general programming concept, these are teh different characteristics that make up an object
  - can refer to the names or the names and values attributed to the object
- Prpoerty: a combination of an instance varible, a getter method, and an optional setter method
  - provides controlled access to the attributes of an object
- **Difficult to provide absolute definitions for OOP nomenclature**
- In summary:
  - Attributes include both methods and instance variables
  - Properties are getters and setters defined by the @property and @name.setter decorators. Properties don't require an associated instance variable, though they usualy do have one

## Duck Typing

- Duck typing occurs when objects of different unrelated types both respond to the same method namme
  - **NOT concerned with class or type of an object, but a particular behavior**
  - This is another form of polymorphism

~~~Python
class Wedding:
    def prepare(self, preparers):
        for preparer in preparers:
            preparer.prepare_wedding(self)

class Chef:
    def prepare_wedding(self, wedding):
        prepare_food(wedding.guests)

    def prepare_food(self, guests):
        # implementation goes here

class Decorator:
    def prepare_wedding(self, wedding):
        decorate_place(wedding.flowers)

    def decorate_place(self, flowers):
        # implementation goes here

class Musician:
    def prepare_wedding(self, wedding):
        prepare_performance(wedding.songs)

    def prepare_performance(self, songs):
        # implementation goes here
~~~

## Encapsulation

- describes the idea of bundling or combining the data and the operations that work on that data into a single entity aka an object
  - Python doesn't technically suppport proper encapsulation since it doens't support real *access control* for limiting attribute exposure
- Encapsulation purpose: restrict access to state and certain behaviors via access control
  - AKA objects expose a public interface: keeping their implementation details hidden
  - Python gets around this by using the underscore naming conventions
- **Classes group common behaviors and objects encapsulate state**

## Objects as State

- An object's state is saved in the object's instance variables
- You can also create brand new instance varialbes and assign it to an object

~~~Python
class Person:
    def __init__(self, name):
        self.name = name

class Dog:
    def speak(self):
        return 'bark!'

    def fetch(self):
        return 'fetching!'

class Bulldog(Dog):
    pass

bob = Person('Robert')
bud = Bulldog()

bob.pet = bud
print(bob.pet)      # <__main__.Bulldog object at 0x105001f50>\
~~~

## Collaboration

- **If object A calls any methods or accesses any instance varialbes of object B, then object B is a *collaborator* of object A**
  - If object A just holds onto B and only prints or returns it, then B is not a collaborator of A

~~~Python
class Engine:
    def start(self):
        pass

class Car:
    def __init__(self, engine):
        self.engine = engine

    def start(self):
        return self.engine.start()

class Driver:
    def __init__(self, car):
        self.car = car

    def drive(self):
        return self.car.start()

engine = Engine()
car = Car(engine)
driver = Driver(car)
~~~

- Collaboration can also take place inside a class's methods by using method arguments and instance variables as collaborators:

~~~Python
class Foo:
    def __init__(self, obj):
        self.obj = obj

    def bar(self, qux):
        return self.obj.name() + qux.name()
~~~

- **Be sure to consider what collaborations your classes will have and if those associations make sense**

- **Extending the abilities of a class coincides with an is-a relationship, not has-a**

## Coding and Design Tips

- Explore the problem before designign a solution: use code spikes
- Repetitive nouns in method names is a sign that you're missing a class
- When naming methods, don't include the class name
- Avoid long method invocation chains: long chains can blow up if something returns a value that is unexpected
- Avoid design patterns for now: premature optimization is the root of all evil

## CRC cards

- Class responsiblity collaborate cards: models various classes of a program
<https://launchschool.com/lessons/14df5ba5/assignments/d0605323>
- Only public methods should be listed on the cards

## More nuanced Python stuff

- Interning: simple objects like integers and strings can be optimized by having multiple instances reside in the same memory location
  - can lead to two strings with same value also having the same identity
  - All integers between -5 and 256 are interned regardless of how they are created

### Defining a custom `__eq__` method

- You should define one for each custom class as a good practice
- Python uses the object on the left to find the `eq` method to call
  - If it returns `NotImplemented` it switches the operands: if also returns `NotImplemented`, performs an identity comparison
- **Only `==` and `!=` fall back to using `is`: remaining operators raise a `TypeError` if both normal and reversed comparisons return `NotImplemented`**
- Do not rely on the autogenerated `ne` method that comes when you define an `__eq__` method

### Custom Operators

- Operators you can NOT customize: =, and, or, not, in, is, is not, lambda
- Recommended to define the ordered comparison methods
  - There are some subtle gotchas with the @total_ordering decorator so recomended not to use
- The `+` operator can be defined for any data type: usually some form of addition or concatenation
  - return value should normally have the same type as the left-side operand
  - Should customize `+=` operator each time we customize the `+` operator
    - When defining `__iadd__` for a immutable object, it should return a new object: otherwise it should mutate the calling object
      - This is consistent with the behavior of `+=` with built-in types
- Define in pairs and be consistent with how the operators work with built-in classes:
  - `*` can perform multiplication or repetition
  - `-` can perform subtraction or removal
  - reversed methods aren't needed if your method only works with objects of the same type: however if you're working with a mix of object types a reversed method may be necessary
    - example: working with floats and integers

## F string interpolation

`print(f'{self.radius=}')`

- The above f-string with the `=` sign constructs a string value with the variable name and then its value, good for debugging

## Variable Scope

### Instance Variable Scope

- Instance variables are scoped to an object (used ot track individual objec state)
- Python doesn't care where an instance variable is initialized, as long as it is (otherwise raises an AttributeError)

### Class Variable Scope

- Class variables track certain class characteristics and are not associated with specific instances of the class
- They belong to the class and can be referenced from anywhere in the class: body, class or instance methods, or direct reference
- Note you can have instance variables with the same name as a class variable. Yo uhave to use a class to reference the class variable to access it in this case
- From class methods you can use the class name or the cls argument

~~~Python
class Person:
    name = 'Leslie'

    @classmethod
    def get_name(cls):
        return [cls.name, Person.name]

class Teacher(Person):
    name = 'Ms Taylor'

print(Person.get_name())      # ['Leslie', 'Leslie']
print(Teacher.get_name())     # ['Ms Taylor', 'Leslie']
~~~

- Accessing from instance methods:

~~~Python
class Person:
    name = 'Leslie'

    def get_name(self):
        return [
            Person.name,
            self.__class__.name,
            type(self).name,
            self.name,
        ]

class Teacher(Person):
    name = 'Ms Taylor'

teacher = Teacher()
print(teacher.get_name())
# ['Leslie', 'Ms Taylor', 'Ms Taylor', 'Ms Taylor']
~~~

- Don't use directly self to access class variables because it is indistinguishable if it's a class or isntance variable

### Inheriting instance variables

- Instance variables are not inherited
  - If a superclass defines an instance variable, an instance of a sublcass knows about it
  - A superclass can also reference the instance variables in its subclasses
