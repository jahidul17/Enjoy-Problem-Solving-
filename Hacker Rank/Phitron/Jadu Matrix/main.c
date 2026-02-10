#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n,m;
    scanf("%d %d",&n,&m);

    int a[n][m];

    for(int i=0; i<n; i++)
    {
        for(int j=0; j<m; j++)
        {
            scanf("%d",&a[i][j]);
        }
    }

    int flag=1;

    if(m!=n)
    {
        flag=0;
    }

    for(int i=0; i<n; i++)
    {
        for(int j=0; j<m; j++)
        {
            if((i+j)==m-1 || i==j)
            {

                if(a[i][j]!= 1)
                {
                    flag=0;
                }
                continue;
            }
            else if(i!=j)
            {
                if(a[i][j]!=0)
                {
                    flag=0;
                }
            }
        }

    }

    if(flag==1){
        printf("YES");
    }
    else{
        printf("NO");
    }


    return 0;
}
