#include <iostream>
#include "#15 - includes/myfile.h"

/*
Global Variables - they're accessible everywhere, the scope is the entire program

we can define them up here, and access it both from main and from myfunction
 but it's also accessible from other files!
*/
int x = 100;
extern int test;

/*
We can also make a global variable that is accessible everywhere in this file
 but not as global as 'x' or 'test', a.k.a. not accessible in other files
*/
static int y = 200;


int myfunction(void);

int main() {

    //int a = 200;      // commenting cause it's giving "unused variable" error
    /*
    currently myfunction can't access 'a' and main can't access 'b', outside of scope

    */

    x += 10;    // we can also change the value
    myfunction();

    /*
    if we open an IF block or WHILE/FOR loop, it's also going to be accessible in there
    */

    return 0;
}


int myfunction() {

    //int b = 10;   // commenting cause it's giving "unused variable" error/warning

    std::cout << x << std::endl;
    std::cout << add_to_x(50) << std::endl;

    std::cout << test << std::endl;

    return 0;
}

/*
we open another includes folder and in the 'myfile.cpp' we write a function
 that uses the global variable x, and in header file we specify the signature

How do we access the global 'x' in the myfile.cpp, by using the extern storage class

We can also do the opposite, define the external in the myfile.cpp and access it in here
*/

/*
Compiling:
g++ -o "#15 - Global Variables.exe" "#15 - Global Variables.cpp" "#15 - includes/myfile.cpp"

execution:  .\"#15 - Global Variables.exe"

the automatic compilation doesn't work if I'm importing the .h file but it works
 if I'm importing the .cpp file
*/

