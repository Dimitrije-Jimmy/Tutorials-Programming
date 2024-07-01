#include <iostream>

/*
Arrays - are essentially just collections of the same datatype

datatype arrayname[amount of slots];

We have a section in the RAM, memory stack, where we have the array placed in there
 we write and read values from there, but unlike Java for example
 We can also go beyond the limits, i.e. allocating 20 spots and going to 35
  problem is we don't know what happens
*/

int main() {

    int myarray1[5];    // 20 spaces for 20 integers = 80 bytes 

    /*
    accessing individual values,  same indexing as python
    
    Accessing the array[index] before assigning any value to that spot
     printing something that we haven't assigned yet, we've allocated the space,
     but we haven't said what should be inside of that space, 
    
    What the compiler does here is it says "This range/ this section of memory
     is for this array, but we don't do anything" 
     this section in the memory may already have something in there / some values
     it can have values from previous stuff, random values, zeros
     we just allocate the space, we don't change it, that's why the values are still in there

    We can see this in effect by looping throught the array and printing it's values
    */
    for (int i = 0; i < 20; i++) {
      std::cout << myarray1[i] << std::endl;
    }
    /*
    Outputs:
    616436944
    32758     
    616441549 
    32758     
    -903671184
    32762     
    616436944 
    32758     
    2
    0
    2
    32758     
    8
    0
    616436761 
    32758
    0
    0
    53
    0
    */

    /*
    If we don't want the random values in there, we can just overwrite them in definition
    
    We can also overwrite the first few values by inputing them in the {},
     the rest of the values will be zeros
    */
    int myarray2[20] = {10, 80, 20};


    /*
    What happens if we go beyond the limit of the array

    you can cout array at index 50 despite your array being of length 20

    What happens is we get some random value, it's completely undefined, 
     because we're somewhere in the memory that doesn't belong to this array,
     we can still access it but what happens when we do it it's udnefined
     
     (depends on the compiler, we can end up anywhere and read AND WRITE)
     this is dangerous because you can overwrite some other value because you 
     went over the length of your array

    it's more dangerous if the program terminates than if it crashes, because
     if it crashes you atleast know you fucked up, if it terminates good luck finding it
    
    RAM - Random Access Memory, in here we have the memory where we have all our
     variables, important values and important jumpback addresses for example
     
    Jumpback adress - when we call a function, we jump to that function, execute the code
     and when it ends we need to jumpback and know where to jumpback and continue the rest 
     of the code.
    The problem is we have all of this stored in the stack, which means if we go beyond
     the limits of the buffer of the array that we have, we could land on the 
     jumpback address and override it, and this can happen by accident
     It's dangerous because we don't know what we overwrote, best case scenario it crashes
    */
    std::cout << myarray2[50] << std::endl;


    /*
    This is one thing that hackers do 'Buffer Overflow', basic idea is that

    you have some user input, you string copy into string/character buffer
    you have acertain amount of characters that you can store with a buffer of let's say 50
    and you take some user input that is dynamic size, let's say the user passes 100
    what happens is you fill up those 50 characters and go beyond that and write
    wha the user has put into the program, this is dangerous because the user can put 
    instructions in there that override the jumpback address and then execute 
    the code inside of that buffer

    myarray[50] = 200;
    std::string s;
    std::cin >> s;

    NEVER GO BEYOND THE LIMITS OF WHAT YOU HAVE ALLOCATED!!!
    */

    /*
    you can also define the size of an array using a variable
    we can use this to create a dynamically sized array

    not sure if it's available for all versions of C/C++, or is it compiler based
     soemtimes it doesn't work unless integer is cosntant based, and sometimes
     you need to pass static values, and if you want to have dinamically sized values
     you need to use the function 'malloc'
    */
    int a;
    std::cin >> a;

    int myarray3[a] = {10, 20, 30};

    for (int i = 0; i < a + 10; i++) {
      std::cout << myarray3[i] << std::endl;
    }
    /*
    This code will take in a value for the length of the array,
     create the array with 10, 20, 30 as the first 3 spots

    Then we print and the values will be 10, 20, 30, 
     followed by (a - 3) zeros,
     then we print an additional 10 values, which is now buffer overflow
     thus printing random values it retrieves from memory at those indexes 
    */

    return 0;
}


/*
Originally Answered: What is the difference between stack overflow and buffer overflow?
Both are memory areas, stack is allocated by program per specific single thread/object/method to hold its unique data structures while buffer is created on the heap and is accessible by all program parts, threads, objects and methods to hold shared data structures.

Now the overflow is that you have exceeded the limits of that memory area whether was located on the stack or the heap.
*/

/*
length of arrays

https://www.digitalocean.com/community/tutorials/find-array-length-in-c-plus-plus
*/