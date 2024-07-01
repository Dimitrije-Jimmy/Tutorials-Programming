# OOP - Object Oriented Programming

"""
It's a programming paradigm that tries to model the real world into the programming world
we're taking real world objects/things and try to make abstract models of them (i.e. books, people, cities, computers)
we use classes and objects

class - is like a blueprint of the object
object- an instance of this class
"""

# Example

class Person:
    """
    # this is a blueprint for what a person looks like in python
    # what attributes, what defines a person
    # what happens when we call the method of person
    # we don't really say the name of the person, the age, we just say they have a name, age, ...

    # the actual persons: person1, person2, are the objects
    """

    """
    To construct an object of a class we call the constructor
    constructor - a method we call whenever we want to create an object
    
    the constructor __init__ takes atleast 1 parameter which is 'self'
    the self parameter needs to be in every method, function, that we define in the class
     because it refers to the object that we're using right now

    this is just a way to generalize what we do with our objects

    we don't work with the class, we work with the objects, that are just an instance of the class

    whenever we want to access some attribute of that object we have to use the self parameter/keyword
     because it always referes to the object with which we're dealing right now
    """

    # constructor 1
    #def __init__(self):
    #    print("Hello World!")


    """
    to now create an object of the class (what we have now is just a class, it doesn't have any attributes or methods)
     we can create an instance of the class
    """


# This is how we call the constructor by calling the entire class
#  thus we execute what is written in the constructor (this example prints "Hello World!")
x = Person()

# Usually the constructor is for initializing the class
    
    # constructor 2
    def __init__(self):
        self.name = "Mike"
        self.age = 25
    # Ignore the errors, you'd put this in the class but I'm going so it's readable

person1 = Person()
print(person1.name)
print(person1.age)

# now we're accessing the attributes of the object person1

# usually we pass more parameters to the constructor i.e. name, age, height
    
    # constructor 3
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

# we're accepting some parameters and we're then assigning the values of these
#  parameters to the actual attributes of the self object

person1 = Person("Mike", 30, 180)
print(person1.height)

person2 = Person("Sarah", 21, 155)


# you can also change the values of the attributes
person1.name = "Henry"
print(person1.name)


"""
Other predefined methods (this also goes in the class but again here for reading)
"""

# this is definining other methods within the class
    def helloWord(self):
        print("Hello World!")

person1.helloWorld()


# you can also define a destructor (what happens when an object get's deleted)
    def __del__(self):
        print("Object deleted!")

# when you want to delete a variable, object, you can delete the whole objec
#  it's no longer there, it's not in the memory anymore 
del person1

# the __del__ method changes/defines what happens when the object is deleted
#  we don't use this often


"""
The STR function - what happens when we print our object
 i.e. printing the entire person1 for example

if you just write print(person1), you get: <__main__.Person object at 0x032885E0>
 you get the object and it's memory address

We'd like to get the summarry of all the attributes printed in a nice format
"""

# how it behaves when I typecast it into a string, which is what happens when we try and print it
    def __str__(self):
        return "Name: {}, Age: {}, Height: {}".format(
            self.name, self.age, self.height
        )

    """
    you're returning what happens when you typecast it to a string - a.k.a. 
        what happens when you print it
    """

print(person1)

    
    def get_older(self, years):
        self.age += years

person1.get_older(10)

"""
Class variables

up until now we've defined attributes, functions, methods
but we haven't talked about çlass variables

class variables - are not unique for each object, they are the same value for each object
 for example the amount of people we have in our class
"""

    # for example
   
class Person:

    amount = 0

    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
        
        Person.amount += 1
        # we are not using the 'self' because it refers to the individual object

    # now when we create an object with the constructor, we're also adding 1 to the class variable called 'amount'

    def __del__(self):
        Person.amount -= 1 # we also have to remove it when we deelete an object

person2 = Person("Sarah", 40, 176)
del person2

print(Person.amount) # directly accessing the amount
# basically a global variable


# DODATEK: TechWithTim za class methods

class Person():
    number_of_people = 0
    GRAVITY = -9.81

    def __init__(self, name):
        self.name = name
        #Person.number_of_people += 1
        Person.add_person()

    """
    class methods are defined differently than raider methods

    we use a decorator '@classmethod' to denote it's a class method

    the idea is that this method 'number_of_people(cls)' isn't going to be acting
     on behalf of one instance, not specific on one instance
     it's meant to be called on the entire class that's why 'cls' instead of 'self'
    """

    @classmethod
    def number_of_people_(cls):
        return cls.number_of_people
    
    @classmethod
    def add_person(cls):
        cls.number_of_people += 1

    # we can use the classmethod to add a person


"""
p1 = Person("tim")
print(Person.number_of_people)

p2 = Person("jill")
print(Person.number_of_people)
"""

p1 = Person("tim")
p2 = Person("jill")

print(Person.number_of_people_())
# now it returns 2

"""
Sometimes you want to create classes that organize fuhnctions together
 like for example import a bunch of fuctions (math, numpy, ...)
You organize it in a class so it's more structured and you can use it in modules
"""

class Math:
    # we define functions / methods we'd like to use but are not specific to an instance
    #  we don't have to make an instance of the 'Math' class we can just call them
    
    @staticmethod # not changing, they don't have access to an isntance and they don't change anything
    def add5(): # no self or cls because it doesn't access anything
        # why not define a function globally? It's more of an organizational thing
        #  and  there are some other uses for static methods
        return x + 5
    
    @staticmethod
    def add10():
        return x + 10
    
    @staticmethod
    def pr():
        print("run")



print(Math.add5(5))
# returns 10

Math.pr()
# returns "run"


