#include <bits/stdc++.h>

using namespace std;

int main()
{
    int test;
    cin>>test;
    while(test>=1)
    {

        string s,x;

        cin>>s>>x;

        int xl=x.length();


        while(s.find(x) != -1)
        {
            s.replace(s.find(x),xl,"#");
        }

        cout<<s<<endl;

        test--;
    }


    return 0;
}
