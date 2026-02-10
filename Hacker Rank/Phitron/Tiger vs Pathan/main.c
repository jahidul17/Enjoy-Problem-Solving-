#include <stdio.h>
#include <stdlib.h>

int main()
{
    int test;
    scanf("%d",&test);

    while(test>=1)
    {
        int n;
        scanf("%d",&n);

        char s[n];
        scanf("%s",&s);

        int t=0;
        int p=0;
        for(int i=0; i<n; i++)
        {
            if(s[i]=='T')
            {
                t++;
            }
            if(s[i]=='P')
            {
                p++;
            }
        }

        if(t<p)
        {
            printf("Pathaan\n");
        }
        else if(p<t)
        {
            printf("Tiger\n");
        }
        else
        {
            printf("Draw\n");
        }

        test--;
    }

    return 0;
}
