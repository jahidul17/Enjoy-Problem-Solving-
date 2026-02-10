#include <stdio.h>
#include <stdlib.h>

int main()
{
    int t;
    scanf("%d",&t);

    for(int i=1;i<=t;i++){
        char s[10001];
        int capital=0,small=0,digits=0;
        scanf("%s",s);

        for(int j=0;j<strlen(s);j++){

            if(s[j]>='A' && s[j]<='Z'){
                capital++;
            }
            else if(s[j]>='a' && s[j]<='z'){
                small++;
            }
            else{
                digits++;
            }

        }

        printf("%d %d %d\n",capital,small,digits);


    }

    return 0;
}
