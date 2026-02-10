#include <bits/stdc++.h>

using namespace std;

int main()
{
    string s;
    int flag=0;
    getline(cin,s);

    stringstream ss(s);

    string word;

    while(ss>>word)
    {
        if(word=="Jessica")
        {
            flag++;
            break;
        }

    }
    if(flag==1)
    {
        cout<<"YES"<<endl;
    }
    else
    {
        cout<<"NO"<<endl;
    }

    return 0;
}
