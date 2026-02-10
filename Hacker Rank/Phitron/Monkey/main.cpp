#include <bits/stdc++.h>

using namespace std;

int main()
{

    string s;


    while(getline(cin,s))
    {
        //This is built in function and known from geeksforgeeks
        //Reference: https://www.geeksforgeeks.org/remove-spaces-from-a-given-string/
        s.erase(remove(s.begin(), s.end(), ' '), s.end());

        sort(s.begin(), s.end());

        cout<<s<<endl;

    }
    return 0;
}
