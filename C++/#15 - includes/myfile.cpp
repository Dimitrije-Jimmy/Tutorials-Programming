extern int x;
/*
This means "There is this variable 'x' somewhere externally, we know it's there,
 outside of this class, and it's defined, we don't need to initialize it"
*/

int test = 350;     // defining a variable to access externally in main.cpp

int add_to_x(int i) {
    return x + i;
}