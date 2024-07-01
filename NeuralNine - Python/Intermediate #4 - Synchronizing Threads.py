"""
Synchronization of threads

how to use multiple threads at once that try to acces the same resource, how do we manage that,
 how do we ensure that there are no errors there
imagine 10 threads accessing some kind of resource that might be a restrful web API, a list of numbers, a string
 and multiple threads are trying to access that resource at the same time and change it/use it
 one is changin one is reading, this leads to problems

we prevent that with synchronization, different types of locking, and semaphores, ...
"""

# Locking
# we have a shared resource a number the power of 2
# one thread will double and one divive
# these two processes counteract and we're trying to assert what's the minimum and maximum value
# but this isn't going to work, we'll make it lock so we let one reach the max and the other the min

import threading
import time

x = 8192

lock = threading.Lock()
# this lock allows or forbids the use of our resource
# when I access my resource I have to first lock it
# if it's locked already I can't access it because somebody else is using it


def double():
    global x, lock # variable not part of func, but I want to change that global variable
    lock.acquire() # this tries to acquire the lock, if it doesn't, the code wait's here
    while x < 16384:
        x *= 2
        print(x)
        time.sleep(1) # tells a program to wait _ amount of seconds
        # we do this so we see what happens, otherwise it'll execute in milliseconds and we won't see what happens
    print("Reached the maxium!")
    lock.release() # releases the resource to be used by other processess


def halve():
    global x, lock
    lock.acquire()
    while x > 1:
        x /= 2
        print(x)
        time.sleep(1)
    print("Reached the minimum!")
    lock.release()


t1 = threading.Thread(target=halve)
t2 = threading.Thread(target=double)
    
#t1.start()
#t2.start()

"""
one thread is trying to double the number and the other is trying to divide it, so they're in the endless loop, 
 and thus we're never near the maximum or minimum

this is a trivial example because in this case we're using multithreading to run at the same time, creating the problem
 and we're solving it by joining, instead of just not running multithreading in the first place

here it bounces between a couple of numbers forever, depending how fast it can multithread


When we add the lock, the first function that get's triggered will lock the resource, do it's thing,
 then free up the resource and allow the other threads to access it

4096.0
2048.0
1024.0
512.0
256.0
128.0
64.0
32.0
16.0
8.0
4.0
2.0
1.0
Reached the minimum!
2.0
4.0
8.0
16.0
32.0
64.0
128.0
256.0
512.0
1024.0
2048.0
4096.0
8192.0
16384.0
Reached the maxium!
"""


"""
Semaphores

another very useful way to limit the access to a resource is semaphores,
 this doesn't lock up the resource completely, but limits the access through a maximum value,
 for example to a max 5 accesses. So multiple threads can access the resource but not infinite

"""

semaphore = threading.BoundedSemaphore(value=5)

# basic function that tries to access the resource
# we pass it some form of identification, because we're going to run 10 threads, 
#  all of the enumerated, so we know which thread is trying to access and which thread is locking/releasing
def access(thread_number):
    print("{} is trying to access!".format(thread_number))
    # now we try to acquire the semaphore
    # if we haven't had 5 accesses already, or if it's not already 5 times acquire without being release,
    #  we'll be granted access to the resource
    semaphore.acquire()
    print("{} was granted access!".format(thread_number))
    time.sleep(10) # 10 seconds
    print("{} is now releasing!".format(thread_number))
    semaphore.release()

"""
now we make a for loop for 10 threads that are all going to execute this function with different thread_number
"""
for thread_number in range(1, 11):
    t = threading.Thread(target=access, args=(thread_number,))
    # the args=(thread_number,) is how we pass the parameters to this thread
    t.start()
    time.sleep(1)

"""
1 is trying to access!
1 was granted access!
2 is trying to access!
2 was granted access!
3 is trying to access!
3 was granted access!
4 is trying to access!
4 was granted access!
5 is trying to access!
5 was granted access!
6 is trying to access!
7 is trying to access!
8 is trying to access!
9 is trying to access!
10 is trying to access!
1 is now releasing!
6 was granted access!
2 is now releasing!
7 was granted access!
3 is now releasing!
8 was granted access!
4 is now releasing!
9 was granted access!
5 is now releasing!
10 was granted access!
6 is now releasing!
7 is now releasing!
8 is now releasing!
9 is now releasing!
10 is now releasing!

once 5 threads are accessing, thread 6-10 won't be granted access, until one of the threads
 from 1-5 releases it's access
"""