#include <iostream>

int main() {

    std::cout << "Hello World!" << std::endl;


    // we can also wait for user input before closing the progr5am with cout
    /*
    std::cin.get() is waiting for user input before it proceeds with the code
     since it's not yet done, it's going to wait before you press enter
    */
    std::cin.get();     // it works in this code

    return 0;
}