#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n;
    scanf("%d",&n);

    int a[n];

    for(int i=0; i<n; i++)
    {
        scanf("%d",&a[i]);
    }

    int two=0,three=0;
    for(int i=0; i<n; i++)
    {

        if(a[i]%2==0)
        {
            two++;
            continue;
        }
        if(a[i]%3==0)
        {
            three++;
        }

    }

    printf("%d %d",two,three);

    return 0;
}
