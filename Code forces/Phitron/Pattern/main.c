#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n,st=1;
    scanf("%d",&n);

    int sp=n-1;

    for(int row=1; row<=(n*2)-1; row++)
    {


        for(int j=1; j<=sp; j++)
        {
            printf(" ");
        }

        if(row%2!=0)
        {
            for(int j=1; j<=st; j++)
            {
                printf("#");
            }
        }
        else
        {
            for(int j=1; j<=st; j++)
            {
                printf("-");
            }
        }


        if(row>=n)
        {
            sp++;
            st-=2;
        }
        else
        {
            sp--;
            st+=2;
        }

        printf("\n");

    }

    return 0;
}
