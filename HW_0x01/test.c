#include <stdio.h>

int main()
{
    char name[8];
    printf("please type your name: ");
    gets(name);
    printf("Hello, %s", name);
    return 0;
}
