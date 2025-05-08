#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        string str;
        cin >> str;
        int a = str[0] - 48;
        int b = str[2] - 48;
        cout << a + b << endl;
    }
}