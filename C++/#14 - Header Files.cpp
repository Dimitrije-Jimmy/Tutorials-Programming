#include <iostream>

/*
Header Files - basic idea is that we can include functionality from
 other source files

Header Files - importing libraries

Imagine we have a huge C++ program with a lot of functionalities, functions, constants, ...
 you usually don't want to put all of this in one file, you split it up into multiple files

You create a separate source file with all the funcitonality, and you create
 a header file that allows you to include that source file

Good practice is having a separate folder with your 'includes'

Let's suppose we have a module called 'calculations.cpp' in folder '#14 - includes'
 in the module we have no 'main' function, just functions
 
 You'll usually have different source files for different more complex functionalities
 e.g.: you have a video chat app, one .cpp file for video proccessing, 
  one for sending the video via sockets, with all packaging into structs and bytes and so on

 Different functionalities outsorced to different files

We now want to include this file into the main.cpp file ('#14 - Header Files.cpp')
*/

#include "#14 - includes/calculations.cpp"
/*
theoretically we could just do this

(convention is, when including your own libraries you use "" around your module
 when using commonly used C++ libraries you use <> brackets (<iostream>))

Doing it like this is bad practice, #because you'd have to import every file separately
 but also because sometimes you want to keep the .cpp file, the actual implementation
 of your programs private, not alway sometimes you want open source but most of the
 time you don't want to give the .cpp file to people

 you just want to give them a file that tells the user of the library, what 
 functionality does this .cpp file have, what are the function signatures,
 what can I do with them, and then include it, work with it, without being
 able to look at the implementations

For this purpose we create Header Files, that have the same name as the
 source file (the file with the implementation):   source_file_name.h

 into it we put all of the definitions/signatures but without the implementation
 e.g.:      int add(int, int)

And now in this code we include the .h file not the .cpp file, and this way
 we're still accessing the functionality of the .cpp file
*/
#include "#14 - includes/calculations.h"

//#include "#14 - includes/*.cpp"   nope doesn't work

int main() {

    std::cout << add(5, 10) << std::endl;

    return 0;
}

/*
But now to be able to use this, we need to compile and link it in the right way

(for me running this with the C/C++ extension VSCode compiles and links correctly
 but I should also know how to do it manually)

cd D:\Programming\Tutorials\C++

you can't just: g++ -o main.exe main.cpp   // <-- nice format tho

you also need to compile the other source files
g++ -o main.exe main.cpp includes/calculations.cpp
*/


/*
You use a Header file for structure, you don't want to have an y implementation in it
 second of all, to hide your source code from end user (programmer using it)
*/