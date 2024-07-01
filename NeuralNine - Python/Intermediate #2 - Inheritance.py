"""
Let's suppose we have a generalised class and the specialised classes that inherit from the generalised one

generalised class - animal
specialised classes - dog, cat, parrot

all animals are animals, but not all animals are dogs, ...

"""

class Person:

    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def __str__(self):
        return "Name: {}, Age: {}, Height: {}".format(
            self.name, self.age, self.height
        )    
    
    def get_older(self, years):
        self.age += years

"""  
class Worker:
    def __init__(self, name, age, height, salary):
        self.name = name
        self.age = age
        self.height = height

    # it's unreasonable to define everything again, because a worker 
    #  is everything the same as a person with additional info
"""

class Worker(Person):
    # Worker is a Person and I can treat it as a Person

    # we use a special method called 'super' that acceses the parent class
    # this was we're accessing the constructor function from the parent class
    def __init__(self, name, age, height, salary):
        super(Worker, self).__init__(name, age, height)
        self.salary = salary

    def calc_yearly_salary(self):
        return self.salary * 12

    # because we haven't redefined the str function yet it doesn't print the salary when printing the entire object
    # we can 'override' the existing function by defining it once again
    def __str__(self):
        """
        return "Name: {}, Age: {}, Height: {}, Salary: {}".format(
            self.name, self.age, self.height
        )  """  

        text = super(Worker, self).__str__()
        text += ", Salary: {}".format(self.salary)
        return text
    
worker1 = Worker("Henry", 40, 176, 3000)
print(worker1)
print(worker1.calc_yearly_salary())


# even more specialised class for example - programmer
# we can make big structures and trees to model reality even better


"""
Operator Overloading

not every programming language allows user defined operator overloading,
 Java doesn't allow it, but python does

You can define yourself, what happens when you add or apply any operator on two of your objects
 (basically change what happens when you're performing operations like adittion, subtraction, multiplication and division)

i.e. what should happen when we add 2 people - in this case it doesn't make sense but
 when we have vectors it makes sense to define an add operation, because they behave differently 
"""

class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # 'self' and 'other' are just 2 different objects of the same class,
    #  in this case that means self and other are 2 different vectors that we're trying to add
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    # we do a similar for other operations
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __str__(self):
        return "X: {}, Y: {}".format(self.x, self.y)
    
v1 = Vector(2, 5)
v2 = Vector(6, 3)

print(v1)
print(v2)

v3 = v1 + v2
v3 = v1 - v2

print(v3)