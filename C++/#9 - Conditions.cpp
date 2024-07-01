#include <iostream>

using namespace std;

int main() {

    /*
    Conditions - are just IF statements
    */

    int a;
    cin >> a;   // user input for a

    /*
    if (statement is True) {code if true} else {code if false}, 
     {} - stands for THEN do this
    */

    if (a > 10) {
        cout << "Your number is greater than 10!" << endl;
    } else {
        cout << "Your number is not greater than 10!" << endl;
    }  // no semicolon here

    /*
    IF, ELSEIF, ELSE statement
    if (statement1) {
        code1
    } else {
        if (statement2) {
            code2
        } else {
            code3
        }
    }
    */
    if (a > 100) {
        cout << "Your number is greater than 100!" << endl;
    } else {
        if (a > 50) {
            cout << "Your number is not greater than 100 but greater than 50!" << endl;
        } else {
            cout << "Your number is not greater than 50!" << endl;
        }
    }

    // another way of doing it (else if statement)
    if (a > 100) {
        // block of code to be executed if condition1 is true
        cout << "Your number is greater than 100!" << endl;
    } else if (a > 50) {
        // block of code to be executed if the condition1 is false and condition2 is true
        cout << "Greater than 50!" << endl;
    } else {
        // block of code to be executed if the condition1 is false and condition2 is false
        cout << "Less or equal to 50!" << endl;
    }


    return 0;
}