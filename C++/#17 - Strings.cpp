#include <iostream>
#include <string.h>


int main() {
    /*
    String are the text datatype

    history of string, C vs C++ strings, we can still use C code and C libraries
     in C there is no string class (because std::string is an object and C doesn't support OOP),

     in C++ we can just use class:  std::string, this is a string object, an instance of the class string
     in C there is only primitive data structs, in C they were just arrays of characters

     on a lower level, when we say 10 spots we're actually allocating one more for 
     the \0 - null terminator, that says "this word is now over"

    */
    // in C++:
    //std::string mytext = "hello";

    // in C:
    char text[10] = "Hellow";
    std::cout << text << std::endl;

    // you can also say
    char text2[4];
    text2[0] = 'H';
    text2[1] = 'e';
    text2[2] = 'y';  // and so on
    text[3]= '\0';  // null terminator at the end if you do it mannually

    std::cout << text2 << std::endl;

    /*
    in a nutshell you create a C-string which is an array of character, 
     and you always want to allocate one more, cause then you have a 
     null-terminator at the end (if you do the whole sentence in one line it
     does it automatically, if you write each character in individually
     you also have to manually input the null terminator)
    */

    /*
    What can we do with C-strings?

    sizeof(text) - prints the size of the array of the text, not the 
     length of the string (you allocate more due to the null-terminator)

     sizeof gives you the amount of charachter memory units - which means bytes

    strlen(text) - string length, we have to: #include <string.h>
    */

    std::cout << sizeof(text2) << std::endl;    // 4
    std::cout << strlen(text2) << std::endl;    // 3, ignores null-terminator

    /*
    A few more functions and cybersecurity

    nowadays we use the string class and not the C-string, one reason why
     is because the functions we have to use with C-strings are very insecure/
     have a lot of vulnerabilites/ are dangerous if you don't know what you're doing

    strcpy() - this function very dangerous if you don't know what you're doing
     let's say we have an array textdestination[16] and input string textinput[200], 
     the strcpy(textdestination, textinput) function takes in one string and copies 
     it into another
     the problem is that we're getting an input of a possible 200 characters,
     and we're copying into a C-string with only 16 bytes, 
     this won't give you an error message, it's just going to buffer overflow
    */
    char text_destination[16];
    char text_input[200];
    std::cout << "Input a max of 15 character or else buffer overflow! ";
    std::cin >> text2;
    
    strcpy(text_destination, text_input);
    /*
    this is exploitable in buffer overflow attacks (sometimes assembly understanding needed)
     What happens is determined in runtime, we don't know, the compiler doesn't know,
     possibility of overwriting jumpback addreses or other things. Don't fuck about.
     
     Point is if I run some software like GDB, I get the memory addresses,
     I get the structure of the program, I look into it "ok how does this work",
      "where are the individual jumpback addresses, where do I need to go",
      we can inject bytecode into this,
      we can figure out where a variable is, can we get into, can we navigate the 
      jumpback address and get into that array, can we inject bytecode into it
      that allows me to have some malicious piece of code in that buffer and execute it.
     It's how buffer overflow attacks work, you just need a function like strcpy
      that doesn't check for the length, and now you have something thats way longer
      than 16 bytes and allows you to go over the borders and overwrite 
      different parts of the memory
    */

    /*
    strcmp(s1, s2) - string compare, compares two strings, returns 0 if s1 == s2
     and less than 0 or greater than 0, if s1 != s2 

     what is s1 < s2, probably the length, characters in alphabetic order

    you can look into the "man pages" (documentation) v terminal napišeš: man strcmp

    strcat(s1, s2) - concatonate, combines/concatonates two strings

    this is only when working with C-strings!
    */

    char s1[20], s2[20];
    std::cout << strcmp(s1, s2) << std::endl; 

    //char concatenated[200] = strcat(s1, s2);    // also dangerous for buffer overflow
    // this just doesn't work
    
    /*
    Now onto MODERN STRINGS which are a string class/object
    */
    std::string s3 = "Hello World!";      // this already creates a new object in memory
    std::string s4("Hello Friends!");

    /*
    Java for example: Classname name = new Classname();

    in C++ you don't need to do that, by just saying Class s, this already
     creates an instance in the memory,

    we can also directly assign a value
    */
    std::cout << s3 << " and " << s4 << std::endl;

    /*
    The other functions but with string object, on the string object instances, 
     we use methods, 's' is not just a string/textvalue, it also has different
     function and attributes

    string_name.length() - length of the string of C++ string, this is a method 
     being called, returns length without null-terminator
    
    string_name.at(index) - gives letter at the indexed position 
    */
    //std::cout << strlen(s3) << std::endl;     // this won't work, you need a a character array, a charracter pointer
    std::cout << s3.length() << std::endl;

    // we can still index the individual positions
    std::cout << s3[6] << std::endl;
    // this would be a cleaner way of doing that! Better practice (using a method)
    std::cout << s3.at(6) << std::endl;


    /*
    compare and concatonate

    for ths we don't even need functions with C++ strings, we can just compare them
     with logical operators (again think this is an instance of a class that has
     the method of comparison written into it)

    for concatonation we just use the addition operator
    */
    // Compare
    if(s3 == s4) {
        std::cout << "SAME" << std::endl;
    } else {
        std::cout << "NOT SAME" << std::endl;
    }

    // Concatonate
    std::string combined = s3 + s4;
    std::cout << combined << std::endl;

    return 0;
}