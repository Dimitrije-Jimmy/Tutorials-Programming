#include <iostream>

/*______________________________________________________________________________
Pre-Processor Directives - are statements that are executed by the pre-processor
 which means that they happen before the compilation. These don't happen 
 during runtime or during compilation, but before

If we have something like return 0; or int a = 10; those belong to the program
 and are going to be executed when we reach that point, they get compiled 
 int assembly, bytecode, and then executed when we get there.

Pre-processor directives aren't going to be part of the code in and of themselves
 they are going to do something with the code, they are statements that manipulate
 the code before we even get to compiling the code

We already have one of these directives in this code and that's the 
 #include <iostream> statement for implementing the standard library

Pre-proccessor statements are always initialized with a #
#include, #define, #undefine, #pragma, #ifdef, #if

What #include actually does, is it copies the code that is written in <iostream>
 and puts it in here, "take the code of iostream and put it in here"

#define - defining macros, it could be just aconstant like PI, what happens now
 everytime we see the PI keyword it replaces it
*/
#define PI (3.14159)
#define SHM_NAME "myshared_mem"      // let's say we're using shared memory

#define ARR_SIZE (128)

#define square(a) a * a

int square2(int a) {
    return a * a;
}

/*
#undef - undefine, what we define we now undefine, basically removing macros

This is useful if you're defining mathematical constants like 'e = 2.71', the problem is
 that there's many things called E, so if you don't want every E in your code to
 be replaced by the macro, you'd define it and undefine it as soon as possible
 so for the rest of the code you don't have a problem
*/
//#undef PI     

#define TRIGGER


// contradicting conditions
#define COND1
#define COND2


/*______________________________________________________________________________
#pragma once - this is one of those directives that is not part of the C++ 
standard but you can still use, because almost every compiler supports it

pragma once means if you have two header files that include eachother (you
 wouldn't do this in the main.cpp file)

let's say you have header file 1 includes header file 2, and header file 2
 includes header file 1, 

 what would happen then, is because you're always just replacing the
 #include "header file.h" with the code of the other one, you would get an
 endless recursion of "I include you, you include me", so if you want to say
 "this thing will be included only once and after that it's not going to be
 included anymore" you say: #pragma once
*/
#pragma once


int main() {

    /*
    This is not the same as having a variable PI, what we did here is,
     we just replaced the text 'PI' with the number 3.14159

    This is done before the compilation, not something the program does,
     it doesn't look for a variabel PI and access it's value, we just 
     replace the string PI with the value (think CS:GO bhop macros)
    */
    std::cout << PI << std::endl;

    #undef PI
    //std::cout << PI << std::endl;     
        // now we would get error: 'PI' was not declared in this scope,
        //  it's calling for a variable but can't find it

    std::cout << SHM_NAME << std::endl;


    /*__________________________________________________________________________
    This is best practice/ recommended to define macros for stuff that can change
     very easely, let's say you're working with some sort of buffer or array
     that has to have a maxsize, and you have to work with that size on
     multiple different locations

    int arr[128]

    Instead of using a for loop that goes to 128 slots, we define a macro for 
     the arr_size and making the code more readable with this
    */
    int arr[ARR_SIZE];

    for (int i = 0; i < ARR_SIZE; i++) {
        arr[i] = i;
    }


    /*__________________________________________________________________________
    Besides strings and numbers we can also define functions with macros

    #define square(a) a * a

    this is dangerous, because we're just taking the string 'square(number)'
     and replacing it with the operation number*number
     this is not the same as defining a function and calling it
    */
    std::cout << square(5) << std::endl;    // 25
    std::cout << square2(5) << std::endl;   // 25

    /*
    Let's say we have a variable i, and we want to square it but we want
     to square it and increase the i by 1 afterwards
    */
    int i = 5;

    std::cout << square(i++) << std::endl;     // 30
    std::cout << i << std::endl;     // 7

    i = 5;
    std::cout << square2(i++) << std::endl;    // 25
    std::cout << i << std::endl;     // 6

    /*
    What happens is that the macro takes the whole 'i++' as 'a' and copies
     it into the a*a = i++ * i++ = 6*5 = 30 and increase 'i' by 1

    This is problematic and need to take care of that, not recommended for functions
    */


    /* _________________________________________________________________________
    We can also have conditions based on those macros,

    let's say we have a macro named TRIGGER, and we say if this macro is define,
     then do something:
    
    If we now undefine TRIGGER we wont get any errors because we're checking if
     it's defined or not, and if it is get into the code, otherwise don't

    #ifndef - if not defined

    with this you can check on which operating system you are
    */
    #ifdef TRIGGER
    std::cout << "Trigger is defined!" << std::endl;
    #endif


    #ifdef __linux__
        std::cout << "This is linux code" << std::endl;
    #endif

    #ifdef _WIN64
        std::cout << "This is windows code" << std::endl;
    #endif

    /*
    You just google what kind of macros depending on what you want to do
     operating system macros C++, drivers, ... anything that could be interesting

    You check if it's defined and if it is, you can execute certain pieces of
     code if you're on a certain operating system, ...
    */


    /*__________________________________________________________________________
    There is also a keyword for a pre-processor directive that triggers errors

    Let's say we have two contradicting conditions defined, 
     for example one for operating on windows, one for if we're operating on linux, 
     and if both are set, something has gone wrong
    */
    #ifdef COND1
    #ifdef COND2
    //#error      // if we want to trigger an error so we can't compile. error: #error
    #endif
    #endif


    return 0;
}