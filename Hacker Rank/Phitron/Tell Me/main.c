#include <stdio.h>
#include <stdlib.h>

int main()
{
    int t;
    scanf("%d",&t);

    for(int i=1; i<=t; i++)
    {

        int n,x;
        scanf("%d",&n);

        int a[n];
        for(int j=0; j<n; j++)
        {
            scanf("%d ",&a[j]);
        }

        scanf("%d",&x);
        int get=0;
        for(int j=0; j<n; j++)
        {

            if(x==a[j])
            {
                get++;
                break;
            }

        }

        if(get==1)
        {
            printf("YES\n");
        }
        else
        {
            printf("NO\n");
        }

    }


    return 0;
}
