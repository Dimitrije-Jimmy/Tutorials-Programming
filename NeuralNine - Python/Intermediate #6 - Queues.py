"""
Queues

Queues are data structures similar to lists and sequences with the difference
 that they have a specific order how elements are put into the list, 
 how we access them to get them out of the list
"""

# to work with Queues we need to import them
import queue

"""
Why should we use queues? When we have multiple threads running, 
 you need to have a structured way of getting data in and out
"""

numbers = [10, 20, 30, 40, 50, 60, 70]

"""
let's suppose I have 3 threads running and each of those threads takes one of
 these numbers and proccesses it somehow / changes it / does something
 it could use it for a port check, a factorial calculation -
 i.e. takes the element and proccesses it

When it's done it needs to access the next element that hasn't been proccessed yet
 the first thread takes 10, second 20 and third 30,
 the problem is when these threads are done they need a way to say 
 "ok 20 is already used, because thread 1 takes 10, the next one is 20 but that one has already been proccessed by thread two, ..."

We need a way to tell it that the next unused one is 40
 we could make a counter and increase it's number by 1, but what happens when 
 thread 1 and 2 finish at the same time and increase the count at the same time
 then from 3 we increase directly to 5 and the 4th one would be completely skipped
 because the counter is saying it's the 5ths turn
 maybe none of them increase the counter correctly and we repeat the usage of a number and proccess it again
 not a very structure way to get multiple threads to take the same data from a collection/sequence

This is what we use queues for, making it structured
"""

q = queue.Queue() # we create the queue

# 1, 2, 3, 4, 5
# these are now in the queue
# whenever something wants to get an element from the queue it will give 1
# 2, 3, 4, 5   now the queue looks like this
# we're basically popping out the first number (first come, first serve)
# we also have different ones like (last come, first serve)

# once an element is gotten out of the list it's no longer in the list, 
#  we can't double use it, and we can't skip it

numbers = [10, 20, 30, 40, 50, 60, 70]
for number in numbers:
    q.put(number) # putting each number in the queue

print(q.get()) # it prints the next element
print(q.get())

# 10
# 20
# now there are no problems when we have like 20 threads

"""
This was the example of the 'first in first out' queue

we can also reverse this and create a 'last in first out' queue
"""

q = queue.LifoQueue()
numbers = [1, 2, 3, 4, 5, 6, 7]
for number in numbers:
    q.put(number) # putting each number in the queue

print(q.get()) # it prints the next element
print(q.get())

# 7
# 6


"""
We can also define a priority queue, it's neither first in first out nor last in first out

it's more manual, it allows you to give each element acertain priority by passing a tuple
 the lower the number the higher the priority - 1 is highest priority
"""

q = queue.PriorityQueue()

# q.put((priority, item), args)
q.put((2, "Hello World!"))
q.put((11, 99))
q.put((5, 7.5))
q.put((1, True))

while not q.empty():
    print(q.get())


"""
(1, True)
(2, 'Hello World!')
(5, 7.5)
(11, 99)

accessed by priority
"""

# you can also write key value pairs / ordered tuples
while not q.empty():
    print(q.get()[1])

# right now it doesn't work because the queue is already empty so I'd need to comment the code above
#  but this is what it would print

"""
True
Hello World!
7.5
99
"""

# for an example of how to combine threading, sockets, and queues
#  go to this link: https://www.neuralnine.com/threaded-port-scanner-in-python/
