#include <stdio.h>
int cal(int a, int b, int c)
{
    int i, j, k;
    int total = 0;
    for(i = 0; i < a; i++)
    {
        for(j = 0; j < b; j++)
        {
            for(k = 0; k < c; k++)
            {
                if(i > k && j < i)
                    return cal(a-1, b-1, c-1);
                return total + cal(a-1, b-1, c-1);
            }
        }
    }
    return 1;
}
int main(int argc, char *argv[]) {
	int a = cal(1,4444,3);
	printf("%d", a);
}