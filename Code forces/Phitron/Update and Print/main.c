#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n,x,v,i;

    scanf("%d",&n);

    int a[n];

    for(i=0;i<n;i++){
        scanf("%d",&a[i]);
    }


    //scan index and value
    scanf("%d %d",&x,&v);

    for(i=0;i<n;i++){
        if(x==i){
            a[i]=v;
        }
    }


    for(i=n-1;i>=0;i--){
        printf("%d ",a[i]);
    }



    return 0;
}
