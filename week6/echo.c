#include <stdio.h>

int main() 
{
    char buf[0x100];

    while( scanf("%s", buf) != EOF ) {
        printf(buf);
        printf("\n");
    }
    return 0;
}
