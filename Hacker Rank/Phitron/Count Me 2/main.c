#include <stdio.h>
#include <stdlib.h>

int main()
{
    char s[100000];
    int consonants=0;
    scanf("%s",s);

    for(int i=0;i<strlen(s);i++){
        if(s[i]!='a' && s[i]!='e' && s[i]!='i' && s[i]!='o' && s[i]!='u' ){
            consonants++;
        }

    }

    printf("%d",consonants);


    return 0;
}
