#include <stdio.h>
#include <stdlib.h>

int main()
{
    int test;
    scanf("%d",&test);

    while(test>0)
    {
        int n;

        scanf("%d",&n);

        int a[n],b[n],c[n],ini[n];

        for(int i=0; i<n; i++)
        {
            scanf("%d",&ini[i]);
        }

        //copy in a from ini array.
        for(int i=0; i<n; i++)
        {
            a[i]=ini[i];

        }

        //shorting ini array
        for(int i=0; i<n-1; i++)
        {
            for(int j=i+1; j<n; j++)
            {
                if(ini[i]>ini[j])
                {
                    int temp=ini[i];
                    ini[i]=ini[j];
                    ini[j]=temp;
                }
            }
        }


        //copy ini array in b array after shorting.
        for(int i=0; i<n; i++)
        {
            b[i]=ini[i];

        }

        //Difference between a and b array.
        for(int i=0; i<n; i++)
        {
            c[i]=a[i]-b[i];
            if(c[i]<0)
            {
                c[i]=c[i]*(-1);
            }
        }

        //Final output.
        for(int i=0; i<n; i++)
        {
            printf("%d ",c[i]);
        }

        printf("\n");

        test--;
    }

    return 0;
}
