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

print(pet.run())              # running!
print(kitty.run())            # running!
print(kitty.speak())          # meow!
try:
    kitty.fetch()
except Exception as exception:
    print(exception.__class__.__name__, exception, "\n")
    # AttributeError: 'Cat' object has no attribute 'fetch'

print(dave.speak())           # bark!

print(bud.run())              # running!
print(bud.sleep())             # "snoring!"

# Class hierarchy

#       Pet
#   Dog      Cat
#  Bulldog

# What is the method resolution order and why is it important?
# The MRO is the order in which Python searches through a class and its superclasses for applicable instance methods. It determines which instance method will be executed when overriding them in subclasses. AKA it is how Python traverses the class hierarchy to look for methods.

# Use the following list comprehension to pretty print MRO
print([ cls.__name__ for cls in Bulldog.mro() ])
# ['Bulldog', 'Dog', 'Pet', 'object']