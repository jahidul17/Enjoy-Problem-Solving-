#include <stdio.h>
#include <stdlib.h>

void odd_even()
{
    int n;
    scanf("%d",&n);

    int a[n];
    int even=0,odd=0;

    for(int i=0; i<n; i++)
    {
        scanf("%d",&a[i]);
    }

    for(int i=0; i<n; i++)
    {
        if(a[i]%2==0)
        {
            even++;
        }
        else
        {
            odd++;
        }
    }

    printf("%d %d",even,odd);

}


int main()
{

    odd_even();

    return 0;
}
