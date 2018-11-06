#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main()
{
    char *p = malloc(0x108);
    malloc(0x108);
    malloc(0x108);
    free(p);
}
