# Practice exercises contained in the OO with Python book
'''
How do we create a class and an object in Python?

Write a program that defines a class and creates two objects from that class. The class should have at least one instance variable that gets initialized by the initializer.

What class you create doesn't matter, provided it satisfies the above requirements.
'''

#. We create a class and an object in Python by using an instantation construtor

class Motorcycle():

    def __init__(self, engine):
        self.engine = engine
        type_name = self.__class__.__name__
        print(f"This is a {engine} size {type_name}")

# supermini = Motorcycle('112')
# big_bike = Motorcycle('250')

# Given an instance of a Foo object, show two ways to print I am a Foo object without hardcoding the word Foo.

# you can use an F string and use foo.__class__.__name__ or do type(self).__name__

class Foo:
    pass

# foo = Foo()
# print(f'I am a {type(foo).__name__} object')
# print(f'I am a {foo.__class__.__name__} object')

# Example of using property decorators:
# Added in print statements to visualize what is happening:

class GoodDog:

    def __init__(self, name, age):
        self.name = name
        print("Init in action")
        self.age = age

    def speak(self):
        return f'{self.name} says arf!'

    @property
    def name(self):
        print('NAME GETTER IN ACTION')
        return self._name

    @name.setter
    def name(self, name):
        print('NAME SETTER IN ACTION')
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
# print(sparky.name)          # Sparky
# print(sparky.age)           # 5
# sparky.name = 'Fireplug'

# print(sparky.name)          # Fireplug
# sparky.age = 6

# # print(sparky._name)
# # print(sparky.name)

# print(sparky.age)           # 6

# sparky.name = 42  # TypeError: Name must be a string

# sparky.age = -1   # ValueError: Age can't be negative