#include <iostream>

//using namespace std;

// again not best practice but you can also just include specific funcitons
using std::cout;
using std::cin;
using std::endl;

int main() {

    int n1, n2;
    
    cout << "Please eneter the first number: ";
    cin >> n1;
    cout << "Please eneter the second number: ";
    cin >> n2;
    cout << "The sum is " << n1 + n2 << endl;
    

    // we can also wait for user input before closing the progr5am with cout
    /*
    std::cin.get() is waiting for user input before it proceeds with the code
     since it's not yet done, it's going to wait before you press enter
    */
    std::cin.get();     // doesn't work for some reason

    return 0;
}