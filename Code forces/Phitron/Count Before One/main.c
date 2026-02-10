#include <stdio.h>
#include <stdlib.h>

int count=0;

int count_before_one(int *a,int n)
{

    for(int i=0; i<n; i++)
    {
        if(a[i]==1)
        {
            break;
        }
        else
        {
            count++;
        }
    }

    return count;

}

int main()
{
    int n;
    scanf("%d",&n);

    int a[n];

    for(int i=0; i<n; i++)
    {
        scanf("%d",&a[i]);
    }

    count_before_one(a,n);

    printf("%d",count);

    return 0;
}
