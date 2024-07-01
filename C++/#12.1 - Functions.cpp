#include <iostream>

/*
Functions - are just blocks of reusable code

We already know the main function

First we specify the return value datatype of the function - int, 
 we deman this datatype as a return value from the function

*/

/*
continuation from below, we DEFINE the function / it's signature
(int, int) - we don't need to say (int x, int y)

the return datatype, the name, the parameter amount and their datatypes
int,    add,    (int, int)
*/
int add(int, int=90);  // the function signature
/*
this says, "There is such a function so you can use it, 
 but it's going to be implemented later on"
 Because the main() function now knows that the add() function exists, it can use it
*/
int f1();
int f2();
bool isGreaterThan(int, int);
void myfunction(void);
/*
In UNI he was taught that if you have no parameters for a function, 
 you should pass (void) into it's parameters, but he doesn't know whether
 that's really something the proffesional programmers do

The same as not passing any parameters, maybe just additional safety
*/

int add(int, int, int);     // this is now a different function with the same name
std::string add(std::string, std::string);


int main() {

    std::cout << add(10, 20) << std::endl;
    /*
    This code outputs this error:
    error: 'add' was not declared in this scope

    This is because in C++ in order to be able to access the function,
     you need to have defined it above the function that ussess it
     (this is different to fortran)
    
    You first define it, then you use it
    */

    std::cout << isGreaterThan(10, 5) << std::endl;
    myfunction();

    //std::cout << myfunction() << std::endl;
    /*
    This results in an exception:
    error: no type named 'type' in 'struct std::enable_if<false, void>'

    because this function returns nothing we can't print what it returns,
     we can just run it
    */
    
    std::cout << add(10, 20, 30) << std::endl;
    // here we're calling the second function add, that takes 3 parameters

    // string concatonation function:
    std::cout << add("Hello", "World!") << std::endl;

    // default value testing, this function call only possible because 
    //  we define the default value for the second integer
    std::cout << add(10) << std::endl;


    return 0;
}

/*
Here in the (int x, int y) those are not definitions those are parameters
 that the function takes in, with the datatype specification
*/
int add(int x, int y) {
    // Here we execute code
    return x + y;
}

/*
It's not best practice to implement functions above the main function in order of use, 
 usually we define the main() function first,
 and the implementation of the other functions comes below the main function,
 that is if we have the functions in the same file at all.

It's also a problem if we have other functions which intertvine

e.g.:     
    (i.e. - stands for 'id est' which is Latin for "That is")
    (e.g. - stands for 'exempli gratia' meaning "for example")
*/
int f1() {
    // f2()
    return 0;
}

int f2() {
    // f1()
    return 0;
}

/*
What do we do? 
We DEFINE the functions above the main function, and IMPLEMENT the functions below
*/


// We can also define functions that return float, bool, short, long, double
bool isGreaterThan(int x, int y) {
    return x > y;
}


/*
We can also define a function that returns no datatype/nothing

you can define an int funciton and return nothing, but you shouldn't do that
if you have a return value you should return it,

if you don't want to have one, what you do is you define the void function
void - emptiness, nothingness - means no return value, 
 it does something but doesn't return anything
*/

void myfunction(void) {
    std::cout << "Hello World!" << std::endl;
}


/*
Function Overloading / Overloading Functions - the idea is that we have a function
 with the same name but more parameters

int add(int x, int y) {
    return x + y;
}

int add(int x, int y, int z) {
    std::cout << "Using 3 parameters!" << std::cout // we add this to show it's a different function
    return x + y + z;
}

In Python you can't define a function name with different function signature 
 and have it be a different function
*/

int add(int x, int y, int z) {
    std::cout << "Using 3 parameters!" << std::endl;     // we add this to show it's a different function
    return x + y + z;
}


/*
We can also have a string add function, another overload function

don't forget to add signature above main()

std::string is a class, not a primitive datatype, it's an array of characters
*/
std::string add(std::string s1, std::string s2) {
    return s1 + s2;  // concatonated string
}


/*
std::string add(int, int) - outputs errors because when you're overloading functions
 you need to change the parameters, either different parameters, or more of them,
 for the code to be able to distinguish
*/


/*
Default Values for Parameters - if you don't get a value passed, it should default to it

you define that in the signature of the function:
int add(int, int, int=90);    <-- this means the last digit is a default value 90

(in this code it would be a problem doing this for the 3 parameter add func,
 because we already have a function add that takes 2 parameters so it'd be confused
 which function to take)

you can of course also define default values for multiple parameters

int add(int, int=50, int=90);  <-- notice that you have to define it from right to left
the call: int add(int, int=50, int), would not be possible
*/


