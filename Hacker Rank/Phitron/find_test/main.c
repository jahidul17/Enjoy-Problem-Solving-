#include <stdio.h>
#include <stdlib.h>

int main()
{
    int test;

    scanf("%d",&test);

    while(test>0)
    {
        long long int m,d;

        int a,b,c;

        scanf("%d %d %d %d",&m,&a,&b,&c);

        d=a*b*c;

        if(m%d==0)
        {
            printf("%lld\n",m/d);
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
