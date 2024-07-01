#include <iostream>


/*
storage class static - if variable define static, it means that, when we
 enter the scope of where that variable is define, you're allocating memory 
 and you're not freeing that mempry until the program is terminated
*/

void myfunction() {
    // this function has a scope only accessible withing this function
    static  int x = 0;

    /*
    What C++/ the compiler does/ what we do at runtime, is we enter that function code
     by calling it in the main function, we allocate the memory for x,
     we do something with x, and we get out of the function with a return statement,
     we go back to the main function, free the memory for x, and next time
     we call myfunction again, it has to allocate x again, rinse and repeat

    By specifying keyword STATIC, we don't do that, we allocate the memory for x
     once, and we don't free that memory untill we terminate the program

    What are the effects of that?

     if we don't put static in front of the int x = 0; in this code,
     repeated calls of myfunction in main will output 1,

     but if we put the static keyword, then the value for x is stored in memory
     untill program termination, thus subsequent calls of myfunction in main
     print increasing values of x

     the first time we initialize x as 0, but then we can't initialize it again,
     it already exists, the memory is not freed, it's already allocated
     static int x = 0;  <-- this line is no longer important because we already 
     have x stored in memory so the program ignores it and just goes forward with
     the next line
    */

    // increase value of x and print it
    x++;
    std::cout << x << std::endl;

}


int main() {

    myfunction();

    //

    myfunction();
    myfunction();
    myfunction();
    myfunction();
    // no matter how many times we call this function it's going to print 1 (if no static keyword)
    // now that we have the static keyword that changes


    return 0;
}
