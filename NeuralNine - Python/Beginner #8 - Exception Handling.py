"""
HANDLING EXCEPTIONS

An Error terminates the script when something happens that should happen - i.e diving by 0 or typecasting a text to number that doesnt contain a number, ...
if the Error is unhandled the script is terminated 
How to raise the errors ourselves

There are different types of errors:

x = "text"
int(x)

--> ValueError: Invalid literal for int() with base 10: 'text'
can't convert text to number



how to handle exception: Try and Except statements


"""
try: # if some exception in this code happens it goes to the except block
    x = int(input("First number: "))
    y = int(input("Second number: "))
    
    print(x / y)
except:
    print("There was an error!")

# it will still exectue code down here even if the except statement was called
# also it prints the custom error


# Sometimes we want to check for specific errors: typecasting text to number, division by 0, or diving text by number 

try: 
    x = int(input("First number: "))
    y = int(input("Second number: "))
    
    print(x / y)
except ValueError:
    print("Please enter a valid number next time!")
except ZeroDivisionError: 
    print("Cannot divide by zero!")
    y = 1
    print(x / y)

# now we'll get a different error message based on how we missused the code


"""
There's also a 'finaly block' which contains code that will execute no matter if the "try" or "except" block executes
"""

try: 
    x = int(input("First number: "))
    y = int(input("Second number: "))
    
    print(x / y)
except ValueError:
    print("Please enter a valid number next time!")
except ZeroDivisionError: 
    print("Cannot divide by zero!")
    y = 1
    print(x / y)
finally:
    print("DONE!")


"""
This is usually used when you have file 'streams' you always have to close them so you usually do this because they're very prone to exceptions and errors
"""


"""
RAISING EXCEPTIONS

Sometimes we want to raise an exception that will terminate our script
"""

def some_function():
    if True:
        raise Exception("Something went terribly wrong!")

some_function()


# You can also raise a specific error
def some_function():
    if True:
        raise ValueError("Something went terribly wrong!")

some_function()


# another way to indirectly raise an exception is "Assert" statements
#   assert statements raise an exception if the condition given is not True (is not met)

x = 100
y = 20
assert(x < y)
# by asserting we demand that this statement holds True otherwise we terminate the script