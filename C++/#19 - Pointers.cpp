#include <iostream>

void function1() {
    std::cout << "I am function 1!" <<std::endl;
}

void function2() {
    std::cout << "I am function 2!" <<std::endl;
}

int main() {

    /*__________________________________________________________________________
    Pointers are a very essential concept when it comes to low level programming
     in languages like C/C++, Rust, Go

    A pointer is just something that points to the memory address of another thing
    */

    int a = 10;

    std::cout << sizeof(a) << std::endl;    // 4 bytes allocated for this particular integer

    /*
    Now the question is "Where is this integer stored". It's stored in the RAM
     but at what address, how do we know where exactly it is.

    _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ...

    GIGA of empty slots, when we create/ store an integer, we allocate 4 of those bytes/ empty slots
     in order to know we're talking about those specific 4 slots, we have memory addresses
     every single slot in the RAM has a memory address and we can print it with
     &a operator

    &a - and operator, gives memory address of 'a'
    */
    std::cout << &a <<std::endl;    // this is the memory address where 'a' is stored in HEXA DECIMAL
    // for me right now it's 0x4a3fffc54, always different

    /*
    if we want to store this location in a variable, this is then a pointer
    
    this means myptr variable is pointing to the memory address of 'a'
    */
    int *myptr = &a;

    std::cout << myptr << std::endl;    // 0x4a3fffc54

    /*
    With this pointer we can also dereference it, which means we add a * in
     the cout and say we are not asking for the value of the pointer, but 
     we're asking for the value of the thing that the pointer is pointing at

    i.e.: in this case it should print out the value of 'a' which is 10
    */
    std::cout << *myptr << std::endl;   // 10

    /*
    we can also change the value of 'a' using the pointer myptr

    It's important to always specify the * symbol, because that means we're 
     dereferencing the pointer, we're not changing the actual value of the pointer
     because that would make it point to a different address
    
    By using the * symbol we're chaning the value of the thing that the pointer is pointing at
    */
    *myptr = 20;
    //myptr = &b;   // this would be changing what this pointer is pointing at (different address)

    std::cout << a << std::endl;    // 20


    /*__________________________________________________________________________
    Array pointer / pointers to arrays

    we create an integer array with 100 slots which means 100x4 bytes
     this means that we pick a starting address and allocate the next 
     400 bytes for the values 
    In fact the array itself is the pointer to the first position

    What we see, is that the memory addresses increase with a stepsize of 4
     but in hexadecimal, that's why it goes 0,4,8,c; c - stands for 12 in hexa-decimal
     this is because every integer slot takes 4 bytes so the next one starts 4 bytes later obviously
    */
    int arr[100];

    std::cout << &arr[0] << std::endl;      // 0x11975ff580
    std::cout << &arr[1] << std::endl;      // 0x11975ff584
    std::cout << &arr[2] << std::endl;      // 0x11975ff588
    std::cout << &arr[3] << std::endl;      // 0x11975ff58c
    std::cout << &arr[4] << std::endl;      // 0x11975ff590
    std::cout << &arr[56] << std::endl;     // 0x11975ff660

    // we can also print out the address of the array itself (it's just starting index)
    std::cout << &arr << std::endl;     // 0x11975ff580

    /*
    we don't use &arr because the arr is pointing to that address in and of itself
    
    'in and of itself' - latin 'by or in itself; without reference to anything else; intrinsically
    */
    int *ptr = arr; 

    std::cout << ptr << std::endl;  // the pointer is now pointing to the same address as array: 0x11975ff580
    std::cout << "_______________" << std::endl;

    /*
    Pointer Arithmetics - we can add, subtract values to pointer

    ++ptr - adds 1 to the pointer address thus showing the next address (stepsize 4 bytes)
    */
    int b = 10;

    int *ptr2 = &b;

    std::cout << ptr2 << std::endl;  // address of 'b': 0x83fabff870

    // we can now increase the value of the ptr
    std::cout << ++ptr2 << std::endl;   // 0x83fabff874
    std::cout << ++ptr2 << std::endl;   // 0x83fabff878
    std::cout << ++ptr2 << std::endl;   // 0x83fabff87c
    std::cout << ++ptr2 << std::endl;   // 0x83fabff880
    std::cout << ++ptr2 << std::endl;   // 0x83fabff884

    *ptr = 20;  // now we're no longer changing 'b' because the pointer ptr2 
                //  is pointing to a different address
        // once again same problem as with buffer overflow, undefined, we don't know whats happening
    std::cout << b << std::endl;    // 10

    /*
    We can however use this to itterate through an array instead of a FOR loop
    */
    int arr2[10];

    int *first_post = arr2;

    for(int i = 0; i < 10; i++) {
        /*
        we calculate the first position (current pointer that points to the first position)
         + i (how many integer steps do I want to go further)
        dereferncing it, and changing the value there to something: i * 20 for example
        
        we're just assigning random values into the array
        */
        *(first_post + i) = i * 20;
    }

    // looping through the array
    for(int x : arr2) {
        std::cout << x << std::endl;
    }


    /*
    notice the stepsize 4, we're once again dealing with integers,
     the type of the pointer and the type of the variable that the pointer is pointing to
     determinse how big the stepsize is

    if we have an integer pointer it assumes the next element is also an integer
     so it always goes with increments of 4, if we have a bool pointer, then 
     the stepsize/increment is always 1, all based on bytes
    */
    bool c = true;
    bool *ptr3 = &c;    // now stepsize of 1

    std::cout << ptr3 << std::endl;         // 0x42cb9ff7ef
    std::cout << ++ptr3 << std::endl;       // 0x42cb9ff7f0
    std::cout << ++ptr3 << std::endl;       // 0x42cb9ff7f1
    std::cout << ++ptr3 << std::endl;       // 0x42cb9ff7f2
    std::cout << ++ptr3 << std::endl;       // 0x42cb9ff7f3
    std::cout << ++ptr3 << std::endl;       // 0x42cb9ff7f4


    /*__________________________________________________________________________
    Null Pointers - make pointer point to nothing/nowhere
    
    Now we want to do sth with ptr4, and then we want to say to the pointer that it's done,
     that it no longer has to point at 'd', and we also don't want it to point
     at 'b' or any other variable, or any other random memory address,
    I want you to point nowhere!

    The outdated way:
    ptr = 0;
    otr = NULL;     // C

    this is problematic because when you're passing it to a function, NULL is just
     another way of saying 0, it's just a name for 0, the value of NULL is still 0
     sometimes the function won't know whether it's 0 or NULL
    You'll encounter this in old code

    The best practice way:
    ptr = nullptr;    

    nullptr isn't 0, it's an actuall thing, it's not just a macro as NULL is,
     but still returns true when comparing with 0
    */
    int d = 10;
    int *ptr4 = &d;

    // do sth with ptr4

    ptr4 = nullptr;
    if (ptr4 == 0) {
        std::cout << "message" << std::endl;  
    }


    /*__________________________________________________________________________
    Void Pointers - pointers with the type void, that means they can point to virtually everything
    
    They are not limited by a type, however this is not something you should
     always use, this is meant for very special niche cases not recommended for beginners
     sometimes they're necessary
    */
    int e = 20;
    
    void *vp = &e;

    std::cout << vp << std::endl;   // 0x4b14fff604

    /*
    if we had:

    int e = 20;
    bool *vp = &e;

    it would return an error:
    "cannot convert 'int*' to 'bool*' in initialization"
    */

    /*
    let's say we have a character and we want to know the memory address of that character
    
    the problem with that is that you can't just print it, we get some string
     that is definitely not the memory address of the character

    This is because a character pointer is interpreted as a string, a sequence 
     of character and not as a memory address, we treat this A¶ as the starting 
     point of a character array - C-string

    To print the actual memory address of the character you'd just need to 
     cast it to a void pointer: (void *)
    */
    char mychar = 'A';

    std::cout << &mychar << std::endl;                 // A¶
    std::cout << (void *) &mychar << std::endl;        // 0x77d13ffb83


    /*__________________________________________________________________________
    Pointers to pointers - we can use pointers to point to other pointers

    the pointer also needs to be stored somewhere
    */
    int j = 10;

    int *ptr5 = &j;

    // pptr5 points to the memory address of ptr5
    int **pptr5 = &ptr5;

    std::cout << ptr5 << std::endl;     // 0xe2645ff6bc
    std::cout << *pptr5 << std::endl;   // 0xe2645ff6bc


    /*__________________________________________________________________________
    Function Pointers 

    we define two functions f1 and f2, and we can define a pointer that points
     onto the function, and then we can change the value that this pointer has
     but we always execute the same function with a different functionality.

    First we specify the return value, because a pointer has a certain signature
     and every function that we point to, has to have that signature
     we can't define a void function pointer and let it point to an integer function

    signature(*pointer_name)(parameter_list)

    we also have to have the same signature and parameter_list for both functions
    */

    void(*myfunc)();

    myfunc = function1;

    myfunc();

    myfunc = function2;

    myfunc();

    return 0;
}