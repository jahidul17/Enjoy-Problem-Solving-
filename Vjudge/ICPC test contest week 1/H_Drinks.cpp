#include <bits/stdc++.h>

using namespace std;

int main()
{
    int n, val;
    cin >> n;
    int sum = 0;
    for (int i = 1; i <= n; i++)
    {
        cin >> val;
        sum = sum + val;
    }

    double avg = double(sum) / n;
    cout << fixed << setprecision(12) << avg;

    return 0;
}