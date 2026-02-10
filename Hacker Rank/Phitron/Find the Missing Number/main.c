#include <stdio.h>
#include <stdlib.h>

int main()
{
    int test;

    scanf("%d",&test);

    while(test>1)
    {
        long long int m;

        int a,b,c,d;

        scanf("%d %d %d %d",&m,&a,&b,&c);

        d=a*b*c;

        if(m%d==0)
        {
            printf("%d\n",m/d);
        }
        else if(m%d!=0)
        {
            printf("-1\n");

        }
        else if(m==0 || d==0)
        {
            printf("0\n");
        }

        test--;
    }


    return 0;
}
