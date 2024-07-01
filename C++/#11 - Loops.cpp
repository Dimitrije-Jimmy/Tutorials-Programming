#include <iostream>

int main() {

    /*
    Loops - basic programming structures that allow us to execute the same block 
     of code repeatedly as long as a specific condition is met, or specific amount of times

    while (true statement) {
        execute code while statement is true
    }

    another example
    */

    int i;
    std::cout << "Input number: ";
    std::cin >> i;
    
    while (i > 0) {
        std::cout << i-- << std::endl;  // countdown
    }
    std::cout << i << std::endl;    // this way it ends on 0 and prints 0 in the end

    /*
    do while - slight variation of the while loop
     it checks the condition after executing the first itteration of the code
     no matter what the condition is, it executes the code atleast once 

     so in this case if we give it a negative number it will execute once and print
     the negative number, and then see that the number does not fit the statement
     criteria and it won't execute the block of code again.

    you can understand this like this:

    do {
        whatever code
    } while(false);

    this will execute the 'whatever code' once (because while(false) doesn't continue)
    */

    do {
        std::cout << i-- << std::endl;
    } while(i > 0);

    
    /*
    for loop

    for () {
        // do something
    }

    inside of the head/header of the for loop (the '()') we specify 3 things:
    1.) a control variable, can be something define before adn we initialize it inside
        int i;
        for (i = 10) {
            // sth
        }
     or it can be drectly defined in the (): for (int i = 10) {}

    2.) we put a semicolon ; and specify a condition/statement

    3.) another semicolon, and an action that is happening with each iteration 
     (i.e. the while loop increasing of i)
    example:
    */
    
    for (int i = 0; i < 10; i++) {
        // we create an int at 0, as long as i is less than 100, on every iteration 
        //  increase by 1 and execute code inside
        std::cout << "Hello! " << i << std::endl;

        // we can actualy use the same variable as something defined outsidem,
        //  as this i is only in scope of the for loop (careful tho)
    }
    
    // for loop is better for counting and iterating, better for collections, lists, arrays, ...
    // while loops are better for "As long as I don't get a trigger"
    

    return 0;
}