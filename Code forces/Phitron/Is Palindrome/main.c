#include <stdio.h>
#include <stdlib.h>

int flag=1;
int is_palindrome(char *s,int n)
{

    for(int i=0,j=n; i<j; i++,j--)
    {
        if(s[i]==s[j])
        {
            continue;
        }
        else
        {
            flag=0;
            break;
        }

    }

    return flag;


}

int main()
{
    char s[1001];

    scanf("%s",s);

    int sz=strlen(s)-1;

    is_palindrome(s,sz);

    if(flag==1)
    {
        printf("Palindrome");
    }
    else
    {
        printf("Not Palindrome");
    }

    return 0;
}
