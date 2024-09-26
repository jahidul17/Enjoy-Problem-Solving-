#include <stdio.h>
#include <stdlib.h>

int main()
{
    int x, div;

    scanf("%d", &x);

    div = x / 1000;

    if (div % 2 == 0)
    {
        printf("EVEN");
    }
    else
    {
        printf("ODD");
    }

    return 0;
}