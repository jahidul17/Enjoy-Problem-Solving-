#include <bits/stdc++.h>

using namespace std;

int main()
{

    double r;
    cin >> r;
    double pi = 3.141592653;
    // when count digit after (.) then use fixed keyword before setprecision
    cout << fixed << setprecision(9) << pi * r * r;
    return 0;
}