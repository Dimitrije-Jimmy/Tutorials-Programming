#include <iostream>

using namespace std;

float divide(float f1, float f2) {
    if(f2 == 0) {
        // throw error_code, error_code can be whatever (think fortran numbering GO TO)
        throw 15;
    } else {
        return f1 / f2;
    }
}

int main() {
    /*
    Exception handling

    let's suppose we have a piece of code that's very prone to errors/ exceptions
     but you can't prevent it with IF's, if you can prevent it with IF statements, 
     you do, 
     but sometimes things happen during runtime that are you can't prevent/
     is hard to/ you don't want to prevent with IF's
     
    That's why we have exception handling in case something goes wrong we do something
    (in Python we have TRY EXCEPT structure, 
     in C there are error codes, no try and excepts, and you don't deal with exceptions)
     
    Doing it in C:

    // if this something that we try returns error code -1
    if(sth == -1) {
       fprintf(stderr, "error message")
       exit(EXIT_FAILURE)
    }

    In C++ we can still do it like this, but we don't have to,
     we THROW exceptions and CATCH them
    */

    float f1;
    float f2;

    cin >> f1;
    cin >> f2;

    cout << f1 / f2 << endl;    // inf
    // C++ let's you divide by 0 and it gives you inf, even tho it's undefined

    // let's create a function that doesn't allow division by 0
    //cout << divide(f1, f2) << endl;     // terminate called after throwing an instance of 'int'
     
    /*
    We can either write our own exceptions like right here, but even if we don't
     want to do that, there are libraries that throw exceptions whe n something goes wrong,
     for example trying to open a file that doesn't exist, when we do stuff we shouldn't

    If we don't wan't to have our program crash every time it we throw an exception
     we use the TRY CATCH structure
    */

    try {
        cout << divide(f1, f2) << endl;
    } catch (int e) {   // in the () we specify what kind of exception it is
        // if you wan't to distinguish the individual errors:
        if (e == 15) {
            cout << "Division by zero is undefined!" << endl;
        } else {  
            // std::cerr
            cerr << "Error!" << endl;
        }
        
        // now the program doesn't crash and continues with the code
        // if we wouldn't catch the exception it would terminate immediately
    }
    

    cout << "TEST" << endl;

    return 0;
}