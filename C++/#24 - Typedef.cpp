#include <iostream>

/*
Type safety in C++ is not too complicated, you use the typedef keyword and 
 specify a data tye that already exists, 

 and now you want to use a different name for that datatype, you want to create
 a new datatype, not a class or structure nothing too complicated, just another name

The convention is to have a name_t, the _t to know it's a type, or myagetype works too.
The greenish/cyan color in the intellisense signifies it's a type.
*/
typedef unsigned int age_t;     // this is better
typedef unsigned int myagetype;

//hfjsafkfjdlk_t, hello_t, whatever_t   // syntax highlighting that it's a type because _t

/*
Let's look at a concrete example, we want to have a data type bytes, 
and it shall only allocate 1 byte of memory, and we want to do calculations with it

We already have datatypes that allocate 1 byte, bool and char, but we don't want those
*/
typedef unsigned char byte;


// we also have a different way of doing this
//  uint8 - unsigned 8 bit integer, 8 bits = 1 byte
// uint8_t - typedef unsigned char uint8_t

//typedef uint8_t mybyte;   // error: 'uint8_t' does not name a type


// fancy way to have a type for an 8 bit bitset
#include <bits/stdc++.h>
#include <stdint.h>

typedef std::bitset<8> bytetype;


int main() {

    // instead of saying this we use a datatype
    unsigned int value = 10;
    
    // we say
    myagetype age = 20;

    /*
    This is now an unsigned integer but it's of the type myagetype.
    
    This is important for typesafety, it'll be important in signatures, 
     if you have a function that accepts 'myagetype', you can still pass
     an integer in ther, but it's going to tell you "Hey this is actually myagetype"

    Has a lot to do with readability. One type that we already have in C++ is 
     size_t - also unsigned int
    This is for example a type used for defining the sizes of arrays
    */
   
    // it's still a number so we can print it and also calculate with it
    std::cout << age + 60 << std::endl;  // 80


    // the byte example
    byte b = 70;

    std::cout << b << std::endl;    // F
    /*
    The problem that we get here is that it's treated like a character,
     because it is a character, printing out F which is the character 
     that is related to the value 70

    And you can counteract this by just saying unsigned(b) (not the cleanest/
     best solution it works)
    It's still better to do this and call the unsigned, than instead of writing 
     byte b, you say char b, and then you're questioning should you be unsigning
     it when printing or not (basically for readability sake)
    */
    std::cout << unsigned(b) << std::endl;    // 70

    byte b2 = 20;
    byte b3 = b + b2;

    std::cout << b + b2 << std::endl;   // 90
    std::cout << b3 << std::endl;   // Z
    /*
    Now we get a numerical result, because we calculate the sum and it's treated
     like a number. 
    Whereas if we save the calculation to a third byte it will still be treated
     like a character 
    */

    std::cout <<sizeof(b3) << std::endl;    // 1 byte


    bytetype mb = 100;
    std::cout << mb << std::endl;   // 01100100 - binary representation
    // it's not even a 1 byte it allocates 4, so it's not what we're looking for
    // char is still our best option
    std::cout << sizeof(mb) << std::endl;   // 4


    return 0;
}