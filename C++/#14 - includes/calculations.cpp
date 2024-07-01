#include <iostream>

/*
in here we define our functions without the main function
*/

int add(int x, int y) {
    return x + y;
}

int sub(int x, int y) {
    return x - y;
}


void output_message(std::string message) {
    std::cout << message << std::endl;
}