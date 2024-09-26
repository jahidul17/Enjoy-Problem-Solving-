#include <bits/stdc++.h>

using namespace std;

int main()
{

    long long int n, sum;
    cin >> n;
    // can not use loop case of TLE
    //  for (int i = 1; i <= n; i++)
    //  {
    //      sum += i;
    //  }

    sum = n * (n + 1) / 2;
    cout << sum;
    return 0;
}