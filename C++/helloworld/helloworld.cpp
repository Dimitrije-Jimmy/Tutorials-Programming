// LINk: https://code.visualstudio.com/docs/cpp/config-mingw

// C++ source files generally have the .cpp, .cxx or .cc extension suffixes.
// C have .c

#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main() 
{
    vector<string> msg {"Hello", "C++", "World", "from", "VS Code", "and the C++ extension!"};

    for (const string& word : msg)
    {
        cout << word << " ";
    }
    cout << endl;
}

// Choose C/C++: g++.exe build and debug active file from the list of detected compilers on your system.
// g++ is for C++, gcc is for C
// tasks.json stores your build configurations.
// CTRL + / = // , there's manz shortcuts for programmers with the ENG keyboard
// In case you need to change the default compiler, you can run Tasks: Configure Default Build Task


