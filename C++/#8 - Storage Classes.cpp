#include <iostream>

using namespace std;

/*
This is not something found in Python, Java or C#, this is more low-level
 because we're talking about manual memory management, 
 this is done to improve performance

6 Storage Classes:
*/

/*
auto - default storage class, don't need to specify it, automatic storage duration
 that means the compiler figures out itself how long a variable should be stored (time)
 
 you can make the datatype automatic
    auto a = 10;
 the compiler will automatically figure out this has to be an integer,
 but don't mistake this for dynamic typing, C++ is statically typed,
 the compiler will figure out that it's an integer and it will still be a static int
 it's just so that you don't have to specify it
 it slightly increases compiler time
*/
// auto a = 10;

/*
extern - it tells the compiler that there's a variable e which is global/public
 and accessible from multiple files

You have somewhere defined the integer e, and then in another file, you'd say
 extern int e; and by doing that every other file that includes the file where this
 is written, now has access to the variable e.

Tells the compiler there exists some integer e, that's globally accessible, it
 declares the existence, the compiler doesn't care where this integer is define,
 just cares that it is define and we know that it's globally accesible so we
 can work with it, that's what extern does

 you can't say: extern int e = 10;  because the e is already define somewhere 
 else as some value

We put this line extern int e; before the main function, and we can use the variable
 for example: cout <<e
*/
//extern int e;

/*
static - has to do with memory allocation and scope
 (scope is an area of accessibility, basically if you define int a = 10;
 inside the main function, then it's accessible in main everywhere, if 
 you define a variable in a function it's accessible only in the function)

for example if we have a function outside of the main function

int myfunction () {

    int b = 20;
}

the scope of variable b is only accessible in the myfunction but not in main

if we define a third variable outside of both functions like int c = 30;
 that means it can be accessed both by main and by myfunction


whenever you define a variable in a function, the program allocates the memory 
 for the variable and once you're done with the function (whatever it proccesses)
 it dealocates the memory for the variables in the function that is no longer in use
 (except the thing the funtion returns)
 we say once it's out of scope it's deleted, next time we get into the function
 we allocate memory space again

If we don't want to do that - deallocate memory everytime, but want the allocating
 in the memory to be STATIC until the whole program is terminated
that means it doesn't dealocate the memory for a variable even if it's out of scope
 that means the next time we enter it's scope (the function) it doesn't have to
 allocate again, thus saving time, but less memory.
*/
//static int a = 10;

/*
How are variables actually stored when we define them?
int a = 10;
We first look at the datatype and we know we need 4 bytes for an integer,
 we go to the RAM and we allocate a memory block that has 4 bytes and we save/store
 the value 10 in those 4 bytes
Whenever we say something like a += 10, the CPU goes to the RAM, get's the value 
 from that memory block, applies the arithmetic operation and stores the value
 back in the RAM. RAM is fast and efficient but not for long term storage

Sometimes you might want to have a variable closer to the CPU (not always possible)
 when you might want to access an object very very often
 so you don't save it in the RAM but save it in one of the CPU registers

register int i = 10;

this way only if it's possible we store i into a CPU register, rather than RAM
sometimes we don't have any registers free in the CPU, if that happens,
 it'll allocate normal RAM memory

Don't overuse this, select very few objects that really need it, 
 thus optimizing the code

If you use a register class, you can't use pointers!
Pointer - an object that points to a memory address, 
 if object is not in RAM, then there is no thing to point at
*/
//register int i = 10;
//cout << &i << endl;  // this is how you access the memory address of an object


int main() {

    register int i = 10;

    cout << &i << endl;
    // 0x5ffe9c, it outputed a RAM memory address because there was no free register
    // if register would have been free we wouldn't have gotten an address printout

    return 0;
}


/*
for the sake of completess the last two storage classes

mutable - has to do with constants and classes (OOP)

thread_local - has to do with threads, introduced in C++11 
*/
