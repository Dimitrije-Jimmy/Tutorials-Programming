// every C++ file ends with .cpp

/* <-- this is a multiline comment
we can't just start coding, we need a main function, an entry point for the program
 (thing START PROGRAM v fortranu)
We define it like this, (this case return value int)
*/

// import - include, to include something we put a # symbol,
//  # - initialise use of preprocessor directive
#include <iostream>  // iostream - input output stream library

int main() {
    /*
    we use ; after every line
    we returned 0 because our function demands an integer output
     (again think fortran defining what value it will return ahead of time)
    we can still execute other code like printing into the terminal   
    This main function is the entry point of the script
    */

    // Put whatever you want in here
    // std - standard character output
    // cout - is the print function, we can't just use it with the default stack of libraries
    //  we need to import <iostream>

    /* 
    To access the cout function we need to access it's namespace
     in the iostream library we have different namespaces, one of them is std
     std - the namespace in which the cout function is located
     to use it we say: std::cout
    To pass data into the cout function that we want to print on the screen,
     we don't call it, we send data to it using angle brackets <<, or arrows <-
     that point towards the cout function and feed the text into that function
    We also add the std::endl which is the endline, since cout won't make a line break,
     you can also type \n in your string at the end.
    We end every line with semicolons ; that tells the compiler this line is done, 
     there's no expected code after the semicolon (in the line)
    */
    std::cout << "Hello World!" << std::endl;

    return 0; 
    
}

// to compile the code manually (if you don't have VS Code setup like I do)
//  in CMD you cd into your folder with the source code
// execute: g++ "#3 - Hello World.cpp" -o "#3 - Hello World.exe"
// don't use spaces in filenames...: g++ main.cpp -o main.exe
// the -o is for specifying the executable filename
// to run it in the terminal just call the name