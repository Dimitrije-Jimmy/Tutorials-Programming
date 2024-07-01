#include <iostream>

using namespace std;

int main() {

    /*
    Switch Case - just an additional decision making structure in C++
    
    
    if (true) {

    } else if {

    } else {

    }
    
    
    Switch case statements, we pass into it either an int or char, and then
     we can define cases for the values
    */
    /*
    int x;
    cin >> x;

    switch(x) {
        // here we specify certain cases
        case 8:     // if case 8 - which means if the value of 'x' is 8, execute this code
            cout << "The value was 8!" << endl;
            break;   // always have to end a case with a break, otherwise it continues into the next case
        
        case 10:
            cout << "Do the action for input 10" << endl;
            break;

        default:    // if no case is met, execute this (basically ELSE)
            cout << "Nothing happened" << endl;
    }
    */

    // we can build a simple calculator

    float n1, n2;
    char op;    // operator

    cout << "Enter the first number: ";
    cin >> n1;
    cout << "Choose an arithmetic operation: ";
    cin >> op;
    cout << "Enter the second number: ";
    cin >> n2;

    // Use the switch statement to select one of many code blocks to be executed.
    switch(op) {

        case '+':
            cout << n1 + n2 << endl;
            break;
        case '-':
            cout << n1 - n2 << endl;
            break;
        case '*':
            cout << n1 * n2 << endl;
            break;
        case '/':
            cout << n1 / n2 << endl;
            break;
        case '%':
            cout << (int) n1 % (int) n2 << endl;
            break;
        // you can't use modulus on floats, you need int


        default:
            cout << "Operator not supported!" << endl;
            break;

    }

    // you could do this with IF ELSE statements, but this is more convenients
    // but you can only use integers and characters for switch case

    return 0;
}