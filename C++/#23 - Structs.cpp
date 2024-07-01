#include <iostream>

/*
Structs - structs are used to represent data structures in C++

You have a struct with a name, and the idea is that you combine multiple things
 into one structure, ALMOST A CLASS/OBJECT!

differences:
- the members are public by default for a strut, not the same for class
- also not best practice to use structs for things you'd like to use classes for

If you want to represent a data structure - you use a Struct
If you want to actually represent an object something like a book, a human - you go for a Class

In C++ Structs are much more like Classes, in C they're really just data structures
*/
struct mystruct {
    int i;
    std::string s;
    bool b;

    // you can't do this in C, basically a method, this function belongs to this struct
    void test() {
        std::cout << "Test" << std::endl;
    }
};

// This would be a class
class MyClass {       // The class
  public:             // Access specifier
    int myNum;        // Attribute (int variable)
    std::string myString;  // Attribute (string variable)
};


// usually we'd want to model a person with a Class, but this is just for example's sake
// This is especially useful if you're doing something in C or GO, 
//  in GO you also don't have Classes, only Structures
struct person {
    std::string name;
    int age;
    char gender;
    float weight;

    // this function prints info
    void print_info() {

        // String formatting: https://stackoverflow.com/questions/2342162/stdstring-formatting-like-sprintf
        //std::cout << std::format("Hello {}!\n", "World");

        std::cout << "Name: " << name << ", Age: " << age << ", Gender: " << gender << std::endl;
    };
};  


int main() {

    // even behaves like a class
    struct mystruct m1;
    m1.i = 20;
    m1.s = "Hello";
    m1.b = true;

    std::cout << m1.i << std::endl;
    std::cout << m1.s << std::endl;
    std::cout << m1.b << std::endl;

    m1.test();

    /*
    This is not the same as saying int i, and string s, ...
    
    Those values belong to this particular structure (think instance of class)

    */

    struct mystruct m2;
    std::cout << m2.i << std::endl;     
    std::cout << m2.s << std::endl;     
    std::cout << m2.b << std::endl;     
    // now we get undefined values cause we don't have anything assigned


    struct person p1;
    p1.name = "Max";
    p1.age = 25;
    p1.gender = 'm';

    p1.print_info();


    struct person p2;
    p2.name = "Anna";
    p2.age = 35;
    p2.gender = 'f';

    p2.print_info();

    /*
    This works more like a Class, in C you can't do this with functions

    We can also look at the size, how many bytes it allocates for a struct
    */
    std::cout << sizeof(p1) << std::endl;   // 40 without float, 48 with float now defined
    std::cout << sizeof(p2) << std::endl;   // 40 without float, 48 with float now defined

    return 0;
}