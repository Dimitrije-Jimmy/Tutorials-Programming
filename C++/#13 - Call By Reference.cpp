#include <iostream>

void myfunction1(int x) {
    x++;
    std::cout << x << std::endl;
}

void myfunction2(int &x) {  // &x - means we're calling by reference (pointer)
    x++;
    std::cout << x << std::endl;
}


int main() {

    int a = 10;
    myfunction1(a);

    /*
    What's happening here is a Call By Value - we take 'a' and assign value 10 to it,
     when we call myfunction and pass 'a' as a paramater, the integer 'x', takes on
     the value of 'a', then 'x' is increased and printed.
     
     This does not mean that we're actually passing a to the function (in other
     words, 'a' is still stored as value 10 in the memory, because we only passed
     the value of 'a' into the function and assigned the value of 'x' to be the value of 'a')

     we see that by printing out 'a' after the function
    */
   std::cout << a << std::endl;
    
    /*
    This is different from the Call By Reference - we need to specify that we pass
     the address of 'x', we pass a reference to the address of the variable

    void myfunction(int &x)   <-- this is now pointing towards the address of the
     variable/paramater that we pass to this function
     so subsequent proccessing of the variable 'x', changes the memory of the
     variabel that was passed to the function

    myfunction(a)   thus in this case if &x, that would mean that x = a,
     because it's pointing to the address of 'a' and we're changing the value of 'a'

    & - operator is called a 'pointer' and it refers to the memory address of a variable to the right of it
    */
    myfunction2(a);
   std::cout << a << std::endl;


    /*
    Aliases - adverb, (nickname) used to indicate that a named person is also known or more familiar under another specified name.
    
    uses the same principle as discused and creates aliases for variables

    we sppose we have a variable and we want to create another variable that is 
     the same thing, but has a different name
    */
    int i1 = 10;
    int &integer1 = i1;     // two exact same objects i1 and integer1 are the same thing
    // changing one will change the other as they're pointing to the same address in the memory

    /*
    integer1 = i1;  <-- without the pointer this would mean that we have defines
     a variable called 'integer1' to which we assign the same value that the variable 'i1' has
    */

    std::cout << integer1 << std::endl;     // we get 10

    integer1 += 90;

    std::cout << i1 << std::endl;   // couts 100, cause integer1 and i1 are the same thing, just different alias


    return 0;
}