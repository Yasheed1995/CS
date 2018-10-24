/*shellcodetest.c*/
#include <stdio.h>
int main(int argc, char **argv)
{
    unsigned char buf[1000];
    int n = read(0, buf, 1000);
    ((int(*)())buf)();
}
