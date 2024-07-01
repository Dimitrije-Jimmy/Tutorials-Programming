#include <iostream>

int main() {

    /*__________________________________________________________________________
    Constants - are constant and not variables, immutable,
     we can do everything with a constant that we can do with a variable
    */
    const int A = 10;   // explicit type missing ('int' assumed) 

    std::cout << A << std::endl;
    std::cout << A + 20 << std::endl;

    int b = A;

    std::cout << b << std::endl;
    b = b + 50;
    std::cout << b << std::endl;

    /*
    Immutable - we cannot change the value all of a sudden, 
     we can't increment, decrement, any arithmetic operation
    (we change b to b+50 but b is a variable)
    */
    //A = 80;   // error: assignment of read-only variable 'a'

    /*__________________________________________________________________________
    Convention/ Best Practice is to write names of constants in UPPERCASE, 
     even if it's a full word: const int MYCONSTANT = 10;
    MY_CONSTANT works too but all uppercase letters
    */

    /*__________________________________________________________________________
    Constant Pointers - we can define two types/ use the const keyword in 2 different ways

    we want to have a pointer to the variable 'a' but we want the pointer to be constant    
    */
    int a = 10;
    int c = 20;

    const int *p1 = &a;
    int* const p2 = &a; 
    
    /*
    The difference is between waht is constant, 'a' is a variable

    const int *p1 = &a;   <-- we're saying, the object that we're pointing to
     has to be treated as a constant when we're using that pointer
     thus using something like: 
    */
    //*p1 = 20;     // won't work, error: assignment of read-only location '* p1'

    /*
    That's because we said const int *name, (* means pointer), this means that 
     we can't change the value that we're pointing to, through this pointer, 
     we can still change the address that we're pointing to
    */
    p1 = &c;    // this works, because this is not where the constant keyword is placed
    
    
    *p2 = 20;
    std::cout << a << std::endl;    // this works
    /*
    Here the constant keyword is after the pointer: int * const p2
    
    This means that we can't change the address to which the pointer is pointing to
     but we can change the value/ manipulate the resource that we're pointing to
    */
    //p2 = &b;     // won't work, error: assignment of read-only variable 'p2'

    
    const int* const p3 = &a;
    /*
    The hardcore way, if we do it like this, we can neither change the address
     that it's pointing to, nor the value
    */
    //*p3 = 20;  // erorr: assignment of read-only location '*(const int*)p3'
    //p3 = &b;   // error: assignment of read-only variable 'p3'


    return 0;
}