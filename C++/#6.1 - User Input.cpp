#include <iostream>

int main() {

    /*
    All programs up to now have been static with no user interaction, no information
     from outside the program, when we wanted to change something we changed the code
     and recompiled it

    Now we're going to be proccessing user input

    std::cin >>  <-- opposite of cout, it get's something from the console and puts it in the code
        the outwards arrows show that it's coming from outside into the code
        we also need a variable into which we're going to be storing the input
    */

    std::cout << "Please enter your name: ";   // we don't put endline, because we want it in the same line
    std::string name;
    std::cin >>  name;
    std::cout << "Please provide your age " << name << ": " << std::endl;

    /*
    you can also do this with other types, if you input 10, it'll still be a string representation
     but you can also ask for an int or float
    We don't need to typecast it, it does it automatically
    works for primitivetypes, int, float, string, long, short
    */

    int age;
    std::cin >> age;
    // we added the 20 to prove it's an int not str
    std::cout << "Your age is " << age + 20 << std::endl;
    /*
    Please enter your name: Jimmy
    Please provide your age Jimmy:
    no
    Your age is 20

    if provided with string when it wants an int it just makes it 0

    Please enter your name: Jimmy
    Please provide your age Jimmy:
    10.5
    Your age is 30

    and when given a float it typecasts it into a string
    no error
    */

    return 0;
}


/*
C/C++ Compile Run
v1.0.50
danielpinto8zz6

compiler that he uses in VSCode
F6 - to compile and run  (you don't get same name .exe, you get a: a.exe)
F7 - for running with additional parameters

when running in VSCode terminal, cd into folder
and execute filen with:  .\'filename with spaces.exe'
or if no spaces:  .\main.exe
*/