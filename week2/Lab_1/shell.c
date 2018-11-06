# include <stdlib.h>
# include <stdio.h>
# include <unistd.h>

int main()
{
    unsigned char  buf[1000];
    int n = read(0, buf, 1000);
    ((int(*)())buf)();
}
