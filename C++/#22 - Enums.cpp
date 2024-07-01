#include <iostream>

    /*
enums - Enumeration

Sometimes we want to have certain values that are simple, shapes and colors
but you don't want to use strings

*/
//std::string mycolor = "red";

/*
We are not limited with string and can provide any string we want and it's
going to be a vali string, and secondly it's too overkill for what we're
trying to do here

We just want to have a range of colors to choose and say "this is red, this
is blue, ..."

But using something like a code with integers, it's a little confusing
int color = 3;      // 3 = blue;  5 = purple

We can use Enums for that - have numerical labels for values with labvels
*/
enum Color {
    // 0,  1,    2,     3,      4
    RED, GREEN, BLUE, PURPLE, ORANGE
};
 

int main() {

    /*
    Now we can do comparisons  

    If we now print 'BLUE' we don't get the string blue we get the numerical
     value assigned to that in the enum Color

    Later when we have a Class shape or circle, and we want to say that it has
     a certain colour, we don't have to use a string, we just assign the enum color
    */
    std::cout << BLUE << std::endl;     // 2

    Color mycolor = RED;

    std::cout << mycolor << std::endl;  // 0

    return 0;
}