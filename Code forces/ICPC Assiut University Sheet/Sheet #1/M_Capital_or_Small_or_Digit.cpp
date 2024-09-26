#include <stdio.h>
#include <stdlib.h>

int main()
{
    char x;
    scanf("%c", &x);

    if ((x >= 'a' && x <= 'z') || (x >= 'A' && x <= 'Z'))
    {
        printf("ALPHA\n");
        if (x >= 'a' && x <= 'z')
        {
            printf("IS SMALL");
        }
        else
        {
            printf("IS CAPITAL");
        }
    }
    else if (x >= '0' && x <= '9')
    {
        printf("IS DIGIT");
    }

    return 0;
}
