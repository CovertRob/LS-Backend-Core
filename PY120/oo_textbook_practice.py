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