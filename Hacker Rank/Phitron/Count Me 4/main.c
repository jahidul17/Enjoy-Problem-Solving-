#include <stdio.h>
#include <stdlib.h>

int main()
{
    char s[10001];

    scanf("%s",s);

    int val;
    int count[26]={0};
    //count string
    for(int i=0;i<strlen(s);i++){

        val=s[i]-'a';
        count[val]++;

    }

    //a-z print and count
    for(int i=0;i<26;i++){
            if(count[i]==0){
                continue;
            }
        printf("%c - %d\n",i+97,count[i]);
    }

    return 0;
}
