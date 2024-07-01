#include <iostream>


// for the sake of simplicity
using std::cout;
using std::endl;
using std::string;

int main() {

    /*
    Typecasting / typeconversion - converting one data type into another

    string into number so we can calculate for example
    
    */
    string s = "1023";

    //cout << s + 100 << endl;  
    /*
    error: no match for 'operator+' (operand types are 'std::string' 
     {aka 'std::__cxx11::basic_string<char>'} and 'int')
     19 |     cout << s + 100 << endl;

    deduced conflicting types for parameter '_CharT' ('char' and 'int')  
     19 |     cout << s + 100 << endl;

    we can calculate with string and int, we need to typecast it
    */

    // if you have below version C++11, you need to stringstream <sstream> library
    // for all version above C++11 we have 'stoi' - string to integer function
    int i = stoi(s);  // we need the func cause string is not primitive datatype

    /*
    for 'stof' - string to float function
--------------------------------------------------------------------------------
    std::basic_string 
Defined in header <string>
float       stof ( const std::string& str, std::size_t* pos = nullptr );    (1)	(since C++11)
float       stof ( const std::wstring& str, std::size_t* pos = nullptr );   (2)	(since C++11)
double      stod ( const std::string& str, std::size_t* pos = nullptr );    (3)	(since C++11)
double      stod ( const std::wstring& str, std::size_t* pos = nullptr );   (4)	(since C++11)
long double stold( const std::string& str, std::size_t* pos = nullptr );    (5)	(since C++11)
long double stold( const std::wstring& str, std::size_t* pos = nullptr );   (6)	(since C++11)
--------------------------------------------------------------------------------

    for other types that are primitive datatypes, we just use basic typecasting
    (int) 10.92;  <-- this will typecast 10.92 into an int
    
    this is useful for example, when you don't want to save a float into a different
     int variable, but you still want to output/use an int value of the float
    */

    cout << i + 100 << endl;

    float f = 10.78;
    int b = f;  // this does typecasting automatically

    cout << b << endl;  // 10

    cout << (int) f << endl;
    cout << (int) f + 90 << endl;   // we can also work with this result
    cout << f + 90 << endl;

    
    // also works the other way
    int c = 7, d = 3;

    cout << c / d << endl;  //  int division
    cout << (float) c / (float) d << endl;  // float division of integers
    cout << (float) (c / d) << endl;  // this still outputs 2


    /*
    This way of typecasting works perfectly when we're dealing with simple primitive
     datatypes - booleans, integers, floats, doubles, characters, ...
     doesn't work with strings, can do (int) "str" also can't do (string) 10
    
    What we need to do to convert integer  to string is:     
    */
    int num = 10;
    string s1 = "This number is: ";
    string s2 = std::to_string(num);

    // we can use arithmetic addition '+', and if we convert to strings,
    //  we can append them as strings are just lists/sequences of charachters
    cout << s1 + s2 << endl;
    //cout << s1 + num << endl;     // this one delivers error


    return 0;
}