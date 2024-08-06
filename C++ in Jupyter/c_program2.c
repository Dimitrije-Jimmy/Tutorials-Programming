
#include <stdio.h>

int main (int argc, char **argv) {
    int i;

    i = 0;
    // Accidentally built infinite loop ._.
    while (i < argc) {
        printf("argv[%d]: %s\n", i, argv[i]);
        i++;
    }

    return (0);
}
