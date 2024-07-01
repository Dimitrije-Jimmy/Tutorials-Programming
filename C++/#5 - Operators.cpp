#include <iostream>

int main() {

    // Operators - tools that allow us to perform operations onto objects, values, variables

    // Arithmetic Operators
    // + - * / %
    int c = 10, b = 20;
    std::cout << c + b + 70 << std::endl;
    std::cout << c - b + 70 << std::endl;
    std::cout << c * b / 40 << std::endl;
    std::cout << c % 2 << std::endl;    // 0
    std::cout << c % 3 << std::endl;    // 1

    // Assignment Operators 
    // the basic one we alredy know, it's used to assign the value on the right 
    //  to the object or variable to the left (=)
    int a = 20;
    // We can combine arithmetic and assignment operators
    /*
    += - addition
    -= - subtraction
    *= - multiplication
    /= - division
    %= - modulus

    This isn't limited to arithmetic operators, there are other operators 
     that can be used for other things like the bitwise opeartors in combination 
     with the assignment operators
        a &= 10 - you use the assignment operator with another operator
            to save the result of the operation into a variable
    */
    a = a + 10;
    a += 1;
    a -= 1;
    a *= 10;
    a /= 10;
    a %= 10;
    
    std::cout << a << std::endl;


    /*
    a++ - increment, the same as saying a += 1, the difference is that it
     is also used when you want to return the value
    ++a - this one is different because it first increases the value first the display
    a-- - decrement

    so outputing a++ will first output value of a then increment it, but 
     outputting ++a will first increment it then output the value
    */

    // value of a was 0 before cout, cout displays 0 but increment because a++
    //  the ++a cout displays 2 now
    std::cout << a++ << std::endl;
    std::cout << a << std::endl;
    std::cout << ++a << std::endl;

    // same goes for decrement
    std::cout << a-- << std::endl;
    std::cout << a << std::endl;
    std::cout << --a << std::endl;


    // Comparison/Relational Operators
    /*
    used for comparisons, especially important when we come to decision making,
     if statements, loops, ...

    == - equal operator
    != - not equal
    < - less than
    > - greater than
    <= - less or equal to
    >= - greater or equal to
    all of these return a Boolean result
    */
    
    a = 10, b = 20;

    std::cout << (a < b) << std::endl;  // returns 1
    std::cout << (a > b) << std::endl;  // returns 0
    std::cout << (a == b) << std::endl;  // returns 0
    std::cout << (a != b) << std::endl;  // returns 1
    std::cout << (a <= b) << std::endl;  // returns 1


    // we can combine comparison operators with logical operators

    // Logical Operators
    /*
    && - AND
    || - OR
    ! - NOT

    & - used for pointers if used with variables, if not used for variables
     it's also used for the bitwise AND operation

    the entire logical operation needs to be in parentheses

    XOR: https://stackoverflow.com/questions/1596668/logical-xor-operator-in-c
    if(!A != !B) {
    // code here
    }

    XOR(a, b) = a ? !b : b

    bool XOR(bool a, bool b)
    {
        return (a + b) % 2;
    }
    */

    std::cout << ((a < b) && (a > 5)) << std::endl;  // returns 1
    std::cout << ((a < b) && (a > 15)) << std::endl;  // returns 0
    std::cout << ((a < b) || (a > 15)) << std::endl;  // returns 1
    std::cout << (!(a > b)) <<std::endl;  // returns 1
    //std::cout << (!(a > b) && (a > 5) || (...)) <<std::endl;


    // Bitwise Operators
    /*
    google it if you want more, apparently not useful unless doing coding challenges
     unless you know programming in assembly lmao
    
    bitwise operations perform binary (logical) operations on individual bits
    
    binary representation
    15 = 1111
    11 = 1011
    12 = 1100
    
    & - AND bitwise

    15 & 12 = (1 & 1)(1 & 1)(1 & 0)(1 & 0) = 1100 = 12
    11 & 12 = (1 & 1)(0 & 1)(1 & 0)(1 & 0) = 1000 = 8
    */


    return 0;
}