"""
Threading allows us to speed up our program by executing multiple tasks at the same time with so called threads
 threads are lightweight processess, they're similar to processes but need less resources
 multiple threads in the same process, share the same memory, so they can communicate better and exchange data
 this is the advantage of running multithreading
"""

# we need to import the threading module
import threading

# every thread needs to do something, this something is defined in a function (whatever)
# we say "you are the thread, and as long as you're running I want you to execute that function"
def helloworld():
    print("Hellow World!")

# we need to create an object in the Thread class
t1 = threading.Thread(target=helloworld)
    # we are reffering to the function not calling it thats why no helloworld()

# to start the method / run the function we defined
t1.start()

"""
The value of threads is that I can execute two functions at the same time which work in parallel
"""

def function1():
    for x in range(3):
        print("ONE")

def function2():
    for x in range(3):
        print("TWO")


# without threading
function1()
function2()

print("_"*20)
# multithreading
t1 = threading.Thread(target=function1)
t2 = threading.Thread(target=function2)

t1.start()
t2.start()

"""
ONE ONE ONE ONE ONE
ONE ONE ONE ONE ONE
TWO TWO TWO TWO ONE
TWO ONE ONE TWO TWO
ONE TWO TWO TWO TWO
TWO TWO TWO ONE TWO 

It doesnt always return the same
"""

"""
should tehnically print them at the same time in the same line if it's fast enough

for example in videogames you need 1 thread to process the user inputs
 another thread to render the graphics and sound, you need to execute them at the same time
""" 

"""
Waiting for threads

"""
print("_"*20)

def hello():
    for x in range(5):
        print("Hello!")

t1 = threading.Thread(target=hello)
t1.start()

"""
the problem is that the script that I have here is already in a main thread
 so when I run the script, even if I'm not using multihreading, it's running the main thread,
 and every thread I start is started from this main thread
 and if I don't say "wait for the thread to finish" (for example t1)
 I want to wait before I continue with the code, it won't wait because it's multithreading and running in parallel
"""

# for example
print("Another Text")

"""
TWO
TWO
TWO
Another Text
ONE
Hello!
Hello!
Hello!
Hello!
Hello!

it printed other things at the same time even thought the "Another Text" is the last part of the script
 it printed it sooner than the other threads finished
"""

# If I want to wait for the thread to finish before running anything else we do this
t1.join()

print("Final Text")
# now it prints it at the end


"""
TWO
Hello!
Hello!
TWO
Hello!
Another Text
Hello!
Hello!
Final Text
"""
