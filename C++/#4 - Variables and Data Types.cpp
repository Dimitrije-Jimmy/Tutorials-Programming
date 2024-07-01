// code structure first
#include <iostream>
#include <limits.h>

// if you don't want to always specify std::function before every time you
//  use a function, you can instead first write the following line
//using namespace std;
// this however isn't considered best practice
// clean C++ code doesn't look like this, firstly you're using only cout
//  and endl, not the whole std namespace, (basically importing entire library)
//  also potential problems with other libraries that also have these functions
// good for practice and code examples

int main() {
    // if you have using namespace std
    //cout << "Hello World" << endl;

    /*
    Variables - placeholders for values in programs
    in coding we have more data types and objects and things
    C++ is statically typed, that's why we need to define the data type before 
     we can assign data to a variable
    */

    int x = 10;
    x = 90;  // changing the value
    x = 10;  // but you can't change the datatype

    /*
    Primitive data types - numbers, texts, boolean values
    not lists, structures, classes, objects

    int - standard 16 byte integer
    short and short int - integer with smaller memory amount
    Memory Management: "Do I really need an int or is a short enough?"
     this line will give you how many bytes an integer occupies in the RAM
    std::cout << "Integer (int): " << sizeof(int) << std::endl;

    1 byte is 8 bits, therefore 
    int: 4 bytes = 32 bits
    short: 2 bytes = 16 bits
    long: 4 bytes = 32 bits  - the definition of a long is that it has
     atleast as many bytes as an int, it can have more
    long long: 8 bytes = 64 bits
    
    Many things in C/C++ are undefined, not forbidden but we don't know 
     what's going to happen

    Using 16 bits or 2 bytes, the maximum number we can represent is: 
    2 bytes = 16 bits = 65.535
    
    */

    // Numerical Data Types ____________________________________________________
    short int s = 20;
    short l = 20;
    int i = 10;
    std::cout << "Integer (int): " << sizeof(int) << std::endl;   // 4
    std::cout << "Integer (short): " << sizeof(short) << std::endl;  // 2
    std::cout << "Integer (long): " << sizeof(long) << std::endl;  // 4
    std::cout << "Integer (long long): " << sizeof(long long) << std::endl;  // 8

    // let's try and print the max number
    short k = 65535;
    std::cout << k << std::endl;    // prints -1

    /*
    We're not using an unsigned short, the difference between a signed an unsigned
     short, is that if you have a signed number (by default, we don't have to say
     signed short d), this means we start from 0 and we put half as many of the
     available bits into the positive and half as many to present
     into the negative int

    if we want to have only positive int, we put unsigned in front of it
    */
   
    unsigned short a = 65535;
    std::cout << a << std::endl; // 65535
    a = a + 1;  // outputs 0
    a += 1;     // outputs 1
    std::cout << a << std::endl;
    // my compiler outputs 0, in the video it gives him an owerflow warning
    //  the owerflow means that it ran out of the alloted memory, and it starts
    //  to count from the beginning again

    // we can also do the same with int, we can unsign it, and also overflow it
    // HEX = F,  <-- DEC = 15,  <-- BIN = 1111
    // FFFF FFFF = 32 bits = 2 bytes = 4,294,967,295


    // we also have floats, floating point and double, double is more accurate (more decimals)
    std::cout << "Float: " << sizeof(float) << std::endl;  // 4 bytes = 7 digits of accuracy
    std::cout << "Double: " << sizeof(double) << std::endl;  // 8 bytes = 15 digits of accuracy
    std::cout << "Long Double: " << sizeof(long double) << std::endl;  // 16 bytes = 31 digits of accuracy

    float f = 60.78;
    double d = 90.876512;
    long double ld = 9.1867548976;
    // depending on the accuracy that you need


    // if you want to know the limits/boundaries of a data type, include <limits.h>
    std::cout << INT_MAX << std::endl; // signed one for int
    std::cout << INT_MIN << std::endl; // signed one
    std::cout << UINT_MAX << std::endl; // unsigned one
    std::cout << SHRT_MAX << std::endl; // signed one for short
    std::cout << LONG_LONG_MAX << std::endl; // signed one for long long



    // Textual Data Types ______________________________________________________
    
    // character, this is just 1 character, 
    // character uses UTF-8 encoding, 1 byte is enough to represent all the utf charachters
    char c = 'a';
    std::cout << "Char: " << sizeof(char) << std::endl;  // 1 byte

    // you can also typecast a number into a character
    // a character is just a number that representes a character
    char g = 80;
    std::cout << g << std::endl;  // outputs P


    // strings are a collection of characters, essentially an array of characters (char array - carray)
    std::string j = "Hello World!";
    std::cout << j << std::endl;
    std::cout << "String: " << sizeof(std::string) << std::endl;  // 32
    std::cout << "String j: " << sizeof(j) << std::endl;  // 32 set amount
    // for him in the vid the sizeof(std::string) outputs 24


    // Boolean _________________________________________________________________
    // true or false
    bool b = true;
    // you can also define it as bool b = 0 <-- stands for false
    //  but because it's still a bool, that means you can't do calculations with it
    std::cout << b << std::endl;  // ouputs 1 - which stands for true
    std::cout << "Boolean: " << sizeof(bool) << std::endl;  // 1 byte

    return 0;
}