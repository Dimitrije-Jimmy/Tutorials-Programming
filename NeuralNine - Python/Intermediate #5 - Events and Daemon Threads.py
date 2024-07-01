"""
Events and Daemon Threads

Events - are things that we can trigger, when we trigger them we can react to them
"""

import threading

event = threading.Event()
# we can trigger this event and wait for it
# it's just an object/element that has the function to be triggered
# once triggered we can make certain things to happen

def myfunction():
    print("Waiting for even to trigger... \n")
    event.wait()
    # this makes our function wait here until it is triggered
    print("Performing action XYZ now...")
    # this is the response to the event being triggered
 
t1 = threading.Thread(target=myfunction)
t1.start()

# until the even is triggered this thread t1, nothing happens

# we can tell the user to input
x = input("Do you want to trigger the event? (y/n) \n")
if x == "y":
    event.set() # setting the event means we've triggered it
    # "now you can stop waiting"


"""
Daemon Threads - they run in the background and the script terminates even though
 they're still running, they're not vital for the programm
 nobody wait's for Daemon threads
 we can use them for constantly reading data from a file, reading from a web API
 when everything is done we terminate the script and Daemon threads
"""

import threading
import time

# one thread is a Daemon thread reading from a text file
# another thread is printing the information from that file

path = "d:\\Programming\\Tutorials\\NeuralNine\\text.txt"
text = ""

def readFile():
    # this function will do a constant loop to read information from file
    global path, text
    while True:
        with open(path, "r") as f:
            text = f.read()
        time.sleep(3)
    
    # read the information, waits for 3 seconds, and does the same thing again

def printloop():
    for x in range(10):
        print(text)
        time.sleep(2)

# readFile we run in a Daemon thread, because it's not important and we can terminate the script
# when printloop finishes we terminate the script

t1 = threading.Thread(target=readFile, daemon=True)
t2 = threading.Thread(target=printloop)

t1.start()
t2.start()

"""
if I change the text
if I change the text
if I change the text
if I change the text
if I change the text
while its running
while its running
while its running
ill get a different thing


I was able to alter the file from which it was reading whilst the script was running, 
 because the Daemon thread was opening it constantly every 3 seconds

It terminated the script when t2 was done because it's a normal thread, 
 but didn't care about t1 cause it's a Daemon thread
"""

