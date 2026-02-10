#include <stdio.h>
#include <stdlib.h>

int main()
{
    int i,n,sumofposs=0,sumofneg=0,test;

    scanf("%d",&test);

    for(i=1;i<=test;i++){
        scanf("%d",&n);
        if(n>=0){
            sumofposs=sumofposs+n;
        }
        else{
            sumofneg=sumofneg+n;
        }
    }

    printf("%d %d",sumofposs,sumofneg);

    return 0;
}
