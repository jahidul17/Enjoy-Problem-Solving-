#include <bits/stdc++.h>

using namespace std;

int main()
{

    int n, a[1000], b[1000];
    cin >> n;

    for (int i = 0; i < n; i++)
    {
        cin >> a[i] >> b[i];
    }

    int max = b[0], maximum = b[0];

    for (int j = 1; j < n; j++)
    {
        max = max - a[j];
        max = max + b[j];

        if (maximum < max)
        {
            maximum = max;
        }
    }
    cout << maximum;

    return 0;
}